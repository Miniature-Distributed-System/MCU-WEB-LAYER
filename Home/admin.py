from django.contrib import admin
from Home.models import usersinfo, filelog, diagnosis_instance, disease_instance

admin.site.register(usersinfo)
admin.site.register(filelog)
admin.site.register(diagnosis_instance)
admin.site.register(disease_instance)