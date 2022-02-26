from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Order, OrderItem, ShippingAddress, Trainer, Review

from rest_framework import status

from base.serializer import TrainerSerializer, OrderSerializer


@swagger_auto_schema(methods=['post'], request_body=OrderSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No order items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # (1) create order
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )

        # (2) Create shipping address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            trainer = Trainer.objects.get(_id=i['trainer'])

            item = OrderItem.objects.create(
                trainer=trainer,
                order=order,
                name=trainer.first_name,
                qty=i['qty'],
                price=i['price'],
                image=trainer.image.url,
            )

            # (4) Update stock

            trainer.countInStock -= item.qty
            trainer.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def getTrainer(request, pk):
    trainer = Trainer.objects.get(_id=pk)
    serializer = TrainerSerializer(trainer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getTopTrainers(request):
    trainers = Trainer.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = TrainerSerializer(trainers, many=True)
    return Response(serializer.data)


# TODO
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
