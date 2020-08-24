import zeep
import json

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# wsdl = 'http://www.byjg.com.br/site/webservice.php/ws/cep?WSDL'
wsdl = 'http://INDTs-MacBook-Pro.local:8088/mockXacuteWSSoap?wsdl'

client = zeep.Client(wsdl=wsdl)
# print(client.service.obterCEP('Zeep TESTE', 'is cool', 'DF'))

request_data = {
    'logradouro': 'QND 56',
    'localidade': 'Brasilia',
    'UF': 'DF'
}

print(client.service.Xacute())

print(client.service.Xacute()["Row"][0]["cd_posto"])

# a = zeep.helpers.serialize_object(client.service.Xacute())

# json_object_a = json.loads(json.dumps(a))

# print(json_object_a)

# print(json_object_a["Row"][0]["cd_posto"])