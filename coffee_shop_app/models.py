from django.db import models

class Inventory(models.Model):# Tablle for coffee items
    # Coffee_type, quantity, price, discripsion, image
    Coffee_type = models.CharField(max_length=220)
    quantity = models.PositiveBigIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    discripsion = models.TextField()
    image = models.CharField( max_length=5000000)

    def __str__(self):
        return self.Coffee_type

class Sales_Data(models.Model):
    menu_items = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField(default=0)
    price = models.IntegerField(null=True)
    Total_Price = models.IntegerField(null=True)

class Contact(models.Model):
    name=models.CharField( max_length=100)
    Email=models.CharField( max_length=254)
    phone=models.IntegerField(default=0)
    state=models.CharField(max_length=70)
    city=models.CharField( max_length=100)
    message=models.CharField( max_length=5000000000)
    date=models.DateField(null=True)

    def __str__(self):
        return self.name
class Bookings (models.Model):
    name=models.CharField(max_length=100)
    number=models.IntegerField(default=0)
    No_of_people=models.IntegerField(default=0)
    date=models.DateField(null=True)

    def __str__(self):
        return self.name
    