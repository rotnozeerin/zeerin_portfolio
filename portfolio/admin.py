from django.contrib import admin
from .models import Blog, Contact, Proficiency, Profile, About, Skill, Category, Projects

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug')

class ProjectsAdmin(admin.ModelAdmin): # admin panel customize korte modeladmin use kori
     list_display = ['project_title', 'technologies_used', 'project_url', 'category','description' ,'created_date', 'modified_date']
     prepopulated_fields = {'slug' : ('project_title',)}
     

# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skill)
admin.site.register(Proficiency)
admin.site.register(Blog)
admin.site.register(Contact)
