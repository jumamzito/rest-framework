from core.serializers import CurrencySerializer
from django.shortcuts import render
from .serializers import *
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, IsAuthenticated



from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CurrencyListAPIView(ListAPIView):
    queryset= Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class=CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)

class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend)
    search_fields = ("description",)
    ordering_fields = ("amount","date")
    filterset_fields = ("currency__code",)

    def get_queryset(self):
        return Transaction.objects.select_related("currency","category","user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list","retrieve"):
            return ReadTransactionSerializer

        return WriteTransactionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)