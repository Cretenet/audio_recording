from django.contrib.auth.models import User
user = User(username="django")
user.set_password("secret")
user.save()