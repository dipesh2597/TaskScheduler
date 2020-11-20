from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from .forms import RegisterForm,LoginForm
from django.contrib.auth.hashers import make_password
from .models import Profile, Task
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self,request):
        form = RegisterForm()
        return Response({'form': form},status=HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        name = request.POST.get('name').split(" ")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print(latitude,longitude)
        # using " ".join() in case user's name contains more than 2 words
        # User.objects.get_or_create(first_name=name[0],last_name=" ".join(name[1:]),email=email,username=username,password=make_password(password))

        # Profile.objects.create(user=User.objects.get(username=username),mobile=mobile,address=address,latitude=latitude,longitude=longitude)
        # try:
        #     user = authenticate(username=User.objects.get(username=username ),password=password)
        # except Exception as e:
        #     print(e)
        # login(request, user)
        return HttpResponseRedirect(redirect_to='/task/')

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self,request):
        form = LoginForm()
        return Response({'form': form},status=HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(username=User.objects.get(email=email),password=password)
        except:
            return Response({"message": "invalid"},status=HTTP_400_BAD_REQUEST)
        login(request, user)
        return HttpResponseRedirect(redirect_to='/task/')

        # return Response({'message': 'success'},status=HTTP_200_OK)


class TaskView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task.html'

    def get(self,request):

        #filtering all task assigned to logged in user
        queryset = Task.objects.filter(assigned_to=request.user)
        users = User.objects.all()
        return Response({'tasks': queryset,'users':users},status=HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        name = request.POST.get('name')
        assigned_to = User.objects.get(id=request.POST.get('assigned_to')) 
        date_time = datetime.strptime( f"{request.POST.get('date')} {request.POST.get('time')}", '%Y-%m-%d %H:%M')
        Task.objects.create(task_name=name,assigned_to=assigned_to,assigned_by=request.user,date_time=date_time)
        return HttpResponseRedirect(redirect_to='/task/')
        
        # return Response({'message': 'success'},status=HTTP_200_OK)