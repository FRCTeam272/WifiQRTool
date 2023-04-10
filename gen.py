import subprocess
import wifi_qrcode_generator

try:
    # grab output
    Id = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
    
    # extract SSID
    id_results = str([b.split(":")[1][1:-1]
                      for b in Id if "Profile" in b])[2:-3]
    
    # grab Passwords
    password = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles',
         id_results, 'key=clear']).decode('utf-8').split('\n')
    
    # extract specific password
    pass_results = str([b.split(":")[1][1:-1]
                        for b in password if "Key Content" in b])[2:-2]
    print("User name :", id_results)
    print("Password :", pass_results)

    # generate QR Code - save it to a file names the SSID        
    code = wifi_qrcode_generator.wifi_qrcode(id_results, False, 'WPA', pass_results)
    code.print_ascii()
    code.make_image().save(f'{id_results}.png')
except:
    print("something wrong")
     