from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostOrIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('POST'):
            return True

        return request.user and request.user.is_authenticated

