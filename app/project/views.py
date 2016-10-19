import redis
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse


class RedisClientMixin(object):

    def __init__(self, *args, **kwargs):
        super(RedisClientMixin, self).__init__(*args, **kwargs)
        self.redis_client = redis.StrictRedis(host=settings.REDIS_URL)


class CounterView(RedisClientMixin, View):

    def get(self, request):
        try:
            count = self.redis_client.incr('counter', 1)
        except:
            count = 0

        return HttpResponse('Redis Counter: {count}'.format(count=count))
