from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer, UserConfirmationSerializer
from django.contrib.auth import authenticate
from .models import VerificationCode
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False
    )

    confirmation = VerificationCode.objects.create(user=user)

    return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_id = serializer.validated_data.get('user_id')
    code = serializer.validated_data.get('code')

    try:
        confirmation = VerificationCode.objects.get(user_id=user_id, code=code)
    except VerificationCode.DoesNotExist:
        return Response(data={'data': 'Неверный ID пользователя или код подтверждения'},status=status.HTTP_400_BAD_REQUEST)
    user = confirmation.user
    user.is_active=True
    user.save()

    confirmation.delete()

    return Response(data={'message': 'Пользователь успешно активирован'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)



