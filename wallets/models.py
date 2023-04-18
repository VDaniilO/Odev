from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
