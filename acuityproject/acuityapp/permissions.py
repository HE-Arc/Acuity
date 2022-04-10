from pickle import FALSE
from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return view.action in ['best_users', 'worst_users']