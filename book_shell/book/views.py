from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users,Product
from django import forms

# Create your views here.
# here html files are rendered.
# this page is for the request handler.

def say_hello(request):
    # return HttpResponse("hello shyam")
    return render(request, 'form.html',)

# def user(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         insert = Users()
#         insert.name = "shyam"
#         insert.email = "shaym100@gmail.com"
#         insert.save()

def user(request):
    # if request.method == 'POST':
    # form_data = request.POST
    insert = Users()
    insert.name = "shyam"
    insert.email = "shaym100@gmail.com"
    insert.save()


# class create_form(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['name', 'email','password','confPassword']

# def create_new_account(request):
#     if request.method == 'POST':
#         form = create_form(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to success page after saving the data
#             return redirect('index.html')  
#     else:
#         form = create_form()
#     return render(request, 'create_new_user.html', {'form': form})




# def users_login(request):
#     users = Users.objects.all()
#     return render(request, 'login.html',{'users':users})

# def login(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         password = request.POST['password']
        
#         bk_user = Users(name=name, password=password)
#         bk_user.save()
        
#         return render(request, 'success.html')
    
#     return render(request, 'create_person.html')