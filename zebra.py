import socket              
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = "192.168.0.166" 
port = 9100   
# zpl = """
# ^XA
# ^RFR,H,0,8,2^FN1^FS^HV1,,8-byte Tag ID Data:^FS
# ^XZ
# """
# 112233445566778899001122
# 4A840J49C

# Hexadecimal
# zpl = """
# ^XA
# ^FO50,50
# ^A0N,65
# ^FD4A840J49C
# ^FS
# ^RFW,H
# ^FD112233445566778899001122
# ^FS
# ^XZ
# """

# ASCII
# zpl = """
# ^XA
# ^FO50,50
# ^A0N,65
# ^FD4A840J49C
# ^FS
# ^RFW,A
# ^FD4A840J49C
# ^FS
# ^XZ
# """

# zpl = """
# ^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR2,2~SD28^JUS^LRN^CI0^XZ
# ^XA
# ^MMT
# ^PW1063
# ^LL0591
# ^LS0
# ^RFW,A
# ^FD4A840J49C
# ^FS
# ^FT250,30^A0N,25,33^FH\^FDNS^FS
# ^BY3,3,52^FT140,100^BCN,,N,N
# ^FD19271^FS
# ^FT230,130^A0N,25,33^FH\^FD4A840J49C^FS
# ^PQ1,0,1,Y^XZ
# ^XZ
# """

zpl = """
^XA
^RS8
^RFW,A,3,4,1^FD4A840J49C^FS
^RFW,A,,,3^FD123Z1456^FS
^XZ
"""

# zpl = """
# ^XA
# ^FO100,100^BY3
# ^BCN,100,Y,N,N
# ^FD25012345678^FS
# ^RB96,8,28,16,8,36
# ^RFW,E
# ^FD53.1000.250.0.12345678^FS
# ^RFW,H,,4,3^FD12345678^FS
# ^XZ
# """
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