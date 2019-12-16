# Text Intruder Alarm System
A Raspberry Pi 3 Model B+ will be used to create an intruder alarm that sends a text message warning to the owner of a smartphone device with text messaging (SMS) capabilities. If you ever have trouble with a friend or relative checking your phone when you are not around, this will be helpful to know whether they can be trusted. This project can be done by anyone of any skill level if you are interested in trying it out.  

References 
- https://www.hackster.io/gatoninja236/raspberry-pi-texting-intruder-alarm-d0d2a8

# Hardware Components
- CanaKit Raspberry Pi 3 Model B+ 
- PIR Motion Sensor 
- Jumper Wires

# Software Components
- Thony Python (on Raspberry Pi)
- Microsoft Visual Studio Code (Python 3.7.4)

# Carrier/Phones Used
- T-Mobile: number@tmomail.net
- Virgin Mobile: number@vmobl.com 
- Sprint: number@messaging.sprintpcs.com 

# Code Descriptions
```python
import time
import smtplib
import RPi.GPIO as GPIO
```
**Carrier and Email Address:** 
- `TO` : add phone number @ email address based on the carrier used
- `GMAIL_USER` : add gmail account 
- `PASS` : your account password

**Text Message Content:**
- `SUBJECT` : add text message subject line
- `TEXT` : add text message that will alert the intruder

**GPIO Setup**
- `GPIO.setmode(GPIO.BCM)`: refers to the pins Broadcam SOC channel
- `GPIO.setup(4,GPIO.IN)` : identifies pin numbering

**Send Mail Function**
- `def send_mail()` : takes no parameters
- Within the `def` function: 
  - `print("Sending text")`
  - `server = smtplib.SMTP` : Will access a mail transfer protocol to then login into the account
  - `header` : Used to format the messages
  - `msg` : Adds additional formating to the header
  - `time.sleep()` : Takes 1 argument that refers to the time of when the message is sent

**Motion Sensor Function**
- `while True` : Acts as the basis for the PIR sensor
  - `if GPIO.input(4) == 1` : A message will be sent when the PIR sensor detects somemthing and will go to sleep for 2 minutes afterwards 
  - `else` : PIR sensor will check every 5 seconds to detect if something is near it 
  



