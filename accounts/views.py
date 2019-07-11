from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['password2']:
			try:
				User.objects.get(username = request.POST['username'])
				return render(request, 'signup.html',{'error':'Username exist..'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
				auth.login(request,user)
				return redirect('home')


	else:
		return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		f = auth.authenticate(username=request.POST['username'],password=request.POST['password'])

		if f is not None:
			auth.login(request,f)
			return redirect('home')
		else:
			return render(request,'login.html',{'error':'Username Or Password is incorrent'})


	else:
		return render(request,'login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
    
