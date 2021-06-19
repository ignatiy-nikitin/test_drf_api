from django.urls.conf import path
from test_app.views import first_view


urlpatterns = [
    path('first/', first_view),
]
