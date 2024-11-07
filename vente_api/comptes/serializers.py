from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from django.core.validators import FileExtensionValidator
import json



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        data['userinfo'] = {
            'id':self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
            'photo_url':self.user.photo_url.url if self.user.photo_url else None,
            
        }
        return data


class RegisterAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    photo_url = serializers.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),], required=False)

    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password', 'password2', 'role', 'photo_url')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        if 'photo_url' in attrs and attrs['photo_url'] is not None and attrs['photo_url'].size > 1024 * 1024:
            raise serializers.ValidationError(
                {"photo_url": "The file size must be less than 1 MB."})

        return attrs

    def create(self, validated_data):
        photo_url = validated_data.get('photo_url')
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            photo_url=photo_url,
    )
        user.set_password(validated_data['password'])
        user.save()
        
        return user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    photo_url = serializers.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),], required=False)
    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password', 'password2', 'role', 'photo_url','nom_client','adresse','telephone')
        
    def create(self, validated_data):
        photo_url = validated_data.get('photo_url')
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            photo_url=photo_url,
            nom_client=validated_data['nom_client'],
            adresse=validated_data['adresse'],
            telephone=validated_data['telephone'],
    )
        user.set_password(validated_data['password'])
        user.save()
        return user


    
