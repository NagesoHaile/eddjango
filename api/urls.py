from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for the Profile model
    path('member/profile/', views.ProfileListCreateView.as_view(), name='member-list'),
    path('member/profile/<int:pk>/',
         views.ProfileDetailView.as_view(), name='member-detail'),

    # URL patterns for the Profile model
    # path('member/profile/', views.MemberListCreateView.as_view(), name='member-list'),
    # path('member/profile/<int:pk>/',
    #      views.MemberDetailView.as_view(), name='member-detail'),



    # Repeat the process for each model's URL patterns
]
