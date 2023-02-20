from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from time import sleep
from .tasks import sendEmail
import requests
def send_email(request):
    sendEmail.delay()
    return HttpResponse('Done Sending')

def test(request):
    response = requests.get("https://7dcac153-28fd-414a-899c-f80958d9649c.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())