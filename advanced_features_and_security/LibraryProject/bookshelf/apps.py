from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)

def create_groups_and_permissions(sender, **kwargs):
    from .models import Book

    # Permissions
    perms = Permission.objects.filter(content_type__app_label='bookshelf', codename__in=[
        'can_view', 'can_create', 'can_edit', 'can_delete'
    ])

    # Groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    # Assign permissions
    editors.permissions.set(perms.filter(codename__in=['can_create', 'can_edit']))
    viewers.permissions.set(perms.filter(codename='can_view'))
    admins.permissions.set(perms)  # all permissions
