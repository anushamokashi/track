from django.shortcuts import render

# Create your views here.

def base(request):
	print"kkk"

	return render(request, "firstpage.html")