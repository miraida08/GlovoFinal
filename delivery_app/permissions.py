from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CheckProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.store.owner:
            return True
        return False

