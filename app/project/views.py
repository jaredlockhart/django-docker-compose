from django.http import HttpResponse


def home(request):
    import ipdb
    ipdb.set_trace()
    return HttpResponse('Hello!')
