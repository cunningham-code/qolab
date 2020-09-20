from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from .models import Timer
import json
import random
import string


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")


def timer(request, code="000000"):
    # t = Timer.objects.get(code=code)
    # return render(request, 'timer.html', {'code': code, 'timer': t})
    return render(request, 'timer.html', {'code': code})


def form(request):
    return render(request, 'form.html')
    # return HttpResponse("Hello World")


def email(request):
    def get_random_string(length):
        numbers = string.digits
        result_str = ''.join(random.choice(numbers) for i in range(length))
        return result_str

    firstName = request.POST.get('firstName', '')
    start = request.POST.get('start', '')
    end = request.POST.get('end', '')
    date = request.POST.get('date', '')
    ytLink = request.POST.get('youTubeLink', '')
    friends = json.loads(request.POST.get('friends', ''))  # This is not used
    emails = json.loads(request.POST.get('emails', ''))
    # make random number with 6 characters. Characters must be digits 0-9.
    code = get_random_string(6)

    subject = "You have a new QoLab with " + firstName + "!"
    message = firstName + " has invited you to a collab. You code is " + code + \
        ". It starts at " + start + " and ends at " + end + " on " + date + "."
    message = message + "\n\nDon't miss out on studying with friends."

    from_email = "qolabstudying@gmail.com"

    if subject and message and from_email:
        try:
            html_content = '<p>' + message + '</p>'
            msg = EmailMultiAlternatives(subject, message, from_email, emails)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # send_mail(subject, message, from_email, [])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('frick yes.')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


"""
def RGList(request):
    return render(request, 'rg_list.html')


def RGCreate(request):
    return render(request, 'rg_create.html')


def PolicyList(request):
    return render(request, 'policy_list.html')


def RemediationList(request):
    return render(request, 'remediation_list.html')
"""
