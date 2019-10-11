from django.contrib.auth.models import User
import factory


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Faker('user_name')
    fist_name = factory.Faker('fist_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
