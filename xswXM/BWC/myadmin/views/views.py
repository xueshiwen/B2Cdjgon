from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import Users,Types,Goods,Address,Orders,OrderInfo
from django.contrib.auth.hashers import make_password, check_password


def index(request):

	return render(request,'myadmin/index.html')



