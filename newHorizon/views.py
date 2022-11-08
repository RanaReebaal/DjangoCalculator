from django.http import HttpResponse
from django.shortcuts import render
from . import views
from latestTech . models import information
import json

def home(request):
    d = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(name) < 3:
            er = 'Your name is not in our data, Enter your valid name...'
            return render(request, 'home.html', {'m': er})
        data = information(name=name, father_name=father_name,
                           gender=gender, email=email, password=password)
        data.save()
        d = '👻Bro Your Data has Been Sent You Can Go And Check Please 🙏🏼 Thank You'
    return render(request, 'home.html', {'d': d})


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

# def members(request):
#     return render(request, 'members.html')



def members(request):
    name = request.GET.get('u_name')
    age = request.GET.get('u_age')
    city = request.GET.get('u_city')
    job = request.GET.get('u_job')
        
    class model():
        def __init__(self, member, age, city, job):
            self.member = member
            self.age = age
            self.city = city
            self.job = job
        def member_name(self):
            return self.member
        def member_age(self):
            return self.age
        def member_city(self):
            return self.city
        def member_job(self):
            return self.job

    user = model(name, age, city, job)
    
    output = {
        'user_name' : user.member,
        'user_age' : user.age,
        'user_city' : user.city,
        'user_job' : user.job
    }
    with open('UserData.json', 'a') as d:
        json.dump(output, d, indent = 4)

    return render(request, 'members.html', output)


