import datetime

from django.db.models import Prefetch, Q, ExpressionWrapper, IntegerField, F, Func
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from books.models import Book
from orders.models import Order, OrderItem
from orders.serializer import OrderSerializer
from users.models import UserModel
from utils.amount_calc import get_due_amount


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        order_items = request.data.get('order_items')
        mode_of_payment = request.data.get('mode')
        customer_id = request.data.get('customer_id')
        customer = get_object_or_404(UserModel, pk=customer_id)
        order = Order.objects.create(mode_of_payment=mode_of_payment, customer=customer)
        order.save()

        for order_item in order_items:
            book = Book.objects.get(id=order_item["id"])
            order.order_items.add(book)

        order.save()
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def overdue_books(self, request, pk=None):
        customer = get_object_or_404(UserModel, pk=pk)
        today = datetime.date.today()
        orders = Order.objects.prefetch_related('order_items').filter(due_date__lt=today,customer=customer,returned = False).annotate(
            fine=ExpressionWrapper(F('due_date') - today, output_field=IntegerField())
        ).annotate(fine=F('fine'))
        due_orders = []
        for o in orders:
            due_order = {"id": o.id,"issued_date": o.ordered_at, "due_date": o.due_date, "due_amount": get_due_amount(o.fine),
                         "books": [b.name for b in o.order_items.all()],
                         "mode_of_payment": o.mode_of_payment}
            due_orders.append(due_order)
        return Response(due_orders, status=status.HTTP_200_OK)
