from rest_framework import permissions

# not set by default so creating custom one:
class OwnershipCheck(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `specific` attribute:
    """

    def has_object_permission(self, request, view, obj):                       #here has_object permsiision is for single object not for entire systme
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:       #hre you can read
            return True

        # Instance must have an attribute among these options:
        owner = getattr(obj, 'user', None) or getattr(obj, 'author', None)           #else you can write
        return owner == request.user
    
    
    
# This code checks who owns something (like a post or profile) before letting them change it.

# Anyone can see it (GET, HEAD, OPTIONS).
# To edit, the owner must match the logged-in user.
# It checks if the owner is in obj.user or obj.author.
# If yes, editing is allowed. If not, editing is denied.