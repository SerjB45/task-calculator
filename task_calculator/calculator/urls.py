from django.urls import path

from .views import (add_detail, create_task, delete_detail, delete_task,
                    edit_detail, edit_task, index, task_details, info_by_rate,
                    TypeStagesCreateView, TypeStagesDeleteView,
                    TypeStagesUpdateView, InfoByRateCreateView,
                    InfoByRateDeleteView, InfoByRateUpdateView,
                    TypeStagesListView)

urlpatterns = [
    path('', index, name='index'),
    path('create-task/', create_task, name='create_task'),
    path('task/<int:pk>/', task_details, name='task_details'),
    path('task/add-detail/<int:pk>/', add_detail, name='add_detail'),
    path('task/delete/<int:pk>/', delete_task, name='delete_task'),
    path('task/edit/<int:pk>/', edit_task, name='edit_task'),
    path('detail/delete/<int:pk>/', delete_detail, name='delete_detail'),
    path('detail/edit/<int:pk>/', edit_detail, name='edit_detail'),
    path('info-by-rate/', info_by_rate, name='info_by_rate'),
    path('type-stages/create/', TypeStagesCreateView.as_view(),
         name='create_type_stage'),
    path('info-by-rate/create/', InfoByRateCreateView.as_view(),
         name='create_info_by_rate'),
    path('type-stages/delete/<int:pk>/', TypeStagesDeleteView.as_view(),
         name='delete_type_stage'),
    path('info-by-rate/delete/<int:pk>/', InfoByRateDeleteView.as_view(),
         name='delete_info_by_rate'),
    path('type-stages/edit/<int:pk>/', TypeStagesUpdateView.as_view(),
         name='edit_type_stage'),
    path('info-by-rate/edit/<int:pk>/', InfoByRateUpdateView.as_view(),
         name='edit_info_by_rate'),
    path('info-by-stage/', TypeStagesListView.as_view(), name='info_by_stage'),
]
