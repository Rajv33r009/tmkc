import mechanize
import os
import sys
from time import sleep
import requests

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)
url = 'https://m.facebook.com/login.php'

def openlink(msg4):
    r = browser.open(msg4)

def aclass():
    browser.open(url)
    browser.select_form(nr=0)
    browser.form['email'] = emailx
    browser.form['pass'] = pwx
    r = browser.submit()
    browser.select_form(nr=0)
    print("\033[1;37;96m", end = "")
    print(47 * '\033[1;37;1m-')
    msg1 = str(input("➣Enter 2 step google code : "))
    print("\033[1;37;96m", end = "")
    print(47 * '\033[1;37;1m-')
    print(msg1)
    browser.form['approvals_code'] = msg1
    print("\033[1;37;96m", end = "")
    print(47 * '\033[1;37;1m-')
    r = browser.submit()
    browser.select_form(nr=0)
    browser.form['name_action_selected'] = ['save_device']
    r = browser.submit()

def poct(comment):
    browser.select_form(nr=0)
    print("\033[1;37;40m")
    browser.form['comment_text'] = comment
    r = browser.submit()
    


print("\033[1;37;40m")
logo = ("""\033[97;1m
    



\033[1;37;96m _______    ______      _____            
\033[1;37;96m|       \  /      \    |     \           
\033[1;37;96m| $$$$$$$\|  $$$$$$\    \$$$$$           
\033[1;37;96m| $$__| $$| $$__| $$      | $$           
\033[1;37;96m| $$    $$| $$    $$ __   | $$           
\033[1;37;96m| $$$$$$$\| $$$$$$$$|  \  | $$           
\033[1;37;96m| $$  | $$| $$  | $$| $$__| $$           
\033[1;37;96m| $$  | $$| $$  | $$ \$$    $$           
\033[1;37;96m \$$   \$$ \$$   \$$  \$$$$$$            
                                         
                                           
x====The Speed Master Rajveer Own Fiire -X'wd====x

\033[0;34m[[ AUTHOR NAME ]]------------------[ RAJVEER SINGHANIYA ]

\033[0;33m[[ TOOL ]]------------------<3 = [ POST FIGHT WEAPON ]

\033[0;32m[[ RIDIT KI BH4N K4VIT4 K4 PY4R R4JV33R H3R3 ]]
                                                         

\033[1;37;96m""")
print(logo)
import getpass

attemps = 0

while attemps < 12345677901:
     username = input('ENTER USERNAME:')
     password = input('ENTER PASSWORD:')
     if username == 'Rajveer Papa' and password == 'shıwu ki mkb':
     
       print('You Have Successfully Logged in')
       break

       print('incorect please type')
       attemps +=1
       continue
os.system('clear')
print(logo)

def is_network_available():
    try:
        # Try to make a simple HTTP request to a known server (e.g., Google)
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

print("[-[ IF YOU THINK YOU ARE BAD I AM YOUR DAD]-]")
print("\033[1;37;96m", end = "")
print(47 * '\033[1;37;1m-')
emailx = str(input("➣Enter email : "))
print("\033[1;37;96m", end = "")
print(47 * '\033[1;37;1m-')
pwx = str(input("➣Enter pswrd : "))
aclass()
msg4 = str(input("➣Enter post link : "))
print("\033[1;37;96m", end = "")
print(47 * '\033[1;37;1m-')
np1 = str(input("➣Enter Hetter Name : "))
print("\033[1;37;96m", end = "")
print(47 * '\033[1;37;1m-')
msg5 = str(input("➣Enter notepad link : "))
print("\033[1;37;96m", end="")
print(47 * '\033[1;37;1m-')
f = open(msg5, 'r')
lines = f.readlines()
f.close()
msg6 = int(input("➣Enter TIME : "))
os.system('clear')
sys.stdout.flush()

print("\033[1;33;96m", end = "")
print('RajveeR Baap HeRe v1.0')
print("\033[91;1m")
print()
count = 0

while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(msg6)

            while not is_network_available():
                print("Waiting for network connection to be restored...")
                sleep(10)

            openlink(msg4)
            poct(np1+line)
            print("\033[1;33;96m", end = "")
            print("--> Rajveer Own FiiRe :v ::-->> ", np1, line, "\n")
            print("\033[0;32m")
            count += 1
            if count % 10 == 0:
                sleep(1)