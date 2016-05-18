from django.test import TestCase


class Tests(TestCase):

    def test_view_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
