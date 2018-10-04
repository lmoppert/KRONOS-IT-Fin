from django.contrib.auth import views as auth_views
from django.urls import path
from contracts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('contract/<int:pk>/', views.ContractView.as_view(), name='contract'),
    path('invoice/<int:pk>/', views.InvoiceView.as_view(), name='invoice'),
    path('contract/', views.ContractList.as_view(), name='contract_list'),
    path('invoice/', views.InvoiceList.as_view(), name='invoice_list'),
]
