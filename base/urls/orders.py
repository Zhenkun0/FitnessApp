from django.urls import path
from base.views import orders as views

urlpatterns = [

    path('add/', views.addOrderItems, name="orders-add"),
    # path('upload/', views.uploadImage, name="image-upload"),

    # path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    # path('top/', views.getTopTrainers, name='top-trainers'),
    # path('<str:pk>/', views.getTrainer, name='trainer')

    # path('update/<str:pk>/', views.updateProduct, name="product-update"),
    # path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
]