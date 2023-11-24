from django.views.generic import TemplateView,UpdateView,CreateView,DeleteView,ListView,DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from .models import Hospedagem
from .forms import HospedagemForm

class HospedagemCriar(CreateView):
    template_name = 'hospedagem/form.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('hospedagem_listar')

class HospedagemEditar(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'hospedagem/form.html'
    pk_url_kwarg = 'id' # Nome da variável na URL
    
    def get_success_url(self):
        return reverse_lazy('hospedagem_listar')

class HospedagemRemover(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class HospedagemListar(ListView):
    model = Hospedagem
    template_name = 'hospedagem/hospedagens.html'
    context_object_name = 'hospedagens'  # Nome da variável a ser usada no template
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HospedagemForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = HospedagemForm(self.request.GET or None)
        if self.form.is_valid():
            if self.form.cleaned_data.get('nome'):
                queryset = queryset.filter(nome_aluno__icontains=self.form.cleaned_data['nome'])
            if self.form.cleaned_data.get('cidade'):
                queryset = queryset.filter(cidade=self.form.cleaned_data['cidade'])
            if self.form.cleaned_data.get('curso'):
                queryset = queryset.filter(curso=self.form.cleaned_data['curso'])
        return queryset

class HospedagemDetalhe(DetailView):
    model = Hospedagem
    template_name = 'hospedagem/detail.html'
    pk_url_kwarg = 'id'
    

class IndexView(TemplateView):
    template_name = "hospedagem/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_hospedagens'] = Hospedagem.objects.count()
        return context


