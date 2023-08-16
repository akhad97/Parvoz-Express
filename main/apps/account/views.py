from rest_framework import generics
from rest_framework_simplejwt import authentication
from .models import Region
from .serializers import RegionSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserListSerializer,
    UserUpdateSerializer
)
from .models import User

User = get_user_model()


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


region_list_api_view = RegionListAPIView.as_view()


class RegionCreateAPIView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes = [UpdatePermission]


region_create_api_view = RegionCreateAPIView.as_view()


class AuthUserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
        status_code = status.HTTP_201_CREATED 
        response = {
            'success': True,
            'statusCode': status_code,
            'message': 'User succesfully registered',
            'user': serializer.data
        }
        return Response(response, status=status_code)


user_registration_api_view = AuthUserRegistrationView.as_view()


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is not None:
            if 'success' not in data:
                data['success'] = True
        return super().render(data, accepted_media_type, renderer_context)


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer
    # renderer_classes = (CustomRenderer,)

    # def get(self, request, *args, **kwargs):
    #     try:
    #         response = super().get(request, *args, **kwargs)
    #         return response
    #     except Exception as e:
    #         return Response({'success': False, 'error': str(e)})


user_login_api_view = UserLoginView().as_view()



class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserListSerializer


user_list_api_view = UserListAPIView.as_view()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'guid'


user_detail_api_view = UserDetailAPIView.as_view()


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserUpdateSerializer
    lookup_field = 'guid'


user_update_api_view = UserUpdateAPIView.as_view()