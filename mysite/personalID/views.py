from django.shortcuts import render
from django.http import HttpResponse
from foedselsnummer import generateFNr

def index(request):
    fnr = generateFNr(None, None, None)
    return HttpResponse(f"Generated Norwegian national ID: {fnr}")