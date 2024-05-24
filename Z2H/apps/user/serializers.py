from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers
from .models import RegisterUser, Z2HUser, Role, Z2HCustomers
from apps.app.models import Z2HPlanDetails
import os

PRIMARY_LEG_COUNT = int(os.environ.get('PRIMARY_LEG_COUNT'))
SECONDARY_LEG_COUNT = PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT
TERTIARY_LEG_COUNT = SECONDARY_LEG_COUNT * PRIMARY_LEG_COUNT
QUATERNARY_LEG_COUNT = TERTIARY_LEG_COUNT * PRIMARY_LEG_COUNT

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
    system_email = serializers.SerializerMethodField()
    system_role = serializers.SerializerMethodField()

    class Meta:
        model = RegisterUser
        fields = "__all__"

    def get_system_email(self, obj):
        return Z2HUser.objects.get(id=obj.user_id).email
    
    def get_system_role(self, obj):
        return Role.objects.get(id=obj.role_id).name

    def create(self, validated_data):
        request = self.context.get('request', None)
        request_data = request.data if request else None
        if request and request_data['accessed_from'] == 'web':
            email = request_data['user_email']
        else:
            email = str(validated_data['mobile_number']) + "@z2h.com"
        validated_data['user'] = Z2HUser.objects.filter(email=email).first()
        return super().create(validated_data)
    
class UpdateRegisterUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = [
            'address', 'marital_status', 'pan', 'aadhar_number', 'district', 'city', 'town', 'address', 'pin_code',
            'name_of_bank', 'name_as_in_bank', 'ifsc_code', 'bank_branch', 'account_number', 'alternate_mobile_number'
        ]
    
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    date_of_birth = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    mobile_number = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()
    level_one_count = serializers.SerializerMethodField()
    level_two_count = serializers.SerializerMethodField()
    level_three_count = serializers.SerializerMethodField()
    level_four_count = serializers.SerializerMethodField()
    plan_start_date = serializers.SerializerMethodField()

    class Meta:
        model = Z2HCustomers
        fields = '__all__'
    
    def get_date_of_birth(self, obj):
        return RegisterUser.objects.get(user_id=obj.user_id).date_of_birth
    
    def get_gender(self, obj):
        return RegisterUser.objects.get(user_id=obj.user_id).gender
    
    def get_mobile_number(self, obj):
        return RegisterUser.objects.get(user_id=obj.user_id).mobile_number
    
    def get_email_address(self, obj):
        return RegisterUser.objects.get(user_id=obj.user_id).email_address
    
    def get_plan(self, obj):
        return Z2HPlanDetails.objects.filter(uid=obj.active_plan_uid).first().name
    
    def get_plan_start_date(self, obj):
        return str(obj.plan_start_date).split(" ")[0]
    
    def get_level_one_count(self, obj):
        count = Z2HCustomers.objects.filter(referrer=obj).count()
        return f"{count} / {PRIMARY_LEG_COUNT}"
    
    def get_level_two_count(self, obj):
        count = 0
        customers = Z2HCustomers.objects.filter(referrer=obj)
        for customer in customers:
            count += Z2HCustomers.objects.filter(referrer=customer).count()

        return f"{count} / {SECONDARY_LEG_COUNT}"
    
    def get_level_three_count(self, obj):
        count = 0
        customers = Z2HCustomers.objects.filter(referrer=obj)
        for first_level_customer in customers:
            customers_next_level = Z2HCustomers.objects.filter(referrer=first_level_customer)
            for customer in customers_next_level:
                count += Z2HCustomers.objects.filter(referrer=customer).count()

        return f"{count} / {TERTIARY_LEG_COUNT}"
    
    def get_level_four_count(self, obj):
        count = 0
        customers = Z2HCustomers.objects.filter(referrer=obj)
        for first_level_customer in customers:
            customers_next_level = Z2HCustomers.objects.filter(referrer=first_level_customer)
            for second_level_customer in customers_next_level:
                customers_next_level = Z2HCustomers.objects.filter(referrer=second_level_customer)
                for customer in customers_next_level:
                    count += Z2HCustomers.objects.filter(referrer=customer).count()

        return f"{count} / {QUATERNARY_LEG_COUNT}"
    