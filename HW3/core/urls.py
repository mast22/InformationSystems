from django.contrib import admin
from django.urls import path
from .views import HomePageView, OrderView, OrderDetailView, OrderListView, AccountantBaseView, AccountantOrderListView, AccountantOrderDetailView

app_name = 'core'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # client interface
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('create-order/', OrderView.as_view(), name='order'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),

    # accountant interface
    path('accountant/', AccountantBaseView.as_view(), name='acc-base'),
    path('accountant/orders/', AccountantOrderListView.as_view(),
         name='acc-oreder-list'),
    path('accountant/order/<int:pk>/',
         AccountantOrderDetailView.as_view(), name='acc-order-detail'),

]
