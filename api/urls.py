from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for the Profile model
    path('member/profile/', views.ProfileListCreateView.as_view(), name='member-list'),
    path('member/profile/<int:pk>/',
         views.ProfileDetailView.as_view(), name='member-detail'),
    path('notifications/', views.NotificationListView.as_view(),
         name='notification-list'),
    path('notifications/<int:pk>/',
         views.NotificationDetailView.as_view(), name='-list'),
    path('post/<int:pk>/',
         views.ProfileDetailView.as_view(), name='member-detail'),
]
