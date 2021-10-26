from django.contrib import admin

from .models.certificate_model import Certificate
from .models.corporate_model import Corporate
from .models.health_safety_model import HealthAndSafety
from .models.news_model import News
from .models.project_model import Project
from .models.quality_policy_model import QualityPolicy
from .models.sections_model import Section

admin.site.register(Certificate)
admin.site.register(Corporate)
admin.site.register(HealthAndSafety)
admin.site.register(News)
admin.site.register(Project)
admin.site.register(QualityPolicy)
admin.site.register(Section)
