from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

router =routers.DefaultRouter()
router.register('meals',views.MealViewSet)
router.register('ratings',views.RatingViewSet)
router.register('register',views.UserViewSet)



urlpatterns = [
    path('',include(router.urls))
]

