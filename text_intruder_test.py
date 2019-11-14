import time
import smtplib
import RPi.GPIO as GPIO

TO= "6788875894@tmomail.com" #all of the credentials
GMAIL_USER="CDF3.py@gmail.com"
PASS= 'thecoolestpeople123'

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
    if GPIO.input(4)==1: 
        print ("trigger if sensor has detected something")
        send_mail()
        time.sleep(60*2) #Sleep for 2 minutes
    else:
        print ("waiting for 5 seconds)
        time.sleep(5) #check every 5 seconds
