from django.urls import path
from .views import (
    ClientReviewListAPIView,
    ServiceListAPIView, ServiceDetailAPIView,
    ProjectListAPIView, ProjectDetailAPIView,
)

urlpatterns = [
    # ClientReview
    path('client-reviews', ClientReviewListAPIView.as_view(), name='clientreview-list'),

    # Service
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    # Project
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<slug>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]