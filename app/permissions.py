from rest_framework import permissions

# not set by default so creating custom one:
class OwnershipCheck(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `specific` attribute:
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute among these options:
        owner = getattr(obj, 'user', None) or getattr(obj, 'author', None)
        return owner == request.user