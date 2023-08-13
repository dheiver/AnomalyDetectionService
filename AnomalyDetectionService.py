from spyne import Application, rpc, ServiceBase, Unicode, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture

class AnomalyDetectionService(ServiceBase):
    @rpc(Array(Array(Float)), Float, Float, _returns=Array(Array(Unicode)))
    def detect_anomalies(self, time_series_data, sensitivity=1.0, percentile=5.0):
        results = []
        
        # Função para detectar anomalias usando GMM
        def detect_anomalies_gmm(data, n_components=2, percentile=5, sensitivity=1.0):
            gmm = GaussianMixture(n_components=n_components)
            gmm.fit(data.values.reshape(-1, 1))
            likelihood = gmm.score_samples(data.values.reshape(-1, 1))
            threshold = np.percentile(likelihood, percentile) * sensitivity
            return data.index[likelihood < threshold]

        if len(time_series_data) == 1:
            time_series_data = time_series_data[0]
            data_frame = pd.DataFrame(time_series_data)
            anomalies = []
            for column in data_frame.columns:
                anomalies_column = detect_anomalies_gmm(data_frame[column], sensitivity=sensitivity)
                anomalies.append([str(idx) for idx in anomalies_column])
            results.append(anomalies)
        else:
            for time_series in time_series_data:
                data_frame = pd.DataFrame(time_series)
                anomalies = []
                for column in data_frame.columns:
                    anomalies_column = detect_anomalies_gmm(data_frame[column], sensitivity=sensitivity)
                    anomalies.append([str(idx) for idx in anomalies_column])
                results.append(anomalies)
        
        return results

application = Application([AnomalyDetectionService], 'anomaly_detection_service',
                          in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, wsgi_application)
    print("Servindo na porta 8000...")
    server.serve_forever()
