from rest_framework_simplejwt.authentication import JWTAuthentication

def verificar_token(request):
    auth = JWTAuthentication()

    try:
        user_auth = auth.authenticate(request)
        if user_auth:
            return user_auth[0]
    except:
        return None

    return None