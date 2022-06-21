import requests

print("""

██╗██████╗░░██╗░░░░░░░██╗██╗░░██╗░█████╗░██╗░██████╗
██║██╔══██╗░██║░░██╗░░██║██║░░██║██╔══██╗██║██╔════╝
██║██████╔╝░╚██╗████╗██╔╝███████║██║░░██║██║╚█████╗░
██║██╔═══╝░░░████╔═████║░██╔══██║██║░░██║██║░╚═══██╗
██║██║░░░░░░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝██║██████╔╝
╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░

[To Get Info About Any Public Ip]

Telegram @ifostn - instagram @f09l - Twitter @lwv5

""")
IP_TARGET = input("Enter Public Ip : ")
url = (f'https://ipwho.is/{IP_TARGET}')
info = requests.get(url).json()
if info["success"] == False:
    print('Sorry no information')
elif IP_TARGET == "":
    print("Please enter correct IP")

else:
    print('type : '+str(info['type']))
    print('continent : '+str(info['continent']))
    print('continent code : '+str(info['continent_code']))
    print('country : '+str(info['country']))
    print('region : '+str(info['region']))
    print('city : '+str(info['city']))
    print('postal : '+str(info['postal']))
    print('capital : '+str(info['capital']))
    print('calling code : '+str(info['calling_code']))
    print('isp : '+str(info['connection']['isp']))
    print('domain : '+str(info['connection']['domain']))
    print('current time : '+str(info['timezone']['current_time']))
