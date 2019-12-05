import time
import smtplib
import RPi.GPIO as GPIO

TO= "6788875894@tmomail.com" #all of the credentials
GMAIL_USER="textintruderalarm@gmail.com"
PASS= 'raspberrypi3'

SUBJECT = 'Alert!'
TEXT = 'Your Raspberry Pi detected an intruder!'

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN)

def send_mail(): #the texting portion
    print ("Sending text")
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(GMAIL_USER,PASS)
    except Exception as e:
        print("Mail server problem. ",e)
    
    header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
    print (header)
    msg = header + '\n' + TEXT + '\n\n'
    try:
        server.sendmail(GMAIL_USER,TO,msg)
        server.quit()
        print ("Text sent")
    except Exception as ex:
        print("Send mail problem. ",ex)
        
    time.sleep(1)

while True:
    if GPIO.input(13): 
        print ("trigger if sensor has detected something")
        send_mail()
        time.sleep(60*2) #Sleep for 2 minutes
    else:
        print ("waiting for 5 seconds")
        time.sleep(5) #check every 5 seconds
