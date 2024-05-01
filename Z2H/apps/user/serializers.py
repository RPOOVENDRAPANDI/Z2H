from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers
from .models import RegisterUser, Z2HUser, Role


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
class UserListSerializer(serializers.ModelSerializer):
    mobile_number = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model()
        fields = ['name', 'uid', 'mobile_number']

    def get_mobile_number(self, obj):
        return obj.user.email.split("@")[0]
    
    def get_name(self, obj):
        return obj.user.name
    
class AuthTokenSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get('mobile_number') + "@z2h.com"
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
class WebAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        return attrs
    
class UserPasswordUpdateSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )
    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = "__all__"

    def create(self, validated_data):
        email = str(validated_data['mobile_number']) + "@z2h.com"
        validated_data['user'] = Z2HUser.objects.filter(email=email).first()
        return super().create(validated_data)
    
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'