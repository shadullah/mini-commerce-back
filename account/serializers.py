from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Account

User = get_user_model()

class RegSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password!= confirm_password:
            raise serializers.ValidationError({'error': "Password doesn't match!!"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "email already exists!!"})

        account = User(username=username, email=email,first_name=first_name, last_name=last_name )
        print(account)

        account.set_password(password)
        account.save()

        Account.objects.create(user=account)

        return account

class AllUserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model= User 
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser']

class LoginSeria(serializers.Serializer):
    username= serializers.CharField(required=True)
    password= serializers.CharField(required=True)