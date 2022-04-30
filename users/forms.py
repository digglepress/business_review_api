from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdminChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
