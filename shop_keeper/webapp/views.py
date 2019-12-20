from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from webapp.forms import SignUpForm
# Create your views here.
def home_page(request):
    return render(request,'myapps/home.html')

@login_required
def customer(request):
    return render(request,'myapps/customer.html')

def logout_view(request):
    return render(request,'myapps/logout.html')

from django.contrib.auth import login, authenticate



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/cust')
    else:
        form = SignUpForm()
    return render(request, 'myapps/registration.html', {'form': form})