from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import SignUpForm , SignInForm , UpdateUserForm , UpdateUserPasswordForm
from .models import User
# Create your views here.
#@login_required
def home(request , *args , **kwargs):

    #If the user is already logged in then Load DashBoard .
    if request.session.get('username') is None:
        # Redirect to Login page .
        return render(request, "login.html")
    return render(request , "dashboard.html" , {'username':request.session['username']})
def register(request , *args , **kwargs):

    if request.session.get('username') is not None:
        return redirect(home)
    if(request.method =='POST'):
        
        form = request.POST
        register_form = SignUpForm(request.POST)
        username = form['username']
        email = form['email']
        cfhandle = form['cfhandle']
        password1 = form['password1']
        password2 = form['password2']
        #email = register_form.cleaned_data['email']
        if register_form.is_valid() and register_form.cleaned_data['password1'] == register_form.cleaned_data['password2']:
            # Verification is done and form is valid .
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
    
    if request.session.get('username') is not None:
        return redirect(home)
    if request.method == 'POST':
        
        form = SignInForm(request.POST)

        if form.is_valid():
            print("form vaild hai")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                userInfo = User.objects.get(username = username)
                if(userInfo.password==password):
                    request.session['username'] = username
                    return redirect(home)
                else:
                    print(userInfo.password)
                    return HttpResponse("<h1>Username or Password is incorrect</h1>")
            except User.DoesNotExist:
                return HttpResponse("user does not exist")

        else:
            print(form.cleaned_data)
            return HttpResponse("<h1>You did some mistake .</h1>")
    else:
        HttpResponse("<h1>Something Went Wrong Please Try again.</h1>")

def loginRequired():
    pass


def logout(request , *args , **kwargs):
    
    try :
        del request.session['username']
        print("You are Logged Out .")
    except:
        print("There was Some Problem in Logging you out .")
        return redirect(home)
    return redirect(home)

def genrateProblemSet(request , *args , **kwargs):
    pass

def fetchStats(request , *args , **kwargs):
    pass

def updatePassword(request , *args , **kwargs):
    
    if request.method == 'POST':
        form = UpdateUserPasswordForm(request.POST)

        if form.is_valid():
            print("Form was valid .")
            try:
                user = User.objects.get(username = form.cleaned_data['username'] ,)
            except User.DoesNotExist:
                print("hello")
        else:
            return HttpResponse("something went wrong")

def updateDetails(request , *args , **kwargs):
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)

        if form.is_valid():
            print("Form is valid.")
            try:
                user = User.objects.get(email = form.cleaned_data['email'])
                return HttpResponse("The email you are using is already registerd .")
            except User.DoesNotExist:
                User.objects.get(username = request['username'].update(email = form.cleaned_data['email']))
                return HttpResponse("Credentials has been updated")
        else:
            return HttpResponse("Your inputs are not correct")
    else:
        return HttpResponse("something went wrong")
                

def fillProblemSet():
    pass
    # To fill the problem using API .
    # To generate the link use Problem Code where Problem code is concatenation of ContestId + Problem Name or Index .
def sendApology(messgase ,errcode):
    pass



# login 

# generate_problem_set 

# 