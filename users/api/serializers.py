from rest_framework import serializers
from users.models import User


class UserSerliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'is_active',
            'is_staff',
            ]
