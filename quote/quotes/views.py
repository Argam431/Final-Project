#from django.http import HttpResponseRedirect
#from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views import View
from quotes.forms import CreateQuoteForm, LoginForm, SignUpForm
from .models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView,  SuccessURLAllowedHostsMixin
from .utils import NotLoginRequiredMixin



class QuoteListview(ListView):
    paginate_by = 10
    model = Quote
    template_name = 'quote/quote-listview.html'
    context_object_name = 'menu'

    def get_queryset(self):
        query_set = Quote.objects.select_related('author').all().prefetch_related('tags')
        return  query_set



class TagListview(ListView):
    paginate_by = 10
    model = Tag
    template_name = 'quote/tag-listview.html'
    context_object_name = 'menu'
    
    def get_queryset(self):
        return Quote.objects.select_related('author').all().prefetch_related('tags').filter(tags__name=self.kwargs['tag_name'])

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_nm'] = self.kwargs['tag_name']
        return context



class AuthorQuoteListview(ListView):
    paginate_by = 10
    model = Author
    template_name = 'quote/author-quotes-listview.html'
    context_object_name = 'menu'

    def get_queryset(self):
        return Quote.objects.select_related('author').filter(author_id = self.kwargs['author_name']).prefetch_related('tags')

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['author_name'] = self.kwargs['author_name']
        return context



class SignupUser(NotLoginRequiredMixin,CreateView):
    form_class = SignUpForm
    template_name = 'quote/signup.html'
    success_url = reverse_lazy('quote:login')
    redirect_authenticated_user=True


''' 
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('quote:quote-list'))
        return super().get(request, *args, **kwargs)
'''  
    

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'quote/login.html'
    redirect_authenticated_user=True
    #aranc es next paige i gnum er account/profile u berum er 404
    next_page = reverse_lazy('quote:quote-list')
    success_url = reverse_lazy('quote:quote-list')
    

class LogoutUser(LogoutView):
    next_page = reverse_lazy('quote:quote-list')


class CreateQuote(LoginRequiredMixin,CreateView):
    login_url = 'quote:login'
    form_class = CreateQuoteForm
    template_name = 'quote/add_quote.html'
    
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        name = self.request.user.first_name + ' ' + self.request.user.last_name
        author = Author.objects.get_or_create(name=name)[0]
        self.object.author_id = author.name
        return super(CreateQuote, self).form_valid(form)
      

    def get_success_url(self):
        name = self.request.user.first_name + " " + self.request.user.last_name
        return reverse('quote:author-quote-list',args = (name,))
        
            