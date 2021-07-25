from django.shortcuts import render
from .models import *

# Create your views here.

def users(request):
  Users = User_Model.objects.all()
  return render(request,'users.html',{'users':Users})