from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://api.abacatepay.com/v1/pixQrCode/create'
API_KEY = os.getenv('ABACATEPAY_API_KEY')

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_pix(request):
    order = request.data
    total_amount = int(float(order.get('total_amount')) * 100)
    payload = {
        "amount": total_amount,
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, json=payload, headers=headers)
    return Response(response.json())