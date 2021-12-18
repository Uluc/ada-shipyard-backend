from django.shortcuts import render

from .models.certificate_model import Certificate
from .models.corporate_model import Corporate
from .models.health_safety_model import HealthAndSafety
from .models.news_model import News
from .models.project_model import Project
from .models.quality_policy_model import QualityPolicy
from .models.sections_model import Section

def home(request):
    return render(request, 'ada_shipyard/home.html')