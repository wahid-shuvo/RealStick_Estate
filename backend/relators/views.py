from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Relator
from .serializers import RelatorSerializer


class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Relator.objects.all()
    serializer_class = RelatorSerializer
    pagination_class = None


class RealtorView(RetrieveAPIView):
    queryset = Relator.objects.all()
    serializer_class = RelatorSerializer


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Relator.objects.filter(top_seller=True)
    serializer_class = RelatorSerializer
    pagination_class = None
