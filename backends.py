from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class DynamicUsernameBackend(ModelBackend):
    USERNAME_FIELD: str

    def authenticate(self, request, username=None, password=None,  **kwargs):
        if username is None:
            username = kwargs.get(self.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(**{ self.USERNAME_FIELD: username })
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
