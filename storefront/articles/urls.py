from django.urls import path 
from django.conf.urls import url 
from articles import views


app_name="articles"
urlpatterns=[
    path('',views.index,name="list"),
    path("create/",views.article_create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail")
    
]