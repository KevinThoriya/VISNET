import requests
import json
import random

# get request
def sendOTP( phoneNo, textMessage):
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'    
    apiKey = '10QBA0HQI73OLZHH0R0ZPJM0YKL742S1'
    secretKey='G7M8MCMO1BP00JLL'
    useType='stage'
    senderId = 'VISNET'

    req_params = {
    'apikey':apiKey,
    'secret':secretKey,
    'usetype':useType,
    'phone': phoneNo,
    'message':textMessage,
    'senderid':senderId
    }
    return requests.post(URL, req_params)

# response = sendOTP('8160238779','SOME STUFF' )
# print(response.text['status'])
def make_message():
    length = 6
    number = 0
    for i in range(length):
        number *=10
        number += random.randrange( 1, 10, 1 )
    return number

# 'your VisNet verification code is {number}. welcome to Parul University.'

def OTP(phoneNO, number):
    message = f'Your VISNET Verification Code is {number}. Welcome to Parul University.'
    response = sendOTP(phoneNO, message )
    print(response.text)

