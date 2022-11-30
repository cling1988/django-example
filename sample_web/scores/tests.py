import json

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class ScoreTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')

    def tearDown(self):
        self.user.delete()

    def test_index_page(self):
        response = self.client.get(reverse('scores:index'))
        self.assertEqual(response.status_code, 200)
        print(response)
        self.assertContains(response, "Score Page")
        self.assertContains(response, "Log Out")


    def test_get_score(self):
        response = self.client.get(reverse('scores:get_score', kwargs={'user_input': 12}))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(json.loads(response.content), {'result': 13})
