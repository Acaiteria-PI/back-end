from django.contrib.auth import get_user_model


def setUpUser(self, username='testuser', password='testpass'):
    User = get_user_model()
    # Some projects use a custom user model that requires email and does not
    # have a username field. Provide a sensible default email and set the
    # `name` field instead of `username` so it works with custom user models.
    email = f"{username}@example.com"
    # Make the user staff and superuser so they pass DjangoModelPermissions checks
    self.user = User.objects.create_user(email=email, password=password, name=username, is_staff=True, is_superuser=True)
    # try to authenticate API client when available
    try:
        self.client.force_authenticate(user=self.user)
    except Exception:
        pass
