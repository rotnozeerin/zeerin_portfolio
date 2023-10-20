from django import forms
from .models import Contact, ReviewRating, About, Category, Projects, Profile, Skill, Proficiency, Blog

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
    
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['name', 'designation', 'email', 'phone_number', 'long_details', 'profile_pic']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_type', 'skill_percentage']
 
class ProficiencyForm(forms.ModelForm):
    class Meta:
        model = Proficiency
        fields = ['name', 'short_description', 'link', 'icon']         

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'slug','short_description','description','link', 'image']  
        
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'short_bio', 'designation', 'cv']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'slug', 'description', 'cat_image']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['category', 'project_title', 'slug', 'description', 'technologies_used', 'project_url', 'screenshots']
        

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=True,max_length=254)
    subject = forms.CharField(required=True,max_length=300)
    message = forms.CharField(required=True,widget=forms.Textarea)
    
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your E-mail Address'
        self.fields['subject'].widget.attrs['placeholder'] = 'Your Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '10'
    
