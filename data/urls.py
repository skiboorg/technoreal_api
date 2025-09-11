from django.urls import path
from .views import *

urlpatterns = [
    # ClientReview
    path('client-reviews', ClientReviewListAPIView.as_view(), name='clientreview-list'),

    # Service
    path('home_gallery/', HomeGalleryListAPIView.as_view(), ),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    # Project
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<slug>/', ProjectDetailAPIView.as_view(), name='project-detail'),

    path('news/', GetNews.as_view()),
    path('news/<slug>/', GetNewsItem.as_view()),
    path('form', NewForm.as_view()),
]