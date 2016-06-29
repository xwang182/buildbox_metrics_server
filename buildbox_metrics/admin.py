from django.contrib import admin

from .models import BuildTrain, Build, Deliverable

admin.site.register(BuildTrain)
admin.site.register(Build)
admin.site.register(Deliverable)
