from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Book

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Email no encontrado")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Contraseña incorrecta")

        if not user.is_active:
            raise serializers.ValidationError("Usuario inactivo")

        refresh = RefreshToken.for_user(user)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'user_email': user.email
        }


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'author', 'release_date']


class BookWithUserSerializer(serializers.ModelSerializer):
    registered_by_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'author', 'release_date', 'registered_by_user']
    
    def get_registered_by_user(self, obj):
        try:
            from .models import User
            user = User.objects.get(id=obj.registered_by)
            return {
                'id': user.id,
                'name': user.name,
                'email': user.email
            }
        except User.DoesNotExist:
            return None
