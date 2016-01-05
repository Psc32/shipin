from django.shortcuts import render
import datetime


def main(request):
    context = {'message':'Django very good', }
    return render(request, 'main/main.html', context)
