from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model =Meal
        fields =['id','title','description','no_ratings','avg_ratings']

class UserSerializer(serializers.ModelSerializer):
   class Meta:
    model =User
    fields=['id','username','password']
    extra_kwargs={'password':{'write_only':True,'required':True}}