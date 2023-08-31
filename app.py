import time
from ppadb.client import  Client as AdbClient
#def connect():
    
    

if __name__=='main':
    client=AdbClient(host='127.0.0.1', port=5037)#this is the default
    
    devices=client.devices()
    
    if len(devices)==0:
        print('No devices')
        quit()
    device= devices[0]
    
    print(f'conected to {device}')