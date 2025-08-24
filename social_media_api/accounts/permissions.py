from rest_framework import permissions

class CanEditPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.has_perm("accounts.can_edit")


class CanCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.has_perm("accounts.can_create")
