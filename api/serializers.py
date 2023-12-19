from rest_framework import serializers
from .models import *




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model =Meal
        fields =['id','title','description']

