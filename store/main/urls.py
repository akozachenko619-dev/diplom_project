
from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name='about'),
    path("delivery_payment/", views.delivery_payment, name="delivery_payment"),
    path("contact_information/", views.contact_information, name="contact_information"),
    path("catalog/", include("goods.urls", namespace="catalog")),
    ]