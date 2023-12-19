from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display =['id','title','description']
    search_fields =['title','description']
    list_filter =['title','description']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display =['id','meal','user','stars']
    list_filter =['meal','user']

