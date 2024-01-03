from rest_framework import generics
from rest_framework_simplejwt import authentication
from .models import Region
from .serializers import RegionSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserListSerializer,
    UserUpdateSerializer,
    PasswordChangeSerializer,
    AgentCalculationSerializer,
    AgentListSerializer
)
from .models import User, AgentCalculation

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

    def get_queryset(self):
        params = self.request.query_params
        qs = User.objects.all()
        phone_number = params.get('phone_number', None)
        full_name = params.get('full_name', None)

        if phone_number:
            qs = qs.filter(Q(phone_number__icontains=phone_number))
        if full_name:
            qs = qs.filter(Q(full_name__icontains=full_name))
        return qs


user_list_api_view = UserListAPIView.as_view()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'guid'


user_detail_api_view = UserDetailAPIView.as_view()


class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserUpdateSerializer
    lookup_field = 'guid'

user_update_delete_api_view = UserUpdateAPIView.as_view()


class AgentListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_agent=True)
    serializer_class = AgentListSerializer

agent_list_api_view = AgentListAPIView.as_view()


class PasswordChangeAPIView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            if serializer.data['new_password1'] != serializer.data['new_password2']:
                return Response({
                    'status': 'error', 'message': _('These two fields should be the same'),
                })
            user = request.user 
            user_id = serializer.validated_data.get('user_id', None) 
            target_user = None
            if user_id is not None:
                try:
                    target_user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return Response({
                        'status': 'error', 'message': _('User does not exist'),
                    }, status=status.HTTP_400_BAD_REQUEST)
            
            if target_user and request.user.is_superuser:
                user = target_user
            else:
                user = request.user
            user.set_password(serializer.data['new_password1'])
            user.save()
            return Response({
                'message': _('Password successfully updated')},
                status=status.HTTP_200_OK
                )
        else:
            return Response({
                'status': 'error', 'message': _('Invalid data'),
                'data': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
                )

password_change_api_view = PasswordChangeAPIView.as_view()


class AgentCalculationCreateAPIView(generics.CreateAPIView):
    queryset = AgentCalculation.objects.all()
    serializer_class = AgentCalculationSerializer

agentcalculation_create_api_view = AgentCalculationCreateAPIView.as_view()


class AgentCalculationListAPIView(generics.ListAPIView):
    queryset = AgentCalculation.objects.all()
    serializer_class = AgentCalculationSerializer

    def get_queryset(self):
        param = self.request.query_params
        agent=param.get('agent')
        tourpackage=param.get('tourpackage')
        if agent is not None or tourpackage is not None:
            qs = AgentCalculation.objects.filter(agent__guid=agent, tourpackage__guid=tourpackage)
        return qs

agentcalculation_list_api_view = AgentCalculationListAPIView.as_view()

class AgentCalculationUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentCalculation.objects.all()
    serializer_class = AgentCalculationSerializer
    lookup_field='guid'

agentcalculation_update_delete_api_view = AgentCalculationUpdateDeleteAPIView.as_view()
