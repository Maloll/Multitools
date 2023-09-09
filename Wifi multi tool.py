import os
from pystyle import Colors, Colorate
import re
import subprocess
import time
print(Colorate.Vertical(Colors.red_to_purple, """
██╗    ██╗██╗███████╗██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║    ██║██║██╔════╝██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║ █╗ ██║██║█████╗  ██║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║███╗██║██║██╔══╝  ██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
╚███╔███╔╝██║██║     ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                        
""", 2))
print(Colorate.Diagonal(Colors.white_to_red, """ 
[1] Wifi Password (take the passwords of the wifi you have already connected to)
[2] Wifi List (list of the wifi you have already connected to)
[3] Wlan Info (get all the informations about your wifi)

""", 1))
print("""         """)
select = int(input("Selection : "))

if select == 1 :
    os.system('cls')
    time.sleep(0.40)
    print(Colorate.Vertical(Colors.white_to_green, """ 
    
██╗    ██╗██╗███████╗██╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██║    ██║██║██╔════╝██║    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██║ █╗ ██║██║█████╗  ██║    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██║███╗██║██║██╔══╝  ██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
╚███╔███╔╝██║██║     ██║    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                               

    """, 2))
    time.sleep(0.35)
        
    netsh_cmd = 'netsh wlan show profiles'
    netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
    pattern = r'User profiles\n-+\n([\s\S]+?)\n\n'
    match = re.search(pattern, netsh_output)
    if match:
        user_profiles = match.group(1)
        
        user_profiles = user_profiles.strip().split('\n')
        
        profile_names = [line.strip() for line in user_profiles if 'All User Profile' in line]
       
        for profile_name in profile_names:
            print(Colorate.Horizontal(Colors.white_to_green, profile_name, 2))
    else:
        print(Colorate.Horizontal(Colors.white_to_green, "No profile found", 2))
    print("""       """)
    wifiname = input(Colorate.Horizontal(Colors.white_to_green, "Wifi name : ", 2))
    print("""       """)
    netsh_cmd = f'netsh wlan show profile name="{wifiname}" key=clear'
    netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
    pattern = r'Key Content\s+:\s+(.+)'

    match = re.search(pattern, netsh_output)
    
    if match:
        key_content = match.group(1)
        print(Colorate.Horizontal(Colors.green_to_white, "Password :", 1), Colorate.Horizontal(Colors.green_to_white, key_content, -1))
    else:
        print("Password not found")
    print("""       """)
    print(Colorate.Horizontal(Colors.red_to_yellow, "press enter to exit", -1))
    input()

if select == 2 :
    os.system('cls')
    netsh_cmd = 'netsh wlan show profiles'
    netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
    pattern = r'User profiles\n-+\n([\s\S]+?)\n\n'
    match = re.search(pattern, netsh_output)
    if match:
        user_profiles = match.group(1)
        
        user_profiles = user_profiles.strip().split('\n')
        
        profile_names = [line.strip() for line in user_profiles if 'All User Profile' in line]
       
        for profile_name in profile_names:
            print(Colorate.Horizontal(Colors.white_to_green, profile_name, 2))
    else:
        print(Colorate.Horizontal(Colors.white_to_green, "No profile found", 2))
    print("""       """)



if select == 3 :
    
    os.system('cmd /c "netsh wlan show interfaces"')
    print("""       """)
    print(Colorate.Horizontal(Colors.red_to_yellow, "press enter to exit", -1))
    input()