from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from manager.models import Chef

class ChefBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            chef = Chef.objects.get(chefemail=username)
            if check_password(password, chef.chefpassword):
                return chef
        except Chef.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Chef.objects.get(pk=user_id)
        except Chef.DoesNotExist:
            return None