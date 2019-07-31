from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'avatar'
                                             'facebook_id', 'created_at', 'updated_at')


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    expired_time = serializers.DateTimeField()
    user = UserSerializer(read_only=True)
