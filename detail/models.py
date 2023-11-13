from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:         
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name 
    
class Info(models.Model):
    category = models.ForeignKey(category, related_name='Info', on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    description = models.TextField(blank = True, null = True)
    Joined = models.DateField(auto_now_add=True)
    level_choices = (
        ('1', 'zonal'),
        ('2','district'),
        ('3', 'state'),
        ('4', 'ranji'),
        ('5', 'Syed'),
        ('6', 'dilip'),
        ('7', 'Irani'),
        ('8', 'Deodar'),
        ('9', 'Vijay')
        )
    levels = models.CharField(null=True, max_length=20, choices=level_choices)
    Age = models.IntegerField(null=True)
    skill_choices = (
        ('bat', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All Rounder', 'All Rounder'),
        
    )
    Profile_Image = models.ImageField(upload_to = 'images/pfp_images', blank=True, null=True)
    skill = models.CharField(max_length=30, choices=skill_choices)
    
    def __str__(self):
        return self.Name