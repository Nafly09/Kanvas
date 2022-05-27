from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, _):
        if request.method == "POST":
            return True

        return bool(request.user.is_authenticated and request.user.is_admin)
