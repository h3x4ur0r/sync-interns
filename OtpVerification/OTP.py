import os
from dotenv import load_dotenv
import random
import smtplib
from hashlib import sha256 as sha

load_dotenv()

def encode(OTP):
    return sha(bytes(OTP, encoding="utf-8")).hexdigest()

otp = "".join([str(random.randint(0, 9)) for _ in range(6)])

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("pratham2462@gmail.com", os.getenv("MAIL_PASS"))

emailId = input("Enter your email : ")

msg = f"From: pratham2462@gmail.com\r\nTo: {emailId}\r\n\r\n"
msg += "Your code is : " + str(otp)

s.sendmail("pratham2462@gmail.com", emailId, msg)

otp = encode(otp)

otpToVerify = encode(input("Enter the OTP : "))

while otpToVerify != otp:
    print("Please check the OTP again!")
    otpToVerify = encode(input("Enter the OTP : "))
print("Verified!")
