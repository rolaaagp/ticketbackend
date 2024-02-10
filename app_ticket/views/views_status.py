from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Status
from ..serializers import StatusSerializer

from django.shortcuts import get_list_or_404


class StatusAPIView(APIView):
    def get(self, request):
        try:
            status = get_list_or_404(Status)
            serializer = StatusSerializer(status, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'error': 'No content.'}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
