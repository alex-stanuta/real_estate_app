from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
	if request.method == 'POST':
		messages.error(request, 'Testing error messages')
		#Register user
		return redirect('login')
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	return redirect('index')

def register(request):
	if request.method == 'POST':
		messages.error(request, 'Testing error messages')
		return redirect('register')
	else:
		return render(request, 'accounts/register.html')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')