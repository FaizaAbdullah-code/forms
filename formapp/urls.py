from django.urls import include, path
from formapp import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', views.contact, name="contact"),
    path('snippet', views.snippet_detail, name="snippet")
]