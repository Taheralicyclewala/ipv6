import re



def isIP(target):
    IP=str(target)
    if len(IP.rsplit(':')) is 8 and '-' not in IP and '/' not in IP:
        
        ip_flag = True
        for num in IP.rsplit(':'):
            try:
                part = str(num)
              #  print (part)

                matchObj = re.search((r'[a-zA-Z0-9]'),part,re.I)

               # if matchObj:

                print(matchObj.group())
                #else:
            #        print("NO match")

            except:
                ip_flag = False
        return ip_flag
    return False

target = input("enter ipv6 address")

(isIP(target))
