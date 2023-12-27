import random
from pushbullet import Pushbullet

class Message:
    def __init__(self):
        API_KEY = "o.stOyUvr8fJwufgmx6dG4znkKib1YLCkY"
        self.pb = Pushbullet(API_KEY)

    def otp(self, name, number, purpose):
        self.otp_no = random.randint(10000, 100000)
        message = f"""
Dear {name},

Your One-Time Password (OTP) for {purpose.title()} is: {self.otp_no}
"""
        self.pb.push_sms(device=self.pb.devices[0], number=number, message=message)
        return str(self.otp_no)

    def police(self, date, time, place, details):
        message = f"""
Subject: Formal Complaint Regarding Vehicle Loss

Dear Police,
        
            I am writing to formally lodge a complaint regarding the loss of my vehicle, which is insured under your company. I have provided the necessary details below:
        
Vehicle Brand: {details[0]}
Vehicle Model: {details[1]}
Vehicle Year: {details[3]}
Registration Number: {details[4]}
Vehicle Color: {details[2]}
Lost Date: {date}
Lost Place: {place}
Lost Time: {time}
On {date}, my {details[0]} {details[1]}, with registration number {details[4]}, was unfortunately stolen from {place} during the following time period: {time}.
        
            I have already reported the incident to the local law enforcement authorities, and a copy of the police report is enclosed with this letter. I understand the importance of cooperation during the investigation process and am willing to provide any additional information or documentation required to expedite the resolution of this matter.
            I kindly request that you initiate the necessary procedures to process my claim and conduct a thorough investigation into the circumstances surrounding the loss of my vehicle. I expect your prompt attention to this matter and request regular updates on the progress of the investigation and the status of my claim.
            Please do not hesitate to contact me at [Your Phone Number] or [Your Email Address] if you require any further information or clarification. I appreciate your immediate attention to this matter and look forward to a swift resolution.
            Thank you for your understanding and cooperation.
            
Sincerely,
ADMIN
        """
        push = self.pb.push_sms(device=self.pb.devices[0], number="8248107803", message=message)


    def rent_successful(self, phone_no, message):
        push = self.pb.push_sms(device=self.pb.devices[0], number=phone_no, message=message)
message = Message()
message.otp(name="Saran", number="9092786919", purpose="")