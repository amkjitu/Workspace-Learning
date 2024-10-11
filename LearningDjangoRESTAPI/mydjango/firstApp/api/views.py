from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render

def homeView(request):
    return render(request,'index.html')

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def firstAPI(request):
    if request.method=='POST':
        name = request.data['name']
        age = request.data['age']
        print(name,age)        
        return Response({"name":name,"age":age})
    context={
        'name':"Jitu Khan",
        'university':"PSTU-CSE"
    }
    return Response(context)

from django.contrib.auth.models import User
@api_view(['POST',])
@permission_classes([AllowAny])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username is already exists"})
        if password1 != password2:
            return Response({"error":"Passwords did not match"})
        
        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(raw_password=password1)
        user.save()
        return Response({"Success":"User successfully registered!"})