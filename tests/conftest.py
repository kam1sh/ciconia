import logging

import pytest
from anchor.users.models import User

from . import Client, PackageFactory


def pytest_configure():
    # removes StreamHandler to avoid double logging (in stderr and pytest)
    logging.getLogger("anchor").handlers = []


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def client():
    return Client()


class UserFactory:
    def new(self, email, password="123"):
        return User.objects.create_user(email, email=email, password=password)


@pytest.fixture
def users(db):
    return UserFactory()


@pytest.fixture
def user(users):
    usr = users.new("test@localhost")
    try:
        yield usr
    finally:
        usr.delete()


@pytest.yield_fixture
def tempfile(tmp_path):
    with PackageFactory(tmp_path) as factory:
        yield factory.gen_file


@pytest.yield_fixture(scope="function")
def packages(tmp_path, user):
    with PackageFactory(tmp_path) as factory:
        yield factory
