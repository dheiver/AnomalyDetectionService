```markdown
# API de Detecção de Anomalias em Séries Temporais

Esta é uma API baseada em SOAP que permite a detecção de anomalias em dados de séries temporais usando Modelos de Mistura de Gaussianas (GMM). A API é capaz de lidar com tanto uma única série temporal quanto várias séries temporais.

## Pré-requisitos

- Python 3.x
- NumPy
- pandas
- scikit-learn
- spyne

## Começando

1. Instale as dependências necessárias utilizando o seguinte comando:

   ```
   pip install numpy pandas scikit-learn spyne
   ```

2. Execute o servidor da API utilizando o código fornecido:

   ```bash
   python seu_arquivo_da_api.py
   ```

3. A API começará a ser servida na porta 8000.

## Utilização da API

### Endpoint: `/detect_anomalies`

Este endpoint aceita uma requisição SOAP com os seguintes parâmetros:

- `time_series_data`: Uma lista de listas representando os dados das séries temporais (colunas).
- `sensitivity` (opcional): Um parâmetro de sensibilidade para a detecção de anomalias (o padrão é 1.0).
- `percentile` (opcional): Um parâmetro de percentil para a detecção de anomalias (o padrão é 5.0).

#### Exemplo de Requisição:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://schemas.spyne.io/web">
   <soapenv:Header/>
   <soapenv:Body>
      <web:detect_anomalies>
         <time_series_data>
            <item>
               <item>1.2</item>
               <item>2.5</item>
               <!-- Mais pontos de dados -->
            </item>
            <!-- Mais séries -->
         </time_series_data>
         <sensitivity>1.5</sensitivity>
         <percentile>10.0</percentile>
      </web:detect_anomalies>
   </soapenv:Body>
</soapenv:Envelope>
```

#### Exemplo de Resposta:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://schemas.spyne.io/web">
   <soapenv:Header/>
   <soapenv:Body>
      <web:detect_anomaliesResponse>
         <return>
            <item>
               <item>2</item>
               <item>5</item>
               <!-- Índices das anomalias detectadas -->
            </item>
            <!-- Anomalias para outras séries -->
         </return>
      </web:detect_anomaliesResponse>
   </soapenv:Body>
</soapenv:Envelope>
```

## Observações

- A API foi projetada para fins educacionais e ilustrativos. Recomenda-se estender e aprimorar o código para atender a requisitos específicos, como tratamento de erros, segurança e escalabilidade.
- Sempre valide e processe seus dados antes de passá-los para a API.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

```

Lembre-se de substituir `seu_arquivo_da_api.py` pelo nome real do seu arquivo de código da API. Personalize as instruções e os exemplos conforme necessário para corresponder ao seu ambiente e cenário específicos. Certifique-se de fornecer informações claras para os usuários entenderem como usar a API e o que esperar dela.
