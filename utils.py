def main():
    from django.contrib.auth.models import UserManager, User
    from rest_framework.authtoken.models import Token

    username = input('Digite nombre de Usuario para el SuperUsuario ')
    user = User.objects.create_user(username=username, is_staff=True)
    token = Token.objects.create(user=user)
    print(f"{username} creado correctamente, el token para las transacciones es: {token.key}")


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mgFact.settings')
    django.setup()
    main()
