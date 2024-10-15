


from django.urls import path
from .views import ResponseAPIView

urlpatterns = [
    path('response/', ResponseAPIView.as_view(), name='response'),
]