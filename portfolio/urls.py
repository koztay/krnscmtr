from django.conf.urls import url
from .views import ProjectdetailView

urlpatterns = [
        url(r'^(?P<slug>[\w-]+)/$', ProjectdetailView.as_view(), name='project_detail'),
]
