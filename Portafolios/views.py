from django.http import *
from django.shortcuts import render


#Vista principal o home
def main(request):
    return render(request, "main.html", {})