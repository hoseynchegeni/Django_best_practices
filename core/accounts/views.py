from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from time import sleep
from .tasks import sendEmail
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page

def send_email(request):
    sendEmail.delay()
    return HttpResponse('Done Sending')

def oldTest(request):
    if cache.get('test_delay_api') is None:
        response = requests.get("https://7dcac153-28fd-414a-899c-f80958d9649c.mock.pstmn.io/test/delay/5")
        cache.set('test_delay_api', response.json())
    return JsonResponse(cache.get('test_delay_api'))

@cache_page(60)
def test(request):
    response = requests.get("https://7dcac153-28fd-414a-899c-f80958d9649c.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())