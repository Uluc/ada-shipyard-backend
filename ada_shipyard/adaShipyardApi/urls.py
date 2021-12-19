from django.urls import include, path
from . import views

# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.home, name='website-home'),
#     path('about/', views.about, name='website-about'),
#     path('contact/', views.contact, name='website-contact'),
#     path('projects/', views.projects, name='website-projects'),
#     path('projects/<int:project_id>/', views.project_detail, name='website-project-detail'),
#     path('news/', views.news, name='website-news'),
#     path('news/<int:news_id>/', views.news_detail, name='website-news-detail'),
#     path('quality_policy/', views.quality_policy, name='website-quality-policy'),
# 
]
