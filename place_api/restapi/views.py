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
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


def homepage(request):
    return HttpResponse('Hello Android Students.')


class PlaceViewSet(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user).order_by('name')

    def create(self, request):
        if request.method != 'POST':
            return Response("Wrong method")
        try:
            print('creating', request.data)

            serializer = PlaceSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
            # place_ = Place(name=request.data.get('name'), reason=request.data.get('reason'), priority=request.data.get('priority'), user=request.user)
            # place_.full_clean()
            # place_.save()
                return Response({'success': 'created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
                
        except ValidationError as e:
            print('Invalid request, validation error ' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Priority must be positive'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            print('Invalid request, integrity error ' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Rating must be between 0 and 5.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Invalid request' + str(e))
            return Response({'error': 'Invalid data. Place name must be unique. Rating must be between 0 and 5.'}, status=status.HTTP_400_BAD_REQUEST)


# TODO 
"""    if Place.objects.filter(user=self.user).filter(name__iexact=self.name).first():
  File "/Users/ladmin/development/python/place_list_django_rest_framework/venv/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 197, in __get__
    raise self.RelatedObjectDoesNotExist(
place_api.restapi.models.Place.user.RelatedObjectDoesNotExist: Place has no user."""

    # @action(detail=False, methods=['patch'])
    # def update_many(self, request):
    #     print(request.data)
    #     # place_list = JSONParser().parse(request.data)
    #     # print(place_list)
    #     serializer = PlaceSerializer(data=request.data, many=True)
    #     if serializer.is_valid():
    #         print(serializer)
    #         serializer.save()
    #         return Response({'ok': 'updated'}, status=200)
    #     else:
    #         return Response({'no': 'updated'}, status=400)
    #     # return JsonResponse(serializer.errors, status=400)