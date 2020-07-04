import socket              
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = "192.168.0.166" 
port = 9100   
# zpl = """
# ^XA
# ^RFR,H,0,8,2^FN1^FS^HV1,,8-byte Tag ID Data:^FS
# ^XZ
# """
zpl = """
^XA
^FO50,50
^A0N,65
^FDSimple write example
^FS
^RFW,H
^FD112233445566778899001122
^FS
^XZ
"""
try:           
    mysocket.connect((host, port)) #connecting to host
    # mysocket.send(b"~hs")#using bytes
    # mysocket.send(b"~hl")#using bytes
    mysocket.send(bytes(zpl, "utf-8"))
    data = mysocket.recv(1024)
    stringdata = data.decode('utf-8')
    print(stringdata) 
    mysocket.close () #closing connection
except:
    print("Error in connection")