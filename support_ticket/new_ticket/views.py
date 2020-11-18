from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request,'login.html')


def newticket(request):
	return render(request,'add_ticket.html')