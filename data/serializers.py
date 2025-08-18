from rest_framework import serializers
from .models import *

class ProjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectResult
        fields = "__all__"

class ProjectGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGalleryImage
        fields = "__all__"

class ProgectServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    results = ProjectResultSerializer(many=True, read_only=True)
    gallery_images = ProjectGalleryImageSerializer(many=True, read_only=True)
    services = ProgectServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"



class ProjectShortSerializer(serializers.ModelSerializer):
    gallery_images = ProjectGalleryImageSerializer(many=True, read_only=True)
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"

class VariantOptionSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = VariantOption
        fields = "__all__"

class VariantSerializer(serializers.ModelSerializer):
    options = VariantOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = "__all__"

class ServiceGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGalleryImage
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceGalleryImageSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = "__all__"

class ServiceShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"
class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = "__all__"
