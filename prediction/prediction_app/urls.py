from django.conf.urls import url
from prediction_app import views

# template tagging
app_name = 'prediction_app'

urlpatterns = [

    url(r'^formpage/$', views.form_name_view, name='form_name'),
    url(r'^$', views.index, name='index'),

]
