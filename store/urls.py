from django.urls import path  # type: ignore
from . import views

urlpatterns=[
    path('',views.store ,name="store"),
    path('cart/',views.cart ,name="cart"),
    path('checkout/',views.checkout ,name="checkout"),

    path('update_item/',views.updateItem ,name="updateItem"),
    path('process_order/',views.processOrder ,name="process_order"),
]