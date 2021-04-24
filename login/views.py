from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, SignUpSerializer, GetSavedRegexSerializer, GetUserName, AuthTokenSerializer
from .models import userDetails, language, regex, savedRegex, authToken

# Create your views here.
# class LoginView(viewsets.ModelViewSet):
#     serializer_class = LoginSerializer
#     queryset = userDetails.objects.all()
@api_view(['POST', ])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = userDetails.objects.filter(username=serializer.data.get(
                'username'), passward=serializer.data.get('passward')).first()
            if user is not None:
                token = authToken.objects.filter(user=user).first()
                if token:
                    data['token'] = token.key
                    data['response'] = "valid user"
                else:
                    data['response'] = "wrong username or password"
            else:
                data['response'] = "wrong password or username"
        return Response(data)


@api_view(['POST', ])
def signup_view(request):
    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            try:
                token = authToken(user=user)
                token.save()
                data['token'] = token.key
            except:
                data = serializer.delete()
                
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
def get_saved_regex_view(request):
    if request.method == "POST":
        serializer = GetSavedRegexSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            savedRegexs = savedRegex.objects.all().filter(
                userId=serializer.data.get('userId'))
            if savedRegexs is not None:
                for regexid in savedRegexs:
                    fetchedRegex = regex.objects.filter(
                        regexId=regexid.regexId_id).first()
                    data['regexname'] = fetchedRegex.regexName
                    data['regexpattern'] = fetchedRegex.regexPattern
        return Response(data)


@api_view(['POST', ])
def get_username_view(request):
    if request.method == "POST":
        serializer = GetUserName(data=request.data)
        data = {}
        if serializer.is_valid():
            username = userDetails.objects.filter(
                username=serializer.data.get('username')).first()
            if username is not None:
                data['message'] = "username already taken"
                data['taken'] = True
            else:
                data['message'] = "Good to go"
                data['taken'] = False
        return Response(data)
