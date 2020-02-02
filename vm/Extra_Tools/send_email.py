# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
# libraries to be imported 

# python -m install --upgrade pip
# easy_install --upgrade setuptools
# pip install email
# easy_install email


import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def sendmail(id,send_to ):
    """
        for sending email wiht smtp server

        @params id of the visitor.
        @params takes sender's email address

    """
    fromaddr = "visnet.helper@gmail.com"
    toaddr = send_to
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    # storing the receivers email address  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = "Access Card - VISNET"
    # string to store the body of the mail 
    body = f"""
        Welcome to Parul University. This is your digitally generated access card. Your Permanent Visiting ID is {id}.
		
        This card will be helpful to enter this campus again.
		
        While exiting campus, scan the QRcode under the Scanner.
		
        Thank You. Have a nice day. Visit Again.
    """
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    # open the file to be sent  
    filename = f"access_{id}.png"
    attachment = open(f"media/ids/{id}.png", "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "ABCD@abcd123") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit() 