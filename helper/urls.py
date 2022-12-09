from django.urls import path

from helper.apps import HelperConfig
from helper.views import HelperListView, CategoryListView, HelperDetailView, HelperUpdateView, HelperDeleteView

app_name = HelperConfig.name

urlpatterns = [
    path('category/', HelperListView.as_view(), name='list'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', HelperDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', HelperUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', HelperDeleteView.as_view(), name='delete')
]