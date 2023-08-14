from django.db import models
from django.contrib.postgres.fields import JSONField

class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email_address = models.EmailField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.first_name)

class Rates(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE) 
    comment = models.CharField(max_length=150, null=True)
    stars = models.IntegerField(null=True)
    time = models.TimeField()
    image_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.userId)
    
class Reviews(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=500, null=True)
    rate = models.ManyToManyField(Rates)

    def __str__(self):
        return self.name  

class Restaurants(models.Model):
    type = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=500, null=True)
    rate = models.ManyToManyField(Rates)
    general_rate = models.IntegerField(null=True)
    location = models.CharField(max_length=50, null=True)
    api_url = models.URLField(null=True)
    template = JSONField(null=True)

    def __str__(self):
        return self.name 
    
class Barbershop(models.Model):
    type = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=500, null=True)
    rate = models.ManyToManyField(Rates)
    general_rate = models.IntegerField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name     

class Categories(models.Model):
    name = models.CharField(max_length=200, null=True)
    restaurants = models.ManyToManyField(Restaurants) 
    barbers = models.ManyToManyField(Barbershop)

    def __str__(self):
        return self.name    

class History(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    restaurant = models.ManyToManyField(Restaurants)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.date)

class Favorites(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    restaurant = models.ManyToManyField(Restaurants)

    def __str__(self):
        return str(self.userId)

class Booking(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    personCount = models.IntegerField(null=True)
    comment = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    dateTime = models.DateTimeField(null=True)
    langCode = models.CharField(max_length=10, null=True)
    visitDuration = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Reservation2(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.status)
    
class Specialist(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=500, null=True)
    time = models.TimeField()
    rate = models.ManyToManyField(Rates)

    def __str__(self):
        return self.name

class Advertising(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Promotion(models.Model):
    position = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.position)
