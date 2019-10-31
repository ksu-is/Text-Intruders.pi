# Text Intruder Alarm System
A Raspberry Pi 3 Model B will be used to create an intruder alarm that sends a text message warning to the owner of a smartphone device with text messaging (SMS) capabilities. The language used to run the program is Python 3.7.4 at the time this project was developed. In order for the intruder alarm to work, a passive infrared (PIR) sensor is required to sense intruders presence at a certain distance. 

References 
- https://www.hackster.io/gatoninja236/raspberry-pi-texting-intruder-alarm-d0d2a8

# Hardware Components
- Raspberry Pi 3 Model B
- PIR Sensor 
- Jumper Wires

# Software Components
- Python (3.7.4) IDLE
- Visual Studio Code 

# Carrier/Phones Used
- T-Mobile: number@tmomail.net
- Virgin Mobile: number@vmobl.com 
- Sprint: number@messaging.sprintpcs.com 

# Instructions
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
- `TEXT` : add text message to alert of intruder

**GPIO Setup**
- `GPIO.setmode(GPIO.BCM)`: this refers to the pins Broadcam SOC channel
- `GPIO.setup(4,GPIO.IN)` : identifying pin numbering

**Send Mail Function**
- `def send_mail()` : takes no parameters
- Within the `def` function: `print("Sending text")`
- `server = smtplib.SMTP` : refers to the Mail Transfer Protocol

