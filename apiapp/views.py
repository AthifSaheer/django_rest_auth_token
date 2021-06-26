from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegister
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class registration(APIView):
    def post(self, request, format=None):
        serializer = UserRegister(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registered'
            data['username'] = account.username
            data['email'] = account.email
            token, create = Token.objects.get_or_create(user=account)
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)
