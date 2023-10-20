from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm, ChangeUserData,ContactForm, ReviewForm, AboutForm, CategoryForm, ProjectsForm, ResumeForm, SkillForm, ProficiencyForm, BlogForm
from .models import About, Contact, Profile, Skill, Proficiency, Blog, Category, Projects, ReviewRating
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

def portfolio_home(request, category_slug=None):
    #return render(request, './portfolio/index.html')
    profile = Profile.objects.first()
    about = About.objects.first()
    category = None
    projects = None
    
    if category_slug : 
        category = get_object_or_404(Category, slug = category_slug)
        projects = Projects.objects.filter(category=category) # category wise projects
  
    else : 
        projects = Projects.objects.all() # all projects
        
    categories = Category.objects.all()
    
    skill = Skill.objects.all()
    proficiency = Proficiency.objects.all()
    blog = Blog.objects.all()
    form = ContactForm()
    context = {
        'profile':profile,
        'about':about,
        'categories' : categories,
        'projects' : projects,
        'skill':skill,
        'proficiency':proficiency,
        'blog': blog,
        'form': form,
        
    }
    return render(request, 'index.html',context)


def project_details(request, category_slug=None, project_slug=None):
    single_project = Projects.objects.get(slug = project_slug, category__slug = category_slug) # category wise projects
    #print(single_project)
    reviews = ReviewRating.objects.filter(project_id=single_project.id, status=True)
    context = {
        'single_project': single_project,
        'reviews': reviews
    }
    return render(request, 'project_details.html', context)
    #return render(request, 'project_details.html', single_project)
    
def blog_details(request, blog_slug=None):
    single_blog = Blog.objects.get(slug = blog_slug) 
    return render(request, 'blog_details.html', {"single_blog":single_blog})

def submit_review(request, project_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            project = Projects.objects.get(id = project_id)
            reviews = ReviewRating.objects.get(user = request.user, project = project)
            form = ReviewForm(request.POST, instance = reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.project_id = project_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted')
                return redirect(url)
            
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
       return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass) # check kortechi user database e ache kina
                if user is not None:
                    login(request, user)
                    return redirect('profile') # profile page e redirect korbe    
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')                

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) # password update korbe
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form':form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) # password update korbe
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form':form})
    else:
        return redirect('login')

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')

def MailContact(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  
            messages.success(request,"Conform form submitted successfully")
            form.save()
    return redirect(url)

    
class AboutFormView(CreateView):
    model = About
    template_name = 'create_about.html'
    form_class = AboutForm
    success_url = reverse_lazy('show_about')
    
class AboutListView(ListView):
    model = About
    template_name = 'show_about.html'
    context_object_name = 'aboutlist'
     

class AboutUpdateView(UpdateView):
    model = About
    template_name = 'create_about.html'
    form_class = AboutForm
    success_url = reverse_lazy('show_about')
    
class CategoryFormView(CreateView):
    model = Category
    template_name = 'create_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('show_category')
    
class CategoryListView(ListView):
    model = Category
    template_name = 'show_category.html'
    context_object_name = 'categorylist'
     

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'create_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('show_category')

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_category')
    
    
class ProjectsFormView(CreateView):
    model = Projects
    template_name = 'create_projects.html'
    form_class = ProjectsForm
    success_url = reverse_lazy('show_projects')
    
class ProjectsListView(ListView):
    model = Projects
    template_name = 'show_projects.html'
    context_object_name = 'projectslist'
     

class ProjectsUpdateView(UpdateView):
    model = Projects
    template_name = 'create_projects.html'
    form_class = ProjectsForm
    success_url = reverse_lazy('show_projects')

class DeleteProjectsView(DeleteView):
    model = Projects
    template_name = 'delete_projects_confirmation.html'
    success_url = reverse_lazy('show_projects')

class ResumeListView(ListView):
    model = Profile
    template_name = 'show_resume.html'
    context_object_name = 'resume'

class ResumeUpdateView(UpdateView):
    model = Profile
    template_name = 'create_resume.html'
    form_class = ResumeForm
    success_url = reverse_lazy('show_resume')
    
class SkillsFormView(CreateView):
    model = Skill
    template_name = 'create_skills.html'
    form_class = SkillForm
    success_url = reverse_lazy('show_skills')
    
class SkillsListView(ListView):
    model = Skill
    template_name = 'show_skills.html'
    context_object_name = 'skillslist'
     
class SkillsUpdateView(UpdateView):
    model = Skill
    template_name = 'create_skills.html'
    form_class = SkillForm
    success_url = reverse_lazy('show_skills')

class DeleteSkillsView(DeleteView):
    model = Skill
    template_name = 'delete_skills_confirmation.html'
    success_url = reverse_lazy('show_skills')
    
class ProficiencyFormView(CreateView):
    model = Proficiency
    template_name = 'create_proficiency.html'
    form_class = ProficiencyForm
    success_url = reverse_lazy('show_proficiency')
    
class ProficiencyListView(ListView):
    model = Proficiency
    template_name = 'show_proficiency.html'
    context_object_name = 'proficiencylist'
     
class ProficiencyUpdateView(UpdateView):
    model = Proficiency
    template_name = 'create_proficiency.html'
    form_class = ProficiencyForm
    success_url = reverse_lazy('show_proficiency')

class DeleteProficiencyView(DeleteView):
    model = Proficiency
    template_name = 'delete_proficiency_confirmation.html'
    success_url = reverse_lazy('show_proficiency')
    
class BlogFormView(CreateView):
    model = Blog
    template_name = 'create_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('show_blog')
    
class BlogListView(ListView):
    model = Blog
    template_name = 'show_blog.html'
    context_object_name = 'bloglist'
     
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'create_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('show_blog')

class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete_blog_confirmation.html'
    success_url = reverse_lazy('show_blog')
    
class ContactListView(ListView):
    model = Contact
    template_name = 'show_contact.html'
    context_object_name = 'contactlist'