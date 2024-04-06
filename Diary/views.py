from django.shortcuts import render, redirect, get_object_or_404
from Diary.models import Diary
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required





# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated:
        diaries = Diary.objects.filter(owner = request.user)
    else:
        diaries = None
    return render(request, 'index.html', {'mydiaries' : diaries})


@login_required(login_url='/login/')
def new_diary(request):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body'):
            newdiarydata = Diary(title = request.POST['title'], body= request.POST['body'], owner= request.user)
            newdiarydata.save()
            messages.success(request, "New journal added to your diary!")
            return redirect('index')
        
        else:
            messages.error(request, "Fill in diary title and content.")
            return redirect('new_diary')

    return render(request, 'newdiary.html')


def register(request):

    if request.user.is_authenticated:
        return redirect('diary')
    
    
    if request.method == 'POST':
        uname= request.POST.get('username') 
        password =  request.POST.get('password')  
        cpassword = request.POST.get('cpassword')

        if (uname and password and cpassword) and (password == cpassword):
            if not get_user_model().objects.filter(username = uname).exists():
                get_user_model().objects.create(username=uname, password=password)
                messages.success(request, "Your account has been created sucessfully")
                return redirect('signin')
            else:
                messages.warning(request, "This account already exists. Please, login.")
                return redirect('signin')
        else:
            messages.warning(request, "Please, fill in all the fields.")
            return redirect('register')    
        

    return render(request, 'signup.html')


def signin(request):

    if request.user.is_authenticated:
        return redirect('diary')
    
    if request.method == 'POST':
        uname= request.POST.get('username') 
        password =  request.POST.get('password')  
       

        if (uname and password ):
            if not get_user_model().objects.filter(username = uname).exists():
                messages.error(request, "No user with this username")
                return redirect('signin')
            else:
                auth = authenticate(request=request, username= uname, password=password)
                if auth:
                    login(request, auth)
                    messages.success(request, "Logged in.")
                    return redirect('index')
                else:
                    messages.error(request, "Please, check your details and try again.")
                    return redirect('signin')
        else:
            messages.warning(request, "Please, fill in all the fields.")
            return redirect('signin')    
        
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('landingpage')


def landingpage(request):
    return render(request, 'landingpage.html')


@login_required(login_url='/login/')
def open_diary(request, id):
    item_to_read = get_object_or_404(Diary, id=id, owner = request.user)
    return render(request, 'readdiary.html', {'item_to_read': item_to_read})