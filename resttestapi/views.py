from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from resttestapi.models import Employee,EmployeeForm
from .serilizars import EmployeeSerializers

# Create your views here.

@api_view(['GET','POST'])
def Employee_list(request):
     if request.method == 'GET':
          obj = Employee.objects.all()
          serilizars = EmployeeSerializers(obj,many=True)
          return Response(serilizars.data)
     elif request.method == 'POST':
          serilizars = EmployeeSerializers(data=request.data)
          if serilizars.is_valid():
               serilizars.save()
               return Response(serilizars.data,status=status.HTTP_201_CREATED)
          return Response(serilizars.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def employeedetails(request,pk):
     try:
          obj = Employee.objects.get(id=pk)
     except Employee.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
          serilizars = EmployeeSerializers(obj)
          return Response(serilizars.data)
     elif request.method == 'PUT':
          serilizars = EmployeeSerializers(obj,data=request.data)
          if serilizars.is_valid():
               serilizars.save()
               return Response(serilizars.data)
          return Response(serilizars.errors,status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
          obj.delete()
          return Response(status=status.HTTP_202_ACCEPTED)
          # return Response(serilizars.errors, status=status.HTTP_400_BAD_REQUEST)


class Employeeview(APIView):
     def get(self,request):
          obj = Employee.objects.all()
          serilizars = EmployeeSerializers(obj, many=True)
          return Response(serilizars.data)
     def post(self,request):
          serilizars = EmployeeSerializers(data=request.data)
          if serilizars.is_valid():
               serilizars.save()
               return Response(serilizars.data, status=status.HTTP_201_CREATED)
          return Response(serilizars.errors, status=status.HTTP_400_BAD_REQUEST)

class employeedetail(APIView):
     def get_object(self,id):
          try:
               return Employee.objects.get(id=id)
          except Employee.DoesNotExist:
               return Response(status=status.HTTP_404_NOT_FOUND)
     def get(self,request):
          obj = Employee.objects.all()
          serilizars = EmployeeSerializers(obj, many=True)
          return Response(serilizars.data)
     def post(self,request):
          serilizars = EmployeeSerializers(data=request.data)
          if serilizars.is_valid():
               serilizars.save()
               return Response(serilizars.data, status=status.HTTP_201_CREATED)
          return Response(serilizars.errors, status=status.HTTP_400_BAD_REQUEST)
     def put(self,request,id=None):
          obj = self.get_object(id)
          serilizars = EmployeeSerializers(obj, data=request.data)
          if serilizars.is_valid():
               serilizars.save()
               return Response(serilizars.data)
          return Response(serilizars.errors, status=status.HTTP_400_BAD_REQUEST)
     def delete(self,request,id=None):
          obj = self.get_object(id)
          obj.delete()
          return Response(status=status.HTTP_202_ACCEPTED)






# def login_register_check(url):
#      if User.is_authenticated:
#           print('login')


# @login_register_check(url = "userlogin")
def index(request):
     form = EmployeeForm()
     return render(request,"loginuser.html",{'form':form})
     # return HttpResponse("hellow")

def loginss(request):
     if request.method == "GET":
          return render(request,'loginuser.html',{})
     elif request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          print(f"{username}, {password}")
          user = authenticate(username=username,password=password)
          try:
               if user is not None:
                    login(request,user)
                    return HttpResponse('login successfully<a href="loguots">logout</a>')
          except:
               return HttpResponse('login error unseccessfully')
     return HttpResponse('login unseccessfully')

def loguots(request):
     logout(request)
     return HttpResponse("logout successfully")

def saveemp(request):
     form = EmployeeForm()
     if request.method == 'POST':
          form = EmployeeForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponse('sava data')
     
     return render(request,"loginuser.html",{'form':form})