from rest_framework import serializers

from .models import Profile, Contribution, MemberFamily, Notification


# Serializer for the Profile Model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# Serializer for the Contribution Model


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

# Serializer for the MemberFamily Model


class MemberFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberFamily
        fields = '__all__'

# Serializer for the Notification Model


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
