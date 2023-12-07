from django import forms
from .models import Post
from detail.models import Info


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'visibility']



class DetailForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        
        
class UserSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
    
    