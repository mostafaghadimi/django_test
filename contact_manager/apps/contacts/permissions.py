from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):

        # Instance must have an attribute named `id`.
        return obj.id == request.user.id