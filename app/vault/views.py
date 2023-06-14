from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from vault.models import User, Password
from django.views.decorators.csrf import csrf_exempt
from vault.serializers import UserSerializer, PasswordSerializer

# Create your views here.

# GET list of all users
@csrf_exempt
def user_all(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#GET and DELETE unique users  
@csrf_exempt
def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
    
#get all passwords by unique user
@csrf_exempt
def passwords_one_user(request):
    user = request.GET.get('user')
    url = request.GET.get('url')
    password = Password.objects.filter(user=user).filter(url=url)
    try:
        passwords = Password.objects.filter(user=user)
    except Password.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=="GET" and url==None:
        serializer = PasswordSerializer(passwords, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = PasswordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method=="GET":
        serializer = PasswordSerializer(password, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='PUT':
        new_password = Password.objects.filter(user=user).filter(url=url).first()
        data = JSONParser().parse(request)
        new_password.delete()
        serializer = PasswordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        password.delete()
        return HttpResponse(status=204)