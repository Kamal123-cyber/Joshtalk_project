from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = UserAccount.objects.filter(email=email).first()
        if user and user.check_password(password):
            tokens = RefreshToken.for_user(user)
            return {
                'refresh': str(tokens),
                'access': str(tokens.access_token),
                'email': user.email,
                'username': user.username,
            }
        raise serializers.ValidationError("Invalid credentials")



from rest_framework import serializers
from .models import UserAccount

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'first_name', 'last_name', 'mobile', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserAccount.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            mobile=validated_data.get('mobile', '')
        )
        return user
