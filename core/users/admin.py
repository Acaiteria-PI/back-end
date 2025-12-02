# core/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["-date_joined"]
    list_display = ("email", "name", "registration", "is_management", "is_staff", "is_active")
    list_filter = ("is_management", "is_staff", "is_active", "establishment")
    search_fields = ("email", "name", "registration")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Informações pessoais"), {"fields": ("name", "registration", "establishment")}),
        (_("Permissões"), {"fields": ("is_active", "is_staff", "is_superuser", "is_management", "groups", "user_permissions")}),
        (_("Datas importantes"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "registration", "establishment", "password1", "password2", "is_active", "is_staff", "is_superuser", "is_management"),
        }),
    )

    # Campo usado como identificador
    add_form_template = None
    filter_horizontal = ("groups", "user_permissions")


