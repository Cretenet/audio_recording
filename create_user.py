from django.contrib.auth.models import User
user = User(username="user")
user.set_password("secrete")
user.save()