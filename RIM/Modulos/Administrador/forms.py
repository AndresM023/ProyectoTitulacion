from django import forms
from django.contrib.auth.hashers import make_password

from Modulos.Administrador.models import Usuario, Roles, Permisos


# Formulario para el modelo de Usuario Personalizado
class CustomUserForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)  # Campo de contraseña con widget de input de tipo password

    class Meta:
        model = Usuario
        fields = ['usuario', 'email', 'contrasena', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Cifrar la contraseña si es un nuevo usuario
        user.contrasena = make_password(self.cleaned_data['contrasena'])
        if commit:
            user.save()
        return user


# Formulario para el modelo de Rol
class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['nombre', 'permisos', 'descripcion']


# Formulario para el modelo de Permiso
class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permisos
        fields = ['nombre', 'descripcion']
