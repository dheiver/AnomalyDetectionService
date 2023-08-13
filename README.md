```markdown
# Anomaly Detection API for Time Series

![GitHub](https://img.shields.io/github/license/your-username/anomaly-detection-api)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

This is a SOAP-based API that allows you to detect anomalies in time series data using Gaussian Mixture Models (GMM). The API can handle both single time series and multiple time series.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Usage](#api-usage)
- [Examples](#examples)
- [Notes](#notes)
- [License](#license)

## Prerequisites

- Python 3.x
- NumPy
- pandas
- scikit-learn
- spyne

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/anomaly-detection-api.git
   cd anomaly-detection-api
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:

   ```bash
   python your_api_script_name.py
   ```

4. The API will start serving on port 8000.

## API Usage

### Endpoint: `/detect_anomalies`

This endpoint accepts a SOAP request with the following parameters:

- `time_series_data`: A list of lists representing time series data (columns).
- `sensitivity` (optional): A sensitivity parameter for anomaly detection (default is 1.0).
- `percentile` (optional): A percentile parameter for anomaly detection (default is 5.0).

#### Request Example:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://schemas.spyne.io/web">
   <soapenv:Header/>
   <soapenv:Body>
      <web:detect_anomalies>
         <time_series_data>
            <item>
               <item>1.2</item>
               <item>2.5</item>
               <!-- More data points -->
            </item>
            <!-- More series -->
         </time_series_data>
         <sensitivity>1.5</sensitivity>
         <percentile>10.0</percentile>
      </web:detect_anomalies>
   </soapenv:Body>
</soapenv:Envelope>
```

#### Response Example:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://schemas.spyne.io/web">
   <soapenv:Header/>
   <soapenv:Body>
      <web:detect_anomaliesResponse>
         <return>
            <item>
               <item>2</item>
               <item>5</item>
               <!-- Detected anomaly indexes -->
            </item>
            <!-- Anomalies for other series -->
         </return>
      </web:detect_anomaliesResponse>
   </soapenv:Body>
</soapenv:Envelope>
```

## Examples

For more usage examples, refer to the [Examples](examples/) directory.

## Notes

- The API is designed for educational and illustrative purposes. It's recommended to extend and enhance the code to meet specific requirements, such as error handling, security, and scalability.
- Always validate and preprocess your data before passing it to the API.

## License

This project is licensed under the [MIT License](LICENSE).
```

Este README.md inclui algumas melhorias, como um badge de licença, uma tabela de conteúdos, um link para exemplos e mais detalhes de uso. Certifique-se de ajustar o nome do repositório, as instruções de instalação e as URLs de acordo com o seu projeto. Isso ajudará os usuários a entenderem e usarem a sua API no GitHub.
