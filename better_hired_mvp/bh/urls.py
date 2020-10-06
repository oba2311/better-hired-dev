from django.urls import path
from . import views

urlpatterns = [
    #  /bh/
    path('bh/', views.index, name='index'),
    # /bh/5
    path('<int:question_id>/', views.detail, name='details'),
    # /bh/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /bh/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # /bh/dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]