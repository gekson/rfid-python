# import zeep

# wsdl = 'http://INDTs-MacBook-Pro.local:8088/mockNumberConversionSoapBinding'
# client = zeep.Client(wsdl=wsdl)
# print(client.service.Method1('Zeep', 'is cool'))

from zeep import Client
from pprint import pprint
import operator

wsdl = 'http://www.byjg.com.br/site/webservice.php/ws/cep?WSDL'
# wsdl = 'http://INDTs-MacBook-Pro.local:8088/mockNumberConversionSoapBinding?wsdl'
client = Client(wsdl)
# result = client.service.NumberToDollars(100.0)

# assert result == 62.137

# for service in client.wsdl.services.values():
#     print("service:", service.name)
#     for port in service.ports.values():
#         operations = sorted(
#             port.binding._operations.values(),
#             key=operator.attrgetter('name'))

#         for operation in operations:
#             print("method :", operation.name)
#             print("  input :", operation.input.signature())
#             print()
#     print()

def parseElements(elements):
    all_elements = {}
    for name, element in elements:
        all_elements[name] = {}
        all_elements[name]['optional'] = element.is_optional
        if hasattr(element.type, 'elements'):
            all_elements[name]['type'] = parseElements(
                element.type.elements)
        else:
            all_elements[name]['type'] = str(element.type)

    return all_elements


interface = {}
for service in client.wsdl.services.values():
    interface[service.name] = {}
    for port in service.ports.values():
        interface[service.name][port.name] = {}
        operations = {}
        for operation in port.binding._operations.values():
            operations[operation.name] = {}
            operations[operation.name]['input'] = {}
            elements = operation.input.body.type.elements
            operations[operation.name]['input'] = parseElements(elements)
        interface[service.name][port.name]['operations'] = operations


pprint(interface)

request_data = {
    'logradouro': 'QND 56',
    'localidade': 'Brasilia',
    'UF': 'DF'
}

response = client.service.obterCEP(**request_data)