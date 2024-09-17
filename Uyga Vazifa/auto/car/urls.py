from django.urls import path
from .views import CarRetrieveApiView, CarApiView

urlpatterns = [
    path('api/v1/', CarApiView.as_view()),
    path('api/v1/<int:pk>/', CarRetrieveApiView.as_view()),
]