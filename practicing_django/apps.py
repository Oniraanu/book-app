from django.contrib.admin.apps import AdminConfig


class BookAdminConfig(AdminConfig):
    default_site = "practicing_django.admin.BookBoutAdmin"
