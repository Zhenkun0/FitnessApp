from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.status import *

from base.models import Order, OrderItem, BillingAddress, Trainer, Review

from rest_framework import status

from base.serializer import TrainerSerializer, OrderSerializer

param_id = openapi.Parameter('id', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
order_response = openapi.Response('response description', OrderSerializer)
orders_response = openapi.Response('response description', OrderSerializer(many=True))


# TODO
# Custom description and data type for swagger yaml
# example
# {
#     "_id": 5,
#     "orderItems": [
#         {
#             "_id": 6,
#             "name": "Yosuke",
#             "qty": 1,
#             "price": null,
#             "image": "/images/Screen_Shot_2022-02-24_at_8.58.09_PM.png",
#             "trainer": 5,
#             "order": 5
#         }
#     ],
#     "billingAddress": false,
#     "user": {
#         "id": 3,
#         "_id": 3,
#         "username": "foo2@test.com",
#         "name": "foo2",
#         "email": "foo2@test.com",
#         "first_name": "foo2",
#         "last_name": "bar2",
#         "isAdmin": false
#     },
#     "paymentMethod": "PayPal",
#     "taxPrice": "0.00",
#     "shippingPrice": "10.00",
#     "totalPrice": "10.00",
#     "paidAt": null,
#     "isDelivered": false,
#     "deliveredAt": null,
#     "createdAt": "2022-02-27T00:43:06.990429Z"
# }


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

        shipping = BillingAddress.objects.create(
            order=order,
            address=data['billingAddress']['address'],
            city=data['billingAddress']['city'],
            postalCode=data['billingAddress']['postalCode'],
            country=data['billingAddress']['country'],
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


# TODO
# include above data example to swagger API
@swagger_auto_schema(methods=['get'], manual_parameters=[param_id], responses={200: order_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No authorized to view this order'}, status=HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Order does not exists'}, status=HTTP_404_NOT_FOUND)


# TODO
@swagger_auto_schema(methods=['put', 'patch'], manual_parameters=[param_id], responses={200: 'Order was paid'})
@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(_id=pk)
    order.isPaid = True
    order.save()

    return Response('Order was paid')


@swagger_auto_schema(methods=['get'], responses={200: orders_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):

    user = request.user

    order = user.order_set.all()
    if order is None:
        return Response({'detail': 'Order does not exists'}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

