import random
from core.models import *
from django.utils import timezone
from decimal import Decimal

txs = []

currencies = list(Currency.objects.all())
categories = list(Category.objects.all())

for i in range(1000):
    tx=Transaction(amount=random.randrange(Decimal(1),Decimal(1000)),currency=random.choice(currencies),description="",date=timezone.now()-timezone.timedelta(days=random.randint(1,365)),category=random.choice(categories))
    txs.append(tx)

len(txs)
