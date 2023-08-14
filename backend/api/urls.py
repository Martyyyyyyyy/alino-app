from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('users/<int:id>/', get_user, name='users'),
    path('user/', create_user),
    path('login/<str:email_address>/', check_login),
    path('categories/', categories_list),
    path('restaurants/', restaurants_list),
    path('restaurants/<int:pk>/', restaurants_by_id, name='restaurants'),
    path('barbershop/', barbershop_list),
    path('barbershop/<int:pk>/', barbershop_by_id, name='barbershop'),
    path('reservations/user/<int:userId>/', reservations_by_userId),
    path('history/user/<int:userId>/', history_by_userId),
    path('favorites/user/<int:userId>/', favorites_by_userId),
    path('bookings/kramar_rest/<int:userId>/', booking_by_userId),
    path('reviews_list/', reviews_list),
    path('rates/', rates_list),
    path('rates/<int:pk>/', rates_list_by_id, name='rates'),
    path('specialist/', specialist_list),
    path('advertising/', advertising_list),
    path('promotion/', promotion_list),
]