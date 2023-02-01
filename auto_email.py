'''import smtplib, ssl
from email.message import EmailMessage

import body as body

port = 465  # For SSL
smtp_server = "smtp.gmail.com"




sender_email = "adutinyhouse@gmail.com"  # Enter your address
receiver_email = ""  # Enter receiver address
password = ""

msg: EmailMessage = EmailMessage()
msg.add_alternative ("""
                    We are sorry to inform you that Sierra Tiny Homes has gone out of business. We understand that
                    this may disappointing news and we want to help you find the tiny home of your dreams.
                    We have access to a variety of tiny homes in different styles, sizes, and price ranges. Let us
                    know a bit more
                    about what you’re looking for and we’ll be able to help you find the perfect tiny home.

                    How much do you want to spend? Do you need a loan? What size of tiny home do you want?

                    We look forward to hearing from you and helping you find the perfect tiny home.

                                                                               Thanks, Woody """)


msg['Subject'] = "Sierra Tiny Homes"
msg['From'] = sender_email
msg['To'] = receiver_email

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
'''

import smtplib, ssl
from email.message import EmailMessage
import logging

import body as body

port = 465  # For SSL
smtp_server = "smtp.gmail.com"




sender_email = "adutinyhouse@gmail.com"  # Enter your address
#receiver_email = ""  # Enter receiver address
password = "jrsdrsdnnskgeogv"

#open the testing.txt file
with open('email_sending.txt', 'r') as file:
    #read the file and extract the email addresses
    addresses = file.read().splitlines()

#loop through the list of addresses
for address in addresses:

    try:
        # create and configure the email message
        msg: EmailMessage = EmailMessage()
        msg.add_alternative("""
         We are sorry to inform you that Sierra Tiny Homes has gone out of business. We understand that this may be
         disappointing news and we want to help you find the tiny home of your dreams.

         We have access to a variety of tiny homes in different styles, sizes, and price ranges. Let us know a bit more
         about what you’re looking for and we’ll be able to help you find the perfect tiny home.

         How much do you want to spend? Do you need a loan? What size of tiny home do you want?

         We look forward to hearing from you and helping you find the perfect tiny home.

Thanks,
Woody""")

        msg['Subject'] = "Sierra Tiny Homes"
        msg['From'] = sender_email
        msg['To'] = address

        # send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email, to_addrs=address)

    except Exception as e:
        # log the exception
        logging.exception(e)

    #msg['Subject'] = "Sierra Tiny Homes"
    #msg['From'] = sender_email
    #msg['To'] = address

    #send the email
    #context = ssl.create_default_context()
    #with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #server.login(sender_email, password)
        #server.send_message(msg, from_addr=sender_email, to_addrs=address)
