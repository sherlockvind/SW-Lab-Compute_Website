from django.shortcuts import render, redirect
from django.http import HttpResponse
import hashlib

from .models import UserData
# Create your views here.

def index(request):
	if request.method == "POST":
		upload(request)
		return render(request, "main/index.html", {"registration_status": 1})
	else:
		return render(request, "main/index.html", {"registration_status": 0})
	
def upload(request):
	sha = hashlib.sha1(request.POST['password'].encode("utf-8"))
	
	user_name = request.POST['name']
	password =  sha.hexdigest() #Hash the password before storage
	id_proof_file = request.FILES['id_proof']
		
	user_form = UserData(user_name=user_name, password=password, id_proof_file=id_proof_file)
	user_form.save()
