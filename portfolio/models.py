from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Count

class Profile(models.Model):
    name = models.CharField(blank=True,null=True,max_length=100)
    background_pic = models.ImageField(upload_to="profile/")
    short_bio=models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    cv = models.FileField(upload_to="profile/cv", max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        
class About(models.Model):
    profile_pic = models.ImageField(upload_to="about/")
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    long_details=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, blank = True) 
    cat_image = models.ImageField(upload_to = 'projects/categories', blank = True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

    
class Projects(models.Model):
    id = models.IntegerField(primary_key=id)
    project_title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    screenshots = models.ImageField(upload_to='projects/')
    technologies_used = models.CharField(max_length=250)
    project_url = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'project'
        verbose_name_plural = 'projects'

class Skill(models.Model):
    skill_type= models.CharField(max_length=100)
    skill_percentage = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'skill'
        verbose_name_plural = 'skills'
        
class Proficiency(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(blank=True,null=True)
    icon = models.ImageField(upload_to='proficiency/')
    link = models.CharField(max_length=150)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'proficiency'
        verbose_name_plural = 'proficiencies'\
            
class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    short_description = models.TextField(blank=True,null=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='blog/')
    link = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    subject = models.CharField(max_length=200)
    message=models.TextField(max_length = 255, blank = True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        
def get_url(self):
        return reverse('project_details', args=[self.category.slug, self.slug])
            
def averageReview(self):
    reviews = ReviewRating.objects.filter(projects = self, status=True).aggregate(average = Avg('rating'))
    avg = 0
    if reviews['average'] is not None:
        avg = float(reviews['average'])
    return avg

def countReview(self):
    reviews = ReviewRating.objects.filter(projects = self, status=True).aggregate(count = Count('id'))
    count = 0
    if reviews['count'] is not None:
        count = float(reviews['count'])
    return count


class ReviewRating(models.Model):
    project = models.ForeignKey(Projects, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject