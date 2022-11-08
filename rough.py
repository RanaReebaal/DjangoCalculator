

# def home(request):
#     d = ''
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         father_name = request.POST.get('father_name')
#         gender = request.POST.get('gender')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#     def valid(n):
#         if len(n) < 3:
#             er = 'Your name is not in our data, Enter your valid name...'
#             print(er)
#         else:
#             data = information(name=name, father_name=father_name, gender=gender, email=email, password=password)
#             data.save()
#             d = '👻Bro Your Data has Been Sent You Can Go And Check Please 🙏🏼 Thank You'
#             return render(request, 'home.html', {'d': d})

#     valid(name)


# class model():
#     def __init__(self, member, age, city, job):
#         self.member = member
#         self.age = age
#         self.city = city
#         self.job = job
#     def member_name():
#         return self.member
#     def member_age():
#         return self.age
#     def member_city():
#         return self.city
#     def member_job():
#         return self.job


# user1 = model('safdar', 45, 'Lahore', 'carpenter')
# user2 = model('nazim', 45, 'Lahore', 'carpenter')
# user3 = model('rashid', 45, 'Lahore', 'carpenter')
# user4 = model('asghar', 45, 'Lahore', 'carpenter')

# print(user1.member)
# print(user1.age)
# print(user1.city)
# print(user1.job)


# class model():
#     def __init__(self, member, age, city, job):
#         self.member = member
#         self.age = age
#         self.city = city
#         self.job = job
#     def member_name(self):
#         return self.member
#     def member_age(self):
#         return self.age
#     def member_city(self):
#         return self.city
#     def member_job(self):
#         if self.job == 'Engr':
#             print(f'{self.job}You are not allowed')
#         else:
#             return self.job


# user1 = model('safdar', 45, 'Lahore', 'Carpenter')


# print(user1.member)
# print(user1.age)
# print(user1.city)
# print(user1.job)

# user1.member_job()

import json

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

user = model('rana adeema', 74, 'Taxila', 'Philospher')

output = {
        'user_name': user.member,
        'user_age': user.age,
        'user_city': user.city,
        'user_job': user.job
}

with open('UserData.py', 'a') as d:
    d.write( f"""\n"This is data of '{user.member}'"                
'Name: {user.member}'
'Age:  {user.age}'
'City: {user.city}'
'Job:  {user.job}' 
"""
)
    
