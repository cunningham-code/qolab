from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")


def form(request):
    return render(request, 'form.html')
    # return HttpResponse("Hello World")


def email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    # request.POST.get('from_email', '')
    from_email = "qolabstudying@gmail.com"
    # subject = "Test"
    # message = "test"
    # from_email = "qolabstudying@gmail.com"
    if subject and message and from_email:
        try:
            html_content = '<p>' + message + '</p>'
            msg = EmailMultiAlternatives(subject, message, from_email, [
                                         'cunningjc10@gmail.com'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # send_mail(subject, message, from_email, [])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('fuck yes.')
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
