from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from .forms import PostForm
from home.models import Post
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
def index(request):
    form = PostForm()  
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    pro = Post.objects.all()
    if request.method == "GET":
        st= request.GET.get('searchname')
        if st!=None:
            pro = Post.objects.filter(title__icontains = st)
    return render(request, 'index.html', {'form': form, 'pro': pro})

def edit(request, id):
    
    pro = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.FILES, request.POST , instance=pro)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home', id=id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PostForm(instance=pro)
    return render(request,'edit.html', {'form':form})

def remove(request, id):
    profile = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, "successfully deleted")
        return redirect('index')
    return render(request, 'remove.html', {'profile':profile})

def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
             messages.error(request, "Sorry, your username or password is incorrect.")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:

         my_user= User.objects.create_user(username= username, email=email, password=password)
         my_user.save()
         messages.success(request, "successfully login")
        return redirect('login_view')
    else:
        messages.error(request, "sorry ")
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    