from rest_framework import viewsets

from .serializers import CertificateSerializer, CorporateSerializer, HealthAndSafetySerializer, NewsSerializer, ProjectSerializer,QualityPolicySerializer, SectionSerializer 

from .models.certificate_model import Certificate
from .models.corporate_model import Corporate
from .models.health_safety_model import HealthAndSafety
from .models.news_model import News
from .models.project_model import Project
from .models.quality_policy_model import QualityPolicy
from .models.sections_model import Section



class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all().order_by('id')
    serializer_class = CertificateSerializer

class CorporateViewSet(viewsets.ModelViewSet):
    queryset = Corporate.objects.all().order_by('id')
    serializer_class = CorporateSerializer
class HealthAndSafetyViewSet(viewsets.ModelViewSet):
    queryset = HealthAndSafety.objects.all().order_by('id')
    serializer_class = HealthAndSafetySerializer
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class QualityPolicyViewSet(viewsets.ModelViewSet):
    queryset = QualityPolicy.objects.all().order_by('id')
    serializer_class = QualityPolicySerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all().order_by('id')
    serializer_class = SectionSerializer