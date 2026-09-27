from django.urls import path
from .views import UserView

urlpatterns = [
    path('api/users', UserView.as_view()),
    path('api/users/<int:id>', UserView.as_view()),
]
