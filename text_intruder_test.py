import time
import smtplib
import RPi.GPIO as GPIO

TO= "your phone # as a carrier email address: 'phone#@txt.att.net' for \ example" #all of the credentials
GMAIL_USER="your GMAIL account email address"
PASS= 'your account password'

SUBJECT = 'Alert!'
TEXT = 'Your Raspberry Pi detected an intruder!'

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

def send_mail(): #the texting portion
    print ("Sending text")
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(GMAIL_USER,PASS)
    header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
    print (header)
    msg = header + '\n' + TEXT + '\n\n'
    server.sendmail(GMAIL_USER,TO,msg)
    server.quit()
    time.sleep(1)
    print ("Text sent")

while True:
    if GPIO.input(4)==1: #trigger if sensor has detected something
        send_mail()
        time.sleep(60*2) #Sleep for 2 minutes
    else:
        time.sleep(5) #check every 5 seconds
