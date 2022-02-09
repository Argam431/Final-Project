from django.urls import path, reverse, reverse_lazy
from .views import  AuthorQuoteListview, CreateQuote, LoginUser, LogoutUser, QuoteListview, SignupUser, TagListview
from django.contrib.auth.decorators import login_required


app_name = 'quote'
urlpatterns = [
    path('',QuoteListview.as_view(),name='quote-list'),
    path('tag/<str:tag_name>/',TagListview.as_view(),name='tag-quote-list'),
    path('author/<str:author_name>/',AuthorQuoteListview.as_view(),name='author-quote-list'),
    path('signup/',SignupUser.as_view(),name='signup'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('create/quote/',login_required(CreateQuote.as_view(),login_url='quote:login'),name='create'), 
]
