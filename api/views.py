from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
# Generic views for the Profile Model


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

# Generic views for the MemberFamily Model


class MemberFamilyListCreateView(generics.ListCreateAPIView):
    queryset = models.MemberFamily.objects.all()
    serializer_class = serializers.MemberFamilySerializer


class MemberFamilyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MemberFamily.objects.all()
    serializer_class = serializers.MemberFamilySerializer

# Generic views for the Event Model


@permission_classes([IsAdminUser])
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer


# Generic views for the Contribution Model
class ContributionListCreateView(generics.ListCreateAPIView):
    queryset = models.Contribution.objects.all()
    serializer_class = serializers.ContributionSerializer


class ContributionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contribution.objects.all()
    serializer_class = serializers.ContributionSerializer
