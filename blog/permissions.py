from rest_framework import permissions
class CustomTokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET and POST requests, deny others
        return request.method in ['GET', 'POST']
