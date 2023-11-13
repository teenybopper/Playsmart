from .views import SponsorPage, ProfileView, unfollow_user, follow_user
from django.urls import path

app_name = 'detail'

urlpatterns = [
    path('<int:pk>/sponsor/', SponsorPage, name ='sponsor'),
    path('<int:player_id>/', ProfileView, name = 'player_profile'),
    path('unfollow/<str:username>', unfollow_user, name='unfollow'),
    path('follow/<str:username>', follow_user, name='follow')
]