# Create your views here.
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, UserProfile
from detail.models import category, Info
from .forms import PostForm, DetailForm





@login_required(login_url='login')
def HomePage(request):
    user_profile = UserProfile.objects.get(user=request.user)
    following = user_profile.following.all()
    following_users = [user.user for user in following]

    posts = Post.objects.filter(user__in=following_users).order_by('-timestamp')
    form = PostForm()
    
    information = get_object_or_404(Info, id=user_profile.user.id )
    profile_image = information.Profile_Image.url if information.Profile_Image else None


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')
    print(user_profile.user.id)
    context = {
        'posts': posts,
        'form': form,
        'pk' : user_profile.user.id,
        'information': information,
        'profile_image' : profile_image
    }
    
    return render(request, 'home.html', context)




def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        Name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        
        if User.objects.filter(username = uname).exists():
            return HttpResponse("Username is already taken.")
        
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('detailpage')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def detailPage(request):
    form = DetailForm()
    
    if request.method == 'POST':
        form  = DetailForm(request.POST)
        
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')
    
    context = {

        'form' : form
    }
    return render (request,'details.html', context)


def Search_View(request):
    results=[]
    #profile = Info.objects.get()
    query = request.GET.get('query', '')
    if query:
        results = User.objects.filter(username__icontains=query)
    context = {
       "results" : results,
       'query': query,
       'pk':8
       }
    
   
    return render(request, 'search.html', context)
