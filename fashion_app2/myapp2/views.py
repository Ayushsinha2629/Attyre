from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer
from .pagination import VideoCursorPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.

class ResponseAPIView(ListAPIView):
    serializer_class = VideoSerializer
    pagination_class = VideoCursorPagination

    def get_queryset(self):
        return Video.objects.select_related('user', 'music').prefetch_related(
            'products__store',
            'products__variants'
        ).order_by('-created_at')


# Caching can be implemented to reduce database load and improve response time for large number of users.

    # this will cache the data for 15 minutes

    
    # @method_decorator(cache_page(60*15))  
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
