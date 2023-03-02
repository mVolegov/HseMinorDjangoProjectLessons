from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse("helloResponse")


def html(request):  # http://127.0.0.1:8000/httpResponse/html/
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s.</body></html>" % now
    return HttpResponse(html)


def f_str(request, str_value):  # http://127.0.0.1:8000/httpResponse/f_str/abc
    print("request.path: ", request.path)
    print(" str_value: ", str_value)
    return HttpResponse(
        f"<p>f_str, str_value.capitalize():  {str_value.capitalize()}</p>"
    )


def f_int(request, int_value):  # http://127.0.0.1:8000/httpResponse/f_int/12345
    print(type(int_value), int_value)
    return HttpResponse(f"f_int, int_value: {int_value} ")


def f_slug(request, slug_value):  # http://127.0.0.1:8000/httpResponse/f_slug/building-your_1st-django-site
    print(type(slug_value), slug_value)
    return HttpResponse(f"f_slug, slug_value: {slug_value}")


def f_path(request, path_value):  # http://127.0.0.1:8000/httpResponse/f_path/building/your-1st/django-site
    print("path_value: ", path_value)
    path_elements = path_value.split("/")
    print(path_elements)
    path_elements_amount = path_elements.__len__()
    print(path_elements_amount)

    print("request.path: ", request.path)
    request_path_elements = request.path.split("/")
    print('request_path_elements:', request_path_elements)
    request_elements_amount = request_path_elements.__len__()
    print(request_elements_amount)
    last_request_path_element = request_path_elements[request_elements_amount - path_elements_amount - 1]
    print(last_request_path_element)
    return HttpResponse(f"last_request_path_element: {last_request_path_element}")


def f_str_int_slug(request, str_value, int_value, slug_value):
    print(type(str_value), str_value)
    print(type(int_value), int_value)
    print(type(slug_value), slug_value)
    return HttpResponse(
        f"f_str, str_value: {str_value} <br>f_int, f_int: {int_value} <br>f_slug, slug_value: {slug_value}"
    )
