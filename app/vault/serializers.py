from rest_framework import serializers
from vault.models import User, Password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PasswordSerializer(serializers.ModelSerializer):
    url = serializers.CharField(max_length=800)

    class Meta:
        model = Password
        fields = ('url', 'password', "user")

