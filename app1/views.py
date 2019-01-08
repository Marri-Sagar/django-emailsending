from django.shortcuts import render,HttpResponse
from django.core.mail import EmailMessage,send_mail
import random
def sendmail(request):
    otp = random.randint(10000, 50000)
    mess="your otp is{}".format(otp)
    email=send_mail(subject="resume",from_email='sagarmarri21@gmail.com',recipient_list=['rayalajeevan@gmail.com'],message=mess)
    return HttpResponse("success")
