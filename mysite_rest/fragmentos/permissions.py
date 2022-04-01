from rest_framework import permissions

# Permiso personalizado para permitir sólo a los
# propietarios de los objectos editarlos
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        # leer permisos permitidos para cualquier request
        # por lo que siempre se permitirán request tipo
        # GET, HEAD o OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
