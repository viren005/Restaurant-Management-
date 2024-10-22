from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from adminside.models import Manager

class ManagerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            manager = Manager.objects.get(managername=username)
            if check_password(password, manager.managerpassword):
                return manager
        except Manager.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Manager.objects.get(pk=user_id)
        except Manager.DoesNotExist:
            return None