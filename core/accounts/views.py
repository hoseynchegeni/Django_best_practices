from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from .tasks import sendEmail
def send_email(request):
    sendEmail.delay()
    return HttpResponse('Done Sending')