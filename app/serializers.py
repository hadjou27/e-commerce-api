from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password','first_name','last_name','birthday']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user






        
        