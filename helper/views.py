from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from helper.models import Helper, Category


class HelperListView(ListView):
    model = Helper

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('cat', None):
            category = self.request.GET.get('cat')
            return queryset.filter(category__id=category).all()


class HelperDetailView(DetailView):
    model = Helper


class HelperUpdateView(UpdateView):
    model = Helper
    fields = ('title', 'body',)
    success_url = reverse_lazy('helper:category_list')


class HelperCreateView(CreateView):
    model = Helper
    fields = ('title', 'body',)
    success_url = reverse_lazy('helper:category_list')


class HelperDeleteView(DeleteView):
    model = Helper
    success_url = reverse_lazy('helper:category_list')


class CategoryListView(ListView):
    model = Category



