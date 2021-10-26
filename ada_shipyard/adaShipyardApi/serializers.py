# serializers.py
from rest_framework import serializers

from .models.certificate_model import Certificate
from .models.corporate_model import Corporate
from .models.health_safety_model import HealthAndSafety
from .models.news_model import News
from .models.project_model import Project
from .models.quality_policy_model import QualityPolicy
from .models.sections_model import Section

class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'certificate_name', 'certificate_image', 'certificate_description')

class CorporateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corporate
        fields = ('id', 'corporate_name', 'corporate_image', 'corporate_description')

class HealthAndSafetySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthAndSafety
        fields = ('id', 'health_safety_name', 'health_safety_image', 'health_safety_description')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'news_name', 'news_image', 'news_description')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'project_name', 'project_image', 'project_description', 
        'project_length', 'project_width', 'project_breadth', 'project_depth', 'project_gross_tonnage')

class QualityPolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QualityPolicy
        fields = ('id', 'quality_policy_text')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('corporate_image', 'facilities_image', 'projects_image', 'news_image', 'contact_image', 'about_image', 'home_image')