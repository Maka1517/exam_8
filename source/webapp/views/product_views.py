from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    paginated_by = 4
    paginate_orphans = 1
    model = Product
    ordering = ['created_at']


class ProductView(DetailView):
   template_name = 'product_view.html'
   model = Product


class ProductCreatView(PermissionRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    fields = ['name', 'category', 'description']
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'products'
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'products'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_issue'