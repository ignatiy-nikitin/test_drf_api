from django.urls.conf import path
from test_app.views import FirstApiView, first_view
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('first/', first_view),
    path('second/', FirstApiView.as_view()),
]
