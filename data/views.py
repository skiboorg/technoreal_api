
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClientReview, Service, Project
from .serializers import *

# ===========================
# ClientReview
# ===========================
class ClientReviewListAPIView(generics.ListAPIView):
    serializer_class = ClientReviewSerializer
    queryset = ClientReview.objects.all()



# ===========================
# Service
# ===========================
class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceShortSerializer

    def get_queryset(self):

        for_index_param = self.request.GET.get('index', None)
        for_index = True if for_index_param.lower() == 'true' else False
        if for_index:
            qs = Service.objects.filter(show_on_main=True).order_by('order')
        else:
            qs = Service.objects.all().order_by('order')

        return qs

class ServiceDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'slug'


# ===========================
# Project
# ===========================
class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectShortSerializer

    def get_queryset(self):

        for_index_param = self.request.GET.get('index', None)
        for_index = True if for_index_param.lower() == 'true' else False
        if for_index:
            qs = Project.objects.filter(show_on_main=True)
        else:
            qs = Project.objects.all()

        return qs


class ProjectDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'slug'
