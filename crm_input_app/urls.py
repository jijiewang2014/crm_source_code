"""Defines URL patterns for crm_input_app """
from django.conf.urls import url
from . import views

urlpatterns=[
    #Home page
    url(r'^$', views.index, name='index'),
    
    #show all parameter sets
    url(r'^parasList/$',views.parasList,name='parasList'),

    #show each parameter set details

    url(r'^parasDetail/(?P<paras_id>\d+)$',views.parasDetail,name='parasDetail'),
 
    #add new parameter sets
    url(r'^new_paras/$', views.new_paras, name='new_paras'),


    # view results page

    url(r'^result/(?P<paras_id>\d+)$', views.getResult, name='result'),

    # edit parameters page
    url(r'^edit_paras/(?P<paras_id>\d+)$', views.edit_paras, name='edit_paras'),

]