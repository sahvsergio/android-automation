import time
from ppadb.client import Client as AdbClient

def connect():
        client=AdbClient(host='127.0.0.1', port=5037)#Default is 127.0.0.1 and 5037
        devices=client.devices()
        
        if len(devices)==0:
            print('No devices')
            
        device = devices[0]
        print(f'Connect to {device}')
        return device, client


def take_selfie():
    device.shell('input keyevent 27')
    # wait 5 seconds
    time.sleep(5)
    # take a photo with volume up
    device.shell('input keyevent 24')
    
    print('Taken a photo!')   
    

def oen_wp():
     
    device.shell('am start -a com.whatsapp/com.whatsapp.Main')
    



if __name__=='__main__':
    
    device,client=connect()
    
    
    
    device.shell('input keyevent KEYCODE_CAMERA')
    
    
    
    time.sleep(5)
    device.shell('input keyevent KEYCODE_VOLUME_UP')
    #device.shell('am start -a android.media.action.IMAGE_CAPTURE')
    #print('Taken a picture')
    #opening
    #device.shell('am start -a com.whatsapp/com.whatsapp.Main')
    
    #device.shell(' input keyevent KEYCODE_CALENDAR')
    
