from rest_framework.permissions import BasePermission, SAFE_METHODS

class EventUserWritePermiss(BasePermission):
    message ='Editing Event is restrected to the user only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.EventCreator == request.user

class IsLoggedInUserOrAdmin(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff