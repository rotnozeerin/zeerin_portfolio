from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.pass_change, name='passchange'),
    path('pass_change2/', views.pass_change2, name='passchange2'),
    path('profile/', views.profile, name='profile'),
    
    path('create_about/', views.AboutFormView.as_view(), name='createabout'),
    path('show_about', views.AboutListView.as_view(), name='show_about'),
    #path('about_details/<int:id>', views.AboutDetailsView.as_view(), name='about_details'),
    path('edit_about/<int:pk>', views.AboutUpdateView.as_view(), name='edit_about'),
    
    path('create_project_category/', views.CategoryFormView.as_view(), name='create_category'),
    path('show_project_category', views.CategoryListView.as_view(), name='show_category'),
    path('edit_project_category/<int:pk>', views.CategoryUpdateView.as_view(), name='edit_category'),
    path('delete_project_category/<int:pk>', views.DeleteCategoryView.as_view(), name='delete_category'),
    
    path('create_projects/', views.ProjectsFormView.as_view(), name='create_projects'),
    path('show_projects', views.ProjectsListView.as_view(), name='show_projects'),
    path('edit_projects/<int:pk>', views.ProjectsUpdateView.as_view(), name='edit_projects'),
    path('delete_projects/<int:pk>', views.DeleteProjectsView.as_view(), name='delete_projects'),
    
    path('show_resume', views.ResumeListView.as_view(), name='show_resume'),
    path('edit_resume/<int:pk>', views.ResumeUpdateView.as_view(), name='edit_resume'),
    
    path('create_skills/', views.SkillsFormView.as_view(), name='create_skills'),
    path('show_skills', views.SkillsListView.as_view(), name='show_skills'),
    path('edit_skills/<int:pk>', views.SkillsUpdateView.as_view(), name='edit_skills'),
    path('delete_skills/<int:pk>', views.DeleteSkillsView.as_view(), name='delete_skills'),
    
    path('create_proficiency/', views.ProficiencyFormView.as_view(), name='create_proficiency'),
    path('show_proficiency', views.ProficiencyListView.as_view(), name='show_proficiency'),
    path('edit_proficiency/<int:pk>', views.ProficiencyUpdateView.as_view(), name='edit_proficiency'),
    path('delete_proficiency/<int:pk>', views.DeleteProficiencyView.as_view(), name='delete_proficiency'),
    
    path('create_blog/', views.BlogFormView.as_view(), name='create_blog'),
    path('show_blog', views.BlogListView.as_view(), name='show_blog'),
    path('edit_blog/<int:pk>', views.BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', views.DeleteBlogView.as_view(), name='delete_blog'),
    
    path('contact/', views.MailContact, name='contact'),
    path('show_contact', views.ContactListView.as_view(), name='show_contact'),

    path('category/<slug:category_slug>/', views.portfolio_home, name='projects_by_category'),
    path('category/<slug:category_slug>/<slug:project_slug>/', views.project_details, name='project_details'),
    path('submit_review/<int:project_id>/', views.submit_review, name='submit_review'),
    path('blog/<slug:blog_slug>/', views.blog_details, name='blog_details'),
    
]
