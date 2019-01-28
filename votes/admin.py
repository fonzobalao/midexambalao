from django.contrib import admin
from votes.models import *

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Vote)
