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

class ProjectMiniSerializer(serializers.ModelSerializer):
    services = ProgectServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['name', 'slug', 'cover','services']


class ProjectSerializer(serializers.ModelSerializer):
    results = ProjectResultSerializer(many=True, read_only=True)
    gallery_images = ProjectGalleryImageSerializer(many=True, read_only=True)
    gallery_images1 = ProjectGalleryImageSerializer(many=True, read_only=True)
    services = ProgectServiceSerializer(many=True, read_only=True)
    others = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_others(self, obj):
        # Берём любые 2 проекта, кроме текущего
        qs = Project.objects.exclude(id=obj.id).only('name', 'slug', 'cover')[:2]
        return ProjectMiniSerializer(qs, many=True).data

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

class ServiceSliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSliderImage
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceGalleryImageSerializer(many=True, read_only=True)
    slider_images = ServiceSliderImageSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    variants = VariantSerializer(many=True, read_only=True)
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Service
        fields = "__all__"

    def get_cover(self, obj):
        qs = obj.slider_images.filter(is_main=True)
        if qs.exists():
            return qs.first().image.url


class ServiceShortSerializer(serializers.ModelSerializer):
    slider_images = ServiceSliderImageSerializer(many=True, read_only=True)
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Service
        fields = "__all__"

    def get_cover(self, obj):
        qs = obj.slider_images.filter(is_main=True)
        if qs.exists():
            return qs.first().image.url

class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = "__all__"

class HomeGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeGalleryImage
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class NewsItemShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        exclude = ['content']


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    others = serializers.SerializerMethodField()
    class Meta:
        model = NewsItem
        fields = '__all__'

    def get_others(self, obj):
        # Берём любые 2 проекта, кроме текущего
        qs = NewsItem.objects.exclude(id=obj.id).only('name', 'slug', 'created')[:2]
        return NewsItemShortSerializer(qs, many=True).data


class CallbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackForm
        fields = '__all__'

        extra_kwargs = {
            "name": {"error_messages": {"required": "Имя обязательное поле"}, 'required': True},
            'phone': {"error_messages": {"required": "Телефон обязательное поле"},'required': True},
            'file': {'required': False},
        }


class SEOPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOPage
        fields = "__all__"