from django import db
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import TransactionTestCase

from app.boot import boot
from app.models import Project


def setupUsers():
    User.objects.create_superuser(username='testsuperuser',
                                  email='superuser@test.com',
                                  password='test1234')
    User.objects.create_user(username='testuser',
                             email='user@test.com',
                             password='test1234')
    User.objects.create_user(username='testuser2',
                             email='user2@test.com',
                             password='test1234')


def setupProjects():
    Project.objects.create(
        owner=User.objects.get(username="testsuperuser"),
        name="Super User Test Project",
        description="This is a test project"
    )
    Project.objects.create(
        owner=User.objects.get(username="testuser"),
        name="User Test Project",
        description="This is a test project"
    )
    Project.objects.create(
        owner=User.objects.get(username="testuser2"),
        name="User 2 Test Project",
        description="This is a test project"
    )

class BootTestCase(TestCase):
    '''
    This class provides optional default mock data as well as 
    proper boot initialization code. All tests for the app
    module should derive from this class instead of TestCase.

    We don't use fixtures because we have signal initialization login
    for some models, which doesn't play well with them.
    '''
    @classmethod
    def setUpTestData(cls):
        super(BootTestCase, cls).setUpTestData()
        boot()
        setupUsers()
        setupProjects()

    @classmethod
    def tearDownClass(cls):
        super(BootTestCase, cls).tearDownClass()


class BootTransactionTestCase(TransactionTestCase):
    '''
    Same as above, but inherits from TransactionTestCase
    '''
    def setUp(self):
        super().setUp()
        boot()
        setupUsers()
        setupProjects()

    @classmethod
    def tearDownClass(cls):
        super(BootTransactionTestCase, cls).tearDownClass()
