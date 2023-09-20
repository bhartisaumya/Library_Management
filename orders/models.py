from django.db import models

from books.models import Book
from users.models import UserModel


# Create your models here.
class Order(models.Model):
    class PaymentMode(models.TextChoices):
        UPI = "UPI", "UPI"
        CASH = "By Cash", "CASH"
        CARD = "Card Payment", "CARD"

    order_items = models.ManyToManyField(Book)
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    ordered_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=False, blank=False)
    mode_of_payment = models.CharField(choices=PaymentMode.choices, default=PaymentMode.CASH, max_length=200)
    returned = models.BooleanField(null= False, blank=False, default=False)

    def __str__(self):
        return self.customer.name + " " + str(self.ordered_at)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
