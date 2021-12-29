from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import mydb
from .serializer import mydbserializer

@api_view(['GET'])
def Dlist(request):
    all_data = mydb.objects.all()
    data = mydbserializer(all_data, many=True).data
    return Response({'data': data})

class Dhtviews(generics.CreateAPIView):
    queryset = mydb.objects.all().order_by('id') #convert arduino data to json file
    serializer_class = mydbserializer    