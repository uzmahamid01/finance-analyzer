from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .models import Transaction
from datetime import datetime
import csv
from transactions.models import Transaction
from transactions.utils import categorize_transaction
from django.db.models import Sum
from django.db.models.functions import TruncMonth

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_csv(request):
    csv_file = request.FILES.get('file')
    if not csv_file:
        return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            description = row['description']
            category = categorize_transaction(description)  # Auto-categorize here

            Transaction.objects.create(
                date=datetime.strptime(str(row['date']), "%Y-%m-%d").date(),
                description=description,
                amount=float(row['amount']),
                category=category,
                notes=row.get('notes', None)
            )
        return Response({"message": "CSV uploaded and transactions created"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def monthly_summary(request):
    data = (
        Transaction.objects
        .annotate(month=TruncMonth('date'))  # annotate month correctly
        .values('month', 'category')         # select month and category fields
        .annotate(total=Sum('amount'))       # sum amount grouped by month and category
        .order_by('month', 'category')
    )

    # Convert date objects to ISO strings to avoid frontend Date parsing issues
    summary = [
        {
            "month": entry['month'].strftime('%Y-%m-%d'),  # keep day for safe parsing
            "category": entry['category'],
            "total": float(entry['total'])
        }
        for entry in data
    ]

    return Response(summary)
