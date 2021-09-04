from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
app_name="tasks"

urlpatterns=[
    path("",views.index,name="index"),
  #  path("metrics",views.metrics,name="metrics")
    path("task",views.task_index,name="task_index"),
    path("/delete/<int:r_id>",views.delete,name="delete"),
    path("/update_t/<int:r_id>",views.update_template,name="update_t"),
    path("update/<int:r_id>",views.update,name="update")
]