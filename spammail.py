#!/usr/bin/python
#Dede Jomblo#

import os
import sys
import smtplib

B='\033[094m'
H='\033[093m'
G='\033[091m'
P='\033[0m'

os.system("clear")
print B+"\n#######################"
print G+"   #================#"
print G+"   # "+H+"[1] "+P+"SPAM GMAIL #"
print G+"   # "+H+"[2] "+P+"SPAM YAHOO #"
print G+"   #================#"
print B+ "########################"

server = raw_input(H+"     [No  Spam]: "+P+" ")
print H+"__________________________________________"
user = raw_input(H+"[UserMail Kamu]:"+P+" ")
Pass = raw_input(H+"[PassMail Kamu]:"+P+" ")
print H+"__________________________________________"

untuk = raw_input(H+"[Email Target]:"+P+" ")
body = raw_input(H+"[Tulis  Pesan]:"+P+" ")
total = input(H+"[Jumlah Pesan]:"+P+" ")
print H+"__________________________________________"

if server == '1':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == '2':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print P+"Pilih No "+H+"[1]\nGmail "+P+"\nAtau "+G+"\n[2]Yahoo"
    time.sleep(2)
    sys.exit()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,Pass)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'from: ' + user + '\nsubject: ' + subject + '\n' + body
        server.sendmail(user,untuk,msg)
        print "\r[Email Success Terkirim]> %i" % i
        sys.stdout.flush()
    server.quit()
    print G+"\n[+] "+P+"BERHASIL !!!"
except KeyboardInterrupt:
    print G+"\n[-] "+P+"GAAAGAAL"
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print "\n[!] Masukkan Yang Benar!!!"
    sys.exit()