from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSz
from django.contrib.auth import get_user_model
from .utils import generate_access_token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from pf_manager.validator import Validator


@api_view(['GET'])
def profile(request):
    import ipdb; ipdb.set_trace()
    user=request.user
    print(user)
    serialized_user = UserSz(user)
    return Response({'user': serialized_user.data})

@api_view(['POST'])
def signup(request):
    data = request.data
    Validator.validate_kwargs(data, ['username', 'email', 'password'])
    user_model = get_user_model()
    user_model.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
    return Response({'message': 'User created'})

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    User = get_user_model()
    username = request.data.get("username")
    password = request.data.get("password")
    response=Response()
    if (username is None) or (password is None):
        response.status_code=400
        response.data={'error':'Please provide both username and password'}
        return response
    user = User.objects.filter(username=username).first()
    if not user:
        response.status_code=404
        response.data={'error':'User not found'}
        return response
    if not user.check_password(password):
        response.status_code=400
        response.data={'error':'Invalid credentials'}
        return response

    serialized_user = UserSz(user).data
    access_token = generate_access_token(user)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response
