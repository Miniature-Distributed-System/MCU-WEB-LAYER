from django.contrib import admin
from Home.models import usersinfo, filelog,devlog, instances

admin.site.register(usersinfo)
admin.site.register(filelog)
admin.site.register(devlog)
admin.site.register(instances)