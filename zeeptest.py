import zeep
import json

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
wsdl = 'http://www.byjg.com.br/site/webservice.php/ws/cep?WSDL'

client = zeep.Client(wsdl=wsdl)
# print(client.service.obterCEP('Zeep TESTE', 'is cool', 'DF'))

request_data = {
    'logradouro': 'QND 56',
    'localidade': 'Brasilia',
    'UF': 'DF'
}

# print(client.service.obterCEP(**request_data))

a = zeep.helpers.serialize_object(client.service.obterCEP(**request_data))

json_object_a = json.loads(json.dumps(a))

# print a['data']['item'][0]['house_id']
print(json_object_a)