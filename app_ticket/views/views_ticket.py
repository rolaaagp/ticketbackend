from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Ticket
from ..serializers import TicketSerializer

from django.shortcuts import get_list_or_404


class TicketAPIView(APIView):
    def get(self, request):
        try:
            tickets = get_list_or_404(Ticket)
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'error': 'No content.'}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
