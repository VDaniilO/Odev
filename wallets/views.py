from rest_framework import generics
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionCreateView(APIView):
    serializer_class = TransactionSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            sender = serializer.validated_data['sender']
            receiver = serializer.validated_data['receiver']
            amount = serializer.validated_data['amount']

            if sender.balance < amount:
                return Response({'error': 'Not enough funds'}, status=status.HTTP_400_BAD_REQUEST)

            sender.balance -= amount
            sender.save()

            receiver.balance += amount
            receiver.save()

            transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)

            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
