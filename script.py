import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "youremail@gmail.com" # your email
password = "(app password)" # app password
subject = "(subject email)" 
body = "(body message)"

with open('email.txt', 'r') as file:
    recipient = [line.strip() for line in file.readlines()] # adjust formatting of email.txt here

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print("Login successful")
except smtplib.SMTPAuthenticationError:
    print("Failed to login")
    server.quit()
    exit()

for recipient_email in recipient:
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    try:
        server.sendmail(sender, recipient_email, message.as_string())
        print(f"Success! send to {recipient_email}")
    except Exception as e:
        print(f"Failed! {recipient_email}: {str(e)}")

server.quit()
