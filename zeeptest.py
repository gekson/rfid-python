import zeep

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
wsdl = 'http://www.byjg.com.br/site/webservice.php/ws/cep?WSDL'

client = zeep.Client(wsdl=wsdl)
# print(client.service.obterCEP('Zeep TESTE', 'is cool', 'DF'))

request_data = {
    'logradouro': 'QND 56',
    'localidade': 'Brasilia',
    'UF': 'DF'
}

print(client.service.obterCEP(**request_data))