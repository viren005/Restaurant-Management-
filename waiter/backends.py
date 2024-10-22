from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from manager.models import Waiter

class WaiterBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            waiter = Waiter.objects.get(waiteremail=username)
            if check_password(password, waiter.waiterpassword):
                return waiter
        except Waiter.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Waiter.objects.get(pk=user_id)
        except Waiter.DoesNotExist:
            return None