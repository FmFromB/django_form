from django.urls import path
from .views import *

urlpatterns = [
    path('', FormRegView.as_view(), name = "register_page"),
    path('final', FinalView.as_view(), name = "final"),
]

