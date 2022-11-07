from django.http import HttpResponse
from django.shortcuts import render
from . import views

def home(request):
    # name = input('Enter your name')
    # roll = input("Enter your roll no")
    # data = {
    #     'n': name,
    #     'r': roll
    # }
    try:
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        operator = request.GET.get('operator')
        result = {'ans':None}
        if operator == 'add':
            result['ans'] = num1 + num2
        elif operator == 'sub':
            result['ans'] = num1 - num2
        elif operator == 'mul':
            result['ans'] = num1 * num2
        else:
            result['ans'] = num1 // num2
        return render(request, 'home.html', result)
    except:
        return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

