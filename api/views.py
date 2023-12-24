from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets ,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
   # authenticaton_classes =[TokenAuthentication,]
    permission_classes=[AllowAny,]
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token,created=Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {'token':token.key,},
            status=status.HTTP_201_CREATED,)
    def list(self, request, *args, **kwargs):
        response={
            'message':'you cant create rating like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)


class MealViewSet(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer
    authenticaton_classes =[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            #username = request.data['username']
            #user = User.objects.get(username=username)

            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

            except:
                # create if the rate not exist 
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    authenticaton_classes =[TokenAuthentication,]
    permission_classes=[IsAuthenticated]

    def update(self, request, *args, **kwargs):
        response ={
            'message':'this way not provided'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response ={
            'message':'this way not provided'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)