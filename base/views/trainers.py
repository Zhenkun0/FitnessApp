from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Trainer, Review

from base.serializer import TrainerSerializer

param_keyword = openapi.Parameter('keyword', openapi.IN_QUERY, description="test manual param",
                                  type=openapi.TYPE_STRING)
param_page = openapi.Parameter('page', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_INTEGER)
param_id = openapi.Parameter('id', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
trainer_response = openapi.Response('response description', TrainerSerializer)


@swagger_auto_schema(methods=['get'], manual_parameters=[param_keyword, param_page], responses={200: trainer_response})
@api_view(['GET'])
def getTrainers(request):
    query = request.query_params.get('keyword')
    if query is None:
        query = ''

    trainers = Trainer.objects.filter(
        first_name__icontains=query).order_by('-createdAt')
    # TODO search both first and last
    # trainers += Trainer.objects.filter(
    #     last_name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(trainers, 5)

    try:
        trainers = paginator.page(page)
    except PageNotAnInteger:
        trainers = paginator.page(1)
    except EmptyPage:
        trainers = paginator.page(paginator.num_pages)

    if page is None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = TrainerSerializer(trainers, many=True)
    return Response({'trainers': serializer.data, 'page': page, 'pages': paginator.num_pages})


@swagger_auto_schema(methods=['get'], manual_parameters=[param_id], responses={200: trainer_response})
@api_view(['GET'])
def getTrainer(request, pk):
    trainer = Trainer.objects.get(_id=pk)
    serializer = TrainerSerializer(trainer, many=False)
    return Response(serializer.data)


@swagger_auto_schema(methods=['get'], manual_parameters=[param_id], responses={200: trainer_response})
@api_view(['GET'])
def getTopTrainers(request):
    trainers = Trainer.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = TrainerSerializer(trainers, many=True)
    return Response(serializer.data)

# TODO
@swagger_auto_schema(methods=['post'], request_body=TrainerSerializer)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createTrainer(request):
    user = request.user

    trainer = Trainer.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )
