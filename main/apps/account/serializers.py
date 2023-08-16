from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Region
from .models import User


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'guid',
            'title'
        )
        extra_kwargs = {
            'id': {'read_only': True}, 
            'guid': {'read_only': True},
        }


class UserRegistrationSerializer(serializers.ModelSerializer):   
    confirm_password = serializers.CharField(
        write_only = True,
        required = True,
        help_text = 'Enter confirm password',
        style = {'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'phone_number',
            "full_name",
            "email",
            'region',
            'is_moderator',
            'is_for_flight',
            'is_for_hotel',
            'is_for_visa',
            'is_working_with_agent',
            'is_for_finance',
            'is_manager',
            'password',
            'confirm_password'
        )    

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError({"message":"Password and confirm password don't match"}) 
        validated_data.pop('confirm_password') 
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
    

class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['guid'] = self.user.guid
        data['phone_number'] = self.user.phone_number
        data['full_name'] = self.user.full_name
        data['is_superuser'] = self.user.is_superuser
        return data
    

class UserListSerializer(serializers.ModelSerializer): 
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    region = serializers.CharField(source='region.title')
    class Meta:
        model = User
        fields = (
            'id',
            'guid',
            'phone_number',
            "full_name",
            "email",
            'region',
            'is_moderator',
            'is_for_flight',
            'is_for_hotel',
            'is_for_visa',
            'is_working_with_agent',
            'is_for_finance',
            'is_manager',
            'is_active',
            'created_at',
            'is_superuser'
        ) 


class UserUpdateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = (
            'is_moderator',
            'is_for_flight',
            'is_for_hotel',
            'is_for_visa',
            'is_working_with_agent',
            'is_for_finance',
            'is_manager',
            'is_active'
        ) 