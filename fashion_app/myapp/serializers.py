from rest_framework import serializers
from .models import User, Store, Variant, Product, Music, Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'username', 'display_name', 'profile_picture_url', 'bio', 'followers_count', 'verified' ]

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'logo_url']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'name', 'options']

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = [ 'id', 'name', 'price', 'original_price', 'discount_percentage', 'image_url', 'timestamp', 'currency', 'store', 'in_stock', 'variants' ]

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'name', 'artist', 'cover_url']


class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductSerializer(many=True)
    music = MusicSerializer()
    hashtags = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Video
        fields = ['id', 'video_url', 'thumbnail_url', 'description', 'view_count', 'duration', 'created_at', 'user', 'products', 'likes_count', 'comments_count', 'shares_count', 'is_liked', 'is_bookmarked', 'music', 'hashtags',
        ]

class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    total_videos = serializers.IntegerField()
    next_cursor = serializers.CharField(allow_null=True, required=False)

class ResponseSerializer(serializers.Serializer):
    videos = VideoSerializer(many=True)
    pagination = PaginationSerializer()