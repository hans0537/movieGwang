from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model=User
      fields=('id','username','email','profile','background','cho_points','groups','user_permissions','followings')