from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read only permissions are allowed for any requests
        # SAFE_METHODS = GET, OPTIONS, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
