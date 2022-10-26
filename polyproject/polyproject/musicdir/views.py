from django.shortcuts import render, redirect
import django_filters.rest_framework
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Musicdir, Category
from .forms import UserRegisterForm
from .serializers import MusicdirSerializer


class HomeMusicdir(ListView):
    model = Musicdir
    template_name = 'musicdir/index.html'
    context_object_name = 'musicdir'
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Musicdir.objects.filter(is_published=True)


def get_category(request, category_id):
    musicdir = Musicdir.objects.filter(Q(category_id=category_id) & Q(is_published=True))
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'musicdir': musicdir,
        'category': category,
        'categories': categories,
    }
    return render(request, 'musicdir/category.html', context)


class MusicdirViewSet(ModelViewSet):
    queryset = Musicdir.objects.all()
    serializer_class = MusicdirSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'category_id']
    search_fields = ['title']
    ordering_fields = ['title', 'category_id']



# class MusicdirViewSet1(ModelViewSet):
#     queryset = Musicdir.objects.all()
#     serializer_class = MusicdirSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'category_id']


# class MusicdirViewSet2(ModelViewSet):
#     queryset = Musicdir.objects.all()
#     serializer_class = MusicdirSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'category_id']


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешна')
            return redirect('login')
        else:
            messages.error(request, 'Ошбика регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'musicdir/register.html', {"form": form})


def login(request):
    return render(request, 'musicdir/login.html')


# def index(request):
#     musicdir = Musicdir.objects.all()
#     categories = Category.objects.all()
#
#     paginator = Paginator(musicdir, 3)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'musicdir': musicdir,
#         'title': 'Трек-лист',
#         'categories': categories,
#         'page_obj': page_obj,
#     }
#     return render(request,  'musicdir/index.html', context)





