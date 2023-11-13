from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet



    
    
class Post(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/post_images', blank=True, null=True)
    
    VISIBILITY_CHOICES = (
        ('public', 'public'),
        ('Followers', 'Followers'),
        ('Only Me', 'Only Me')
    )
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE ,primary_key=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    