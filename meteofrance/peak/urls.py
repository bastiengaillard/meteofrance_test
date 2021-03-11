from django.urls import path
from django.conf.urls import url
from .api import CreatePeak, GetPeaks, UpdatePeak, DeletePeak, GetPeaksByBoundingBox
from . import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
	path('openapi/', get_schema_view(
        title="Peak service",
    ), name='openapi-schema'),

 	path('docs/', TemplateView.as_view(
        template_name='peak/documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

 	path('', views.index, name='index'),
	path('api', GetPeaks.as_view()),	
	path('api/<int:minlat>/<int:minlon>/<int:maxlat>/<int:maxlon>', 				  GetPeaksByBoundingBox.as_view()),	
    path('api/create', CreatePeak.as_view()),
	path('api/<int:pk>', UpdatePeak.as_view()),
  	path('api/<int:pk>/delete', DeletePeak.as_view()),
]
