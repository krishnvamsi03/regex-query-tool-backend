from rest_framework import serializers
from .models import userDetails, savedRegex, regex, language, authToken
import uuid


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ('username', 'passward')
        extra_kwargs: {
            'passward': {'write_only': True}
        }


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = authToken
        fields = ('keys', 'user')

    def save(self,):
        token = authToken(user=self.validated_data['userId'])
        token.save()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ('username', 'email', 'passward', 'isUserVerified')
        extra_kwargs: {
            'password': {'write_only': True},
            'confirmPassword': {'write_only': True}
        }

        def save(self):
            user = userDetails(username=self.validated_data['username'],
                               email=self.validated_data['email'],
                               isUserVerified=self.validate_data['isUserVerified'])
            password1 = self.validated_data['password']
            password2 = self.validated_data['confirmPassword']
            if password1 != password2:
                raise serializers.ValidationError(
                    {'password': 'Password must match'})
            user.set_passward(password1)
            user.save()
            return user

        def delete(self):
            user = userDetails(
                username=self.validate_data['username'], passward=self.validated_data['password'])
            data = {}
            if user is not None:
                user.delete()
            data['Response'] = 'Successfully Rolledback'
            return data


class GetSavedRegexSerializer(serializers.ModelSerializer):
    class Meta:
        model = savedRegex
        fields = ('userId', 'regexId')


class GetUserName(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ('username',)
