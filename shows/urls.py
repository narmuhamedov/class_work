from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('shows/', views.ShowsListView.as_view(), name = 'shows_all'),
    path('shows/<int:id>/', views.ShowsDetailView.as_view(), name = 'shows_detail'),
    path('shows/<int:id>/update/', views.ShowsUpdateView.as_view(), name = 'shows_update'),
    path('shows/<int:id>/delete/', views.ShowDeleteView.as_view(), name='shows_delete'),
    path('add-shows/', views.ShowsCreateView.as_view(), name= 'add-shows'),
]