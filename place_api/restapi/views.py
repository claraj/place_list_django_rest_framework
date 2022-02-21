from django.shortcuts import render
from rest_framework import viewsets 
from place_api.restapi.serializers import PlaceSerializer
from place_api.restapi.models import Place
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.core.exceptions import ValidationError


def homepage(request):
    return HttpResponse('Hello Android Students.')


class PlaceViewSet(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user).order_by('priority')

    def create(self, request):
        try:
            print('creating', request.data)
            place_ = Place(name=request.data.get('name'), reason=request.data.get('reason'), priority=request.data.get('priority'), user=request.user)
            place_.full_clean()
            place_.save()
            return Response(PlaceSerializer(place_).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            print('Invalid request, validation error ' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Priority must be positive'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            print('Invalid request, integrity error ' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Rating must be between 0 and 5.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Invalid request' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Rating must be between 0 and 5.'}, status=status.HTTP_400_BAD_REQUEST)
