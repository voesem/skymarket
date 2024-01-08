from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True

        return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.filter(name='admin').exists()
