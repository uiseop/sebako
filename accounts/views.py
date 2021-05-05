from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from accounts.models import Blog, Profile


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})
    # return render(request, 'zzsignup.html')


def detail(request, pk):
    # blog_detail = get_object_or_404(Blog, pk=pk)
    blog_detail = Blog.objects.get(pk=pk)
    return render(request, 'detail.html', {'blog': blog_detail})


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'signup_error.html')

        if request.POST['password1'] == request.POST['password2']:
            if len(request.POST['password1']) < 8:
                messages.info(request,'비밀 짧아')
                return redirect('signup')

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            korName = '한국'
            engName = 'Engl'
            address = 'bababobo'
            email = 'babo@babo.com'
            phone = '010-5123-4567'
            # korName = request.POST['korName']
            # engName = request.POST['engName']
            # address = request.POST['address']
            # email = request.POST['email']
            # phone = request.POST['phone']
            profile = Profile(user, korName, engName, address, email, phone)
            profile.save()
            auth.login(request, user)
            return redirect('home')

        return render(request, 'zzsignup.html')
    return render(request, 'zzsignup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
