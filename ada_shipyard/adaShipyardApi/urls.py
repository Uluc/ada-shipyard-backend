from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'certificates', views.CertificateViewSet)
router.register(r'corporates', views.CorporateViewSet)
router.register(r'health_safety', views.HealthAndSafetyViewSet)
router.register(r'news',views.NewsViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'quality_policy', views.QualityPolicyViewSet)
router.register(r'sections', views.QualityPolicyViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]