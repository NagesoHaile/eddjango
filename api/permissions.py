
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the request method is safe (GET, HEAD, or OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is an admin
        return request.user and request.user.is_staff
