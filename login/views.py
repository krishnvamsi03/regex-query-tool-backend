from .models import userDetails, languageSC, regex, savedRegex, authToken
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, SignUpSerializer, GetSavedRegexSerializer, GetUserName, AuthTokenSerializer, SaveRegexSerializer, DeleteRegexSerializer


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
            token = authToken.objects.filter(
                key=request.data['token']).first()
            if token:
                user = userDetails.objects.filter(
                    userId=token.user.userId).first()
                savedRegexs = savedRegex.objects.all().filter(
                    userId=user.userId)
                regexList = []
                if savedRegexs is not None:
                    for regexid in savedRegexs:
                        temp = {}
                        fetchedRegex = regex.objects.filter(
                            regexId=regexid.regexId_id).first()
                        temp['id'] = regexid.savedRegexId
                        temp['regexname'] = fetchedRegex.regexName
                        temp['regexpattern'] = fetchedRegex.regexPattern
                        regexList.append(temp)
                data["list"] = regexList
        return Response(data)


@api_view(["POST", ])
def delete_saved_regex(request):
    if request.method == "POST":
        serializer = DeleteRegexSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            token = authToken.objects.filter(key=request.data['token']).first()
            if token:
                user = userDetails.objects.filter(userId=token.user.userId)
                if user:
                    saveregex = savedRegex.objects.filter(
                        savedRegexId=request.data['savedRegexId']).first()
                    if saveregex:
                        regexValue = regex.objects.filter(
                            regexId=saveregex.regexId.regexId).first()
                        saveregex.delete()
                        regexValue.delete()
                        data['response'] = "Deleted successfully"
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


@api_view(["POST", ])
def save_regex_view(request):
    if request.method == "POST":
        serializer = SaveRegexSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            token = authToken.objects.filter(
                key=request.data['token']).first()
            if token:
                user = userDetails.objects.filter(
                    userId=token.user.userId).first()
                lang = languageSC.objects.filter(
                    languageName=request.data['regexLanguage']).first()
                if user and lang:
                    regexValue = regex(
                        regexName=request.data['regexName'], regexPattern=request.data['regexPattern'], regexLanguage=lang)
                    try:
                        regexValue.save()
                        save = savedRegex(userId=user,
                                          regexId=regexValue)
                        save.save()
                        data["response"] = "Saved successfully"
                    except:
                        regexValue.delete()
                        data["response"] = "Something went wrong! please try again"
        else:
            data["response"] = "Something went wrong! please try again"
        return Response(data)
