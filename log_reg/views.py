from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login, logout, forms
# from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        form = UserForm(request.POST)
        value = {'first_name':first_name, 'last_name':last_name, 'username':username, 'email':email, 'password':password}
        username_database = User.objects.filter(username=username)
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        print("fffffffffffffffffffffffffffggg")
        if (first_name and last_name and username and email and password):
            if not username_database:
                new_user.set_password(password)
                new_user.save()
                return redirect('login')
            return render(request, 'register.html', context={'message':'found', 'value':value})
        return render(request, 'register.html', context={'message':"tuldir", 'value':value})
    return render(request, 'register.html')
    
def login_view(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password = request.POST['password']
        value = {'username':username1, 'password':password}
        login_form = forms.AuthenticationForm(request, data=request.POST)
        if (username1 and password):
            if login_form.is_valid():
                user =login_form.get_user()
                login(request, user)
                username_database = User.objects.get(username=username1)
                if username_database:
                    return redirect('index')
                return render(request, 'login.html', context={'message':'nfound', 'value':value})
            return render(request, 'login.html', context={'message':'nfound', 'value':value})
        return render(request, 'login.html', context={'message':'found_first', 'value':value})
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('index')

def account_view(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'account.html', context={'user':user})
    