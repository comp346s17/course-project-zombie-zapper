from django.contrib import admin
from .models import Habit
from .models import Profile
from .models import Commitment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Habit)
admin.site.register(Commitment)