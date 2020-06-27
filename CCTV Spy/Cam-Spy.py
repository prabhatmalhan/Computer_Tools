"""
Author : PRABHAT MALHAN
         B.Tech CSE (Hons.)
         GRAPHIC ERA UNIVERSITY

Inspiration : Angel Security Team
"""

import requests,re,os
import datetime

now = datetime.datetime.now()

print("""
██████╗  ██████╗   █████╗   ██████╗ ██╗  ██╗ ███████╗ ██████╗  ███████╗
██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔════╝ ██║ ██╔╝ ██╔════╝ ██╔══██╗ ██╔════╝
██████ ║ ██████╔╝ ███████║ ██║      █████╔╝  █████╗   ██████╔╝ ███████╗
██╔════╝ ██╔══██╗ ██╔══██║ ██║      ██╔═██╗  ██╔══╝   ██╔══██╗ ╚════██║
██║      ██║  ██║ ██║  ██║ ╚██████╗ ██║  ██╗ ███████╗ ██║  ██║ ███████║
╚═╝      ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚══════╝
                                                 DARCY SECURITY SYSTEMS"""+

f' \n\nAccess Time : {now.hour}:{now.minute}:{now.second}\n\n'+

"""
1)United States                31)Mexico                61)Moldova
2)Japan                        32)Finland               62)Nicaragua
3)Italy                        33)China                 63)Malta
4)Korea                        34)Chile                 64)Trinidad And Tobago
5)France                       35)South Africa          65)Soudi Arabia
6)Germany                      36)Slovakia              66)Croatia
7)Taiwan                       37)Hungary               67)Cyprus
8)Russian Federation           38)Ireland               68)Pakistan
9)United Kingdom               39)Egypt                 69)United Arab Emirates
10)Netherlands                 40)Thailand              70)Kazakhstan
11)Czech Republic              41)Ukraine               71)Kuwait
12)Turkey                      42)Serbia                72)Venezuela
13)Austria                     43)Hong Kong             73)Georgia
14)Switzerland                 44)Greece                74)Montenegro
15)Spain                       45)Portugal              75)El Salvador
16)Canada                      46)Latvia                76)Luxembourg
17)Sweden                      47)Singapore             77)Curacao
18)Israel                      48)Iceland               78)Puerto Rico
19)Iran                        49)Malaysia              79)Costa Rica
20)Poland                      50)Colombia              80)Belarus
21)India                       51)Tunisia               81)Albania
22)Norway                      52)Estonia               82)Liechtenstein
23)Romania                     53)Dominican Republic    83)Bosnia And Herzegovia
24)Viet Nam                    54)Sloveania             84)Paraguay
25)Belgium                     55)Ecuador               85)Philippines
26)Brazil                      56)Lithuania             86)Faroe Islands
27)Bulgaria                    57)Palestinian           87)Guatemala
28)Indonesia                   58)New Zealand           88)Nepal
29)Denmark                     59)Bangladeh             89)Peru
30)Argentina                   60)Panama                90)Uruguay
                                                        91)Extra
""")



 
try:                                                               
    num = int(input("CHOICE : "))
    if num in range(1,92):
        print("\n")
        try:
            x = "".join(open("data","r").readlines()).split('\n')[num-1].split()
        except Exception:
            print('Data File not Found!!')
            exit()

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            files = open("URL DATA.txt",'w+')
            for page in range (0,int(x[0])):
			
                url = ("https://www.insecam.org/en/bycountry/"+x[1]+"/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     os.system('cls')
                     print('Loading'+'.'*(count%4))
                     hasil = findip[count]
                     files.write(hasil+'\n')                 
                     count += 1
            print('Done')
        except:
            print ("INTERNET NOT FOUND")
    else:
        print("INVALID COUNTRY")

except Exception:
        print ("INVALID INPUT")
