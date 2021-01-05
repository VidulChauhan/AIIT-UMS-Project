def msg():
    from twilio.rest import Client
    from random import *
    sid='AC941df350e2684f45d0e175d4faf8e132'
    auth='c5a3cae2b44f3417b71750f66b3a0f39'
    cl=Client(sid,auth)
    r=randrange(635745,952675)
    sms=cl.messages.create(
    from_='+17656256436',
    body='Hi "{}","{}" is the following code to reset your password.DO NOT share this with anyone'.format(name,r),
    to="{}".format(phn),
    )
    return sms.sid
    print("message sent successfully.")
    
     BJFBS FOISDH
