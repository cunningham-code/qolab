from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

import os


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")


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
