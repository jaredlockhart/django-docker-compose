import mock
from django.test import TestCase
from django.core.urlresolvers import reverse


class CounterTest(TestCase):

    def setUp(self):
        self.mock_redis_client = mock.Mock()

        strict_redis_patcher = mock.patch('project.views.redis.StrictRedis')
        strict_redis = strict_redis_patcher.start()
        strict_redis.return_value = self.mock_redis_client
        self.addCleanup(strict_redis_patcher.stop)

    def test_counter_returns_value(self):
        response = self.client.get(reverse('counter'))
        self.assertTrue(response.status_code, 200)

    def test_counter_failure_returns(self):
        self.mock_redis_client.incr.side_effect = Exception
        response = self.client.get(reverse('counter'))
        self.assertTrue(response.status_code, 200)
