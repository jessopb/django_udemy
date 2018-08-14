import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_p2.settings')

django.setup()
from django_app.models import OurUsers
from faker import Faker




fakegen = Faker()


def add_users(number=20):
    for user in range(number):

        first = fakegen.first_name()
        last = fakegen.last_name()
        fakeemail = first + '@example.org'

        ouruser = OurUsers.objects.get_or_create(first_name=first, last_name=last,email=fakeemail)


if __name__ == '__main__':
    print("populating")
    add_users(20)
    print("done")
