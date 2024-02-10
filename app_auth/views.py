from rest_framework import status
from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token


class LoginAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        if request.method == 'POST':
            try:
                username = request.data.get('username')
                password = request.data.get('password')

                user = authenticate(
                    request, username=username, password=password)

                if user is not None:
                    login(request, user)

                    # Obtener el ID del usuario
                    user_id = user.id

                    # Obtener el token CSRF
                    csrf_token = get_token(request)

                    # Obtener la sessionid de la sesión actual
                    sessionid = request.session.session_key

                    # Devolver la respuesta con el token CSRF, sessionid y el ID del usuario
                    response_data = {
                        'message': 'Login successful',
                        'csrfToken': csrf_token,
                        'userId': user_id,
                        'sessionid': sessionid
                    }

                    print(request.data)
                    print(response_data)
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    print(request.data)
                    return Response({'message': 'Invalid credentials'}, status=401)
            except Exception as e:
                print('\nERROR: \n', e)
                return Response({'message': 'An error occurred'}, status=500)
        else:
            return Response({'message': 'An error occurred'}, status=500)


class LogoutAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
