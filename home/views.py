from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from .models import User
# Create your views here.
def home(request , *args , **kwargs):
    return render(request , "signup.html")

def register(request , *args , **kwargs):

    if(request.method =='POST'):
        
        form = request.POST
        register_form = SignUpForm(request.POST)
        username = form['username']
        email = form['email']
        cfhandle = form['cfhandle']
        password1 = form['password1']
        password2 = form['password2']
        #email = register_form.cleaned_data['email']
        print(email)
        if register_form.is_valid() and register_form.cleaned_data['password1'] == register_form.cleaned_data['password2']:
            # Verification is done and form is valid .
            print(register_form.cleaned_data)
            try:
                check = User.objects.get(username = register_form.cleaned_data['username'])
                return HttpResponse("<h1>User Already Exists Please try a new Username</h1>")
            except User.DoesNotExist:

                User.objects.create(username = register_form.cleaned_data['username'] ,
                                    email =register_form.cleaned_data['email'],
                                    cfhandle = register_form.cleaned_data['cfhandle'],
                                    password = register_form.cleaned_data['password1'])
                
            return render(request , "signup.html")
        else :
            return HttpResponse("<h1>You did some mistake</h1>")
            
    else :
        print("something was not right")
        return render(request , "signup.html")



def login(request , *args , **kwargs):
    pass


def logout(request , *args , **kwargs):
    pass

def genrateProblemSet(request , *args , **kwargs):
    pass

def fetchStats(request , *args , **kwargs):
    pass

def udpateUser(request , *args , **kwargs):
    pass

def sendApology(messgase ,errcode):
    pass



# login 

# generate_problem_set 

# 