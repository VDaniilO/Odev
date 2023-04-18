from django.urls import path
from .views import *


urlpatterns = [
    path('wallets/', WalletList.as_view()),
    path('wallets/<int:pk>/', WalletDetail.as_view()),
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
]
