from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import ResponseSerializer, VideoSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class ResponseAPIView(APIView):
    def get(self, request, format=None):
        # Get pagination parameters
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)

        try:
            page = int(page)
            limit = int(limit)
        except ValueError:
            return Response({'error': 'Invalid pagination parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch videos ordered by creation date (newest first)
        videos_queryset = Video.objects.select_related('user', 'music').prefetch_related(
            'products__store',
            'products__variants'
        ).order_by('-created_at')

        paginator = Paginator(videos_queryset, limit)
        total_videos = videos_queryset.count()
        total_pages = paginator.num_pages

        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
            page = 1
        except EmptyPage:
            videos = []
        
        # Serialize videos
        video_serializer = VideoSerializer(videos, many=True)

        # Determine next_cursor (for simplicity, using page number)
        if page < total_pages:
            next_cursor = page + 1
        else:
            next_cursor = None

        # Prepare pagination data
        pagination_data = {
            'page': page,
            'limit': limit,
            'total_pages': total_pages,
            'total_videos': total_videos,
            'next_cursor': next_cursor,
        }

        # Prepare the final response
        response_data = {
            'videos': video_serializer.data,
            'pagination': pagination_data,
        }

        # Serialize the entire response
        response_serializer = ResponseSerializer(response_data)

        return Response(response_serializer.data, status=status.HTTP_200_OK)