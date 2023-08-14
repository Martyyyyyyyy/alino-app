from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from rest_framework .parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework .views import APIView
from json import JSONDecodeError
import requests
import json

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data
            response_data['UserId'] = user.id
            return JsonResponse(response_data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def check_login(request,email_address):
    try:
        user = User.objects.filter(email_address=email_address)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
       serializer = UserSerializer(user,many=True)
       return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
       serializer = UserSerializer(user)
       return JsonResponse(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(id=data['UserId'])
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data
            response_data['UserId'] = user.id
            return JsonResponse(response_data, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'PATCH'])

@csrf_exempt 
def categories_list(request): 
    if request.method == 'GET': 
        reviews = Categories.objects.all().order_by('id').reverse()
        serializer = CategoriesSerializer(reviews, many=True) 
        return JsonResponse(serializer.data, safe=False) 
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = CategoriesSerializer(reviews, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = CategoriesSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def restaurants_list(request):
    if request.method == 'GET':
        restaurants = Restaurants.objects.all().order_by('name').reverse()
        serializer = RestaurantsSerializer(restaurants ,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestaurantsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def barbershop_list(request):
    if request.method == 'GET':
        restaurants = Barbershop.objects.all().order_by('name').reverse()
        serializer = BarbershopSerializer(restaurants ,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BarbershopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def restaurants_by_id(request, pk):
    if request.method == 'GET':
        if pk:
            try:
                restaurants = Restaurants.objects.get(pk=pk)
            except Restaurants.DoesNotExist:
                return HttpResponse(status=404)
            serializer = RestaurantsSerializer(restaurants)
        else:
            restaurants = Restaurants.objects.all()
            serializer = RestaurantsSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            restaurants = Restaurants.objects.get(pk=pk)
        except Restaurants.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = RestaurantsSerializer(restaurants, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def barbershop_by_id(request, pk):
    if request.method == 'GET':
        if pk:
            try:
                barbershop = Barbershop.objects.get(pk=pk)
            except Barbershop.DoesNotExist:
                return HttpResponse(status=404)
            serializer = BarbershopSerializer(barbershop)
        else:
            barbershop = Barbershop.objects.all()
            serializer = BarbershopSerializer(barbershop, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            barbershop = Barbershop.objects.get(pk=pk)
        except Barbershop.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = BarbershopSerializer(barbershop, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def reservations_by_userId(request, userId):
    if request.method == 'GET':
        if userId:
            try:
                reservation = Reservation2.objects.filter(userId=userId, status='pending')
            except Reservation2.DoesNotExist:
                return HttpResponse(status=404)
            serializer = ReservationSerializer(reservation, many=True)
        else:
            reservation = Reservation2.objects.all()
            serializer = ReservationSerializer(reservation, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            reservation = Reservation2.objects.filter(userId=userId)
        except Reservation2.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = ReservationSerializer(reservation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = ReservationSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE': 
        reservation.delete() 
        return HttpResponse(status=204)
    
@csrf_exempt
def history_by_userId(request, userId):
    if request.method == 'GET':
        if userId:
            try:
                history = History.objects.filter(userId=userId, status='closed')
            except History.DoesNotExist:
                return HttpResponse(status=404)
            serializer = HistorySerializer(history, many=True)
        else:
            history = History.objects.all()
            serializer = HistorySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            history = History.objects.filter(userId=userId)
        except History.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = HistorySerializer(history, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = HistorySerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE': 
        history.delete() 
        return HttpResponse(status=204)

@csrf_exempt
def favorites_by_userId(request, userId):
    if request.method == 'GET':
        if userId:
            try:
                favorites = Favorites.objects.filter(userId=userId)
            except Favorites.DoesNotExist:
                return HttpResponse(status=404)
            serializer = FavoritesSerializer(favorites, many=True)
        else:
            favorites = Favorites.objects.all()
            serializer = FavoritesSerializer(favorites, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            favorites = Favorites.objects.filter(userId=userId)
            if not favorites.exists():
                return HttpResponse(status=404)
        except Favorites.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = FavoritesSerializer(favorites, data=data)
        if serializer.is_valid():
            serializer.save(request=request)
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FavoritesSerializer(data=data)
        if serializer.is_valid():
            favorite = serializer.save()
            response_data = serializer.data
            response_data['id'] = favorite.id
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            favorites = Favorites.objects.filter(userId=userId)
            if not favorites.exists():
                return HttpResponse(status=404)
            favorites.delete()
            return HttpResponse(status=204)
        except Favorites.DoesNotExist:
            return HttpResponse(status=404)

@csrf_exempt
def booking_by_userId(request, userId):
    if request.method == 'GET':
        if userId:
            try:
                booking = Booking.objects.filter(userId=userId)
            except Booking.DoesNotExist:
                return HttpResponse(status=404)
            serializer = BookingSerializer(booking, many=True)
        else:
            booking = Booking.objects.all()
            serializer = BookingSerializer(booking, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            response_data = {"error": "Invalid JSON payload"}
            return JsonResponse(response_data, status=400)
        booking = Booking.objects.filter(userId=userId)
        serializer = BookingSerializer(booking, data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {"status": "success"}
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            #booking = Booking.objects.filter(userId=userId).first()
            serializer = BookingSerializer(data=json_data)
            if serializer.is_valid():
                booking1 = serializer.save()
                response_data = serializer.data
                response_data['id'] = booking1.id
                updated_data = serializer.data  # get the updated data from the serializer
                headers = {'Content-Type': 'application/json'}
                response = requests.post('https://kramar-rest.com/api/public/booking/', data=json.dumps(updated_data), headers=headers)
                if response.ok:
                    return JsonResponse(response_data, status=201)
                else:
                    response_data = response.json()
                    return JsonResponse(response_data, status=response.status_code)
            else:
                response_data = {"error": serializer.errors}
                return JsonResponse(response_data, status=400)
        except JSONDecodeError:
            response_data = {"error": "Invalid JSON payload"}
            return JsonResponse(response_data, status=400)
        except Exception as e:
            response_data = {"error": str(e)}
            return JsonResponse(response_data, status=500)
     
@csrf_exempt 
def reviews_list(request): 
    if request.method == 'GET': 
        reviews = Reviews.objects.all().order_by('id').reverse()
        serializer = ReviewsSerializer(reviews, many=True) 
        return JsonResponse(serializer.data, safe=False) 
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = ReviewsSerializer(reviews, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = ReviewsSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) 

@csrf_exempt
def rates_list(request):
    if request.method == 'GET': 
        rates = Rates.objects.all().order_by('id').reverse()
        serializer = RatesSerializer(rates, many=True) 
        return JsonResponse(serializer.data, safe=False) 
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = RatesSerializer(rates, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = RatesSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE': 
        rates.delete() 
        return HttpResponse(status=204)

@csrf_exempt
def rates_list_by_id(request, pk):
    if request.method == 'GET':
        if pk:
            try:
                rates = Rates.objects.get(pk=pk)
            except Rates.DoesNotExist:
                return HttpResponse(status=404)
            serializer = RatesSerializer(rates)
        else:
            rates = Rates.objects.all()
            serializer = RatesSerializer(rates, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            rates = Rates.objects.get(pk=pk)
        except Rates.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = RatesSerializer(rates, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            rates = Rates.objects.get(pk=pk)
        except Rates.DoesNotExist:
            return HttpResponse(status=404)
        rates.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def specialist_list(request):
    if request.method == 'GET':
        specialist = Specialist.objects.all().order_by('rate').reverse()
        serializer = SpecialistSerializer(specialist ,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SpecialistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def advertising_list(request):
    if request.method == 'GET': 
        advertising = Advertising.objects.all().order_by('id').reverse()
        serializer = AdvertisingSerializer(advertising, many=True) 
        return JsonResponse(serializer.data, safe=False) 
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = AdvertisingSerializer(advertising, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = AdvertisingSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE': 
        advertising.delete() 
        return HttpResponse(status=204)

@csrf_exempt
def promotion_list(request):
    if request.method == 'GET':
        promotion = Promotion.objects.all().order_by('position').reverse()
        serializer = PromotionSerializer(promotion ,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PromotionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)