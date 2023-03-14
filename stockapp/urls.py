from django.urls import path

from stockapp import views

urlpatterns =[
    path('', views.home, name='home'),
    path('log', views.log, name='log'),
    path('cust_reg',views.cust_reg,name='cust_reg'),
    path('admin1', views.admin1, name='admin1'),
    path('customer', views.customer, name='customer'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('view_stock', views.view_stock, name='view_stock'),
    path('view_user_stock', views.view_user_stock, name='view_user_stock'),
    path('stock_update/<int:id>/',views.stock_update,name='stock_update'),
    path('stock_delete/<int:id>/',views.stock_delete,name='stock_delete'),
    path('view_customer', views.view_customer, name='view_customer'),
    path('logout_customer', views.logout_customer, name='logout_customer'),
    path('logout_admin', views.logout_admin, name='logout_admin'),









]
