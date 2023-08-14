from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'second_name', 'email_address', 'password', 'phone_number', 'date_created']


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'email_address', 'password')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'restaurants', 'barbers']

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'type', 'name', 'description', 'image_url', 'rate', 'location', 'api_url', 'template']

class BarbershopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbershop
        fields = ['id', 'type', 'name', 'description', 'image_url', 'rate', 'location']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation2
        fields = ['id', 'booking', 'status']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'userId', 'restaurant', 'date', 'time', 'party_size', 'status']

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id', 'userId', 'restaurant']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'userId', 'personCount', 'comment', 'name', 'phone', 'email', 'dateTime', 'langCode', 'visitDuration']

class RatesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rates
        fields = ['id', 'userId', 'comment', 'stars', 'time']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reviews
        fields = ['id', 'name', 'description', 'image_url', 'rate']

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Specialist
        fields = ['id', 'name', 'description', 'image_url', 'time', 'rate']

class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Advertising
        fields = ['id', 'name', 'description', 'image_url']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Promotion
        fields = ['id', 'position', 'date']