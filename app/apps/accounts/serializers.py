from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from ..erp_data.models import Counterparty


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSignupSerializer(serializers.ModelSerializer):
    login = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="Пользователь с таким УНП уже существует.",
        )],
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="Пользователь с такой почтой уже существует.",
        )],
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('login', 'password', 'email')

    def validate(self, data):
        if not Counterparty.objects.filter(counterparty_inn=data['login']):
            raise serializers.ValidationError({'login': 'УНП не найден.'})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            login=validated_data['login'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
