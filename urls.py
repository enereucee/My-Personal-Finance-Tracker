from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import UserActivityViewSet
from . import views


router = DefaultRouter()
router.register(r'user-activities', UserActivityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('log/', views.log_user_activity, name='log-user-activity'),
    path('summary/', views.activity_summary, name='activity-summary'),  # Add this line for the summary view
]