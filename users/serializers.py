from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password"]
        
        
class  MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token["email"] = user.email
        token["avatar"] = user.avatar.url
        token["is_staff"] = user.isStaff
        
        return token