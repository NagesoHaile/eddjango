from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

admin_user_id = User.objects.get(username='admin').id


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    birth_date = models.DateField()
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True)
    member = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of {self.member.username}"


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    sub_city = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)


class MemberFamily(models.Model):
    id = models.AutoField(primary_key=True)
    relationship = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    member = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contribution(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contribution_date = models.DateTimeField(
        default=timezone.now)

    member = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contribution #{self.contribution_id}"


# Event Model
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    notification_title = models.CharField(max_length=100)
    notification_description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    member = models.ForeignKey(
        User, on_delete=models.CASCADE, default=admin_user_id)

    def __str__(self):
        return self.notification_title
