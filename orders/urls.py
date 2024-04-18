from django.urls import path

from orders import views

urlpatterns = [
    path('/list/', views.OrderList.as_view(), name='order_list'),
    path('/detail/{pk}', views.OrderDetail.as_view(), name='order_detail'),
]