from django.shortcuts import render, get_list_or_404, redirect
from .models import Info
from django.contrib.auth.decorators import login_required
from core.models import UserProfile
from django.contrib.auth.models import User
# Create your views here.


@login_required
def follow_user(request, username):
    user_to_follow = User.objects.get(username = username)
    user_profile = UserProfile.objects.get(user = request.user)
    
    if user_to_follow != request.user:
        user_profile.following.add(user_to_follow.id)
        
    return redirect('profile', player_id = user_to_follow.id)    


@login_required
def unfollow_user(request, username):
    user_to_unfollow = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user = request.user)
    user_profile.following.remove(user_to_unfollow)
    
    return redirect('profile', player_id = user_to_unfollow.id)




def ProfileView(request, player_id):
    
    profile = Info.objects.get(id=player_id)
    
    context = {
        'profile' : profile,
        'pk' : player_id
    }
    
    print(player_id)
    return render(request, 'profile.html', context)
    
    
def SponsorPage(request, pk):
    profile = Info.objects.get(id=pk)
    
    context = {
        'profile':profile,
        'pk' : pk

    }    
    return render(request, 'sponsor.html', context)

