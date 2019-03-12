from django.shortcuts import render
from authentication.forms import UserProfileForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def login(request):
	print"jjj"
	if request.POST:
		print request.POST
		username=request.POST['username']
		password=request.POST['password']
		
		if username is not None:  
			print "yes"
			user = authenticate(username=username, password=password)
			return HttpResponseRedirect('/')

		else:
			return HttpResponseBadRequest('Not authenticated')     



	return render(request,"login.html")


def signup(request):
	print"please signup here..."
	if request.method == "POST":
		print "yes"
		print request.POST,"asdasd"
		form=UserProfileForm(request.POST)
		if form.is_valid():
			print "valid..."
			new=form.save(commit=False)
			new.save()
		else:
			print form.errors


	return render(request,"signup.html")

