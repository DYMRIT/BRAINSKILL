from django.urls import path, include
from courses.views import CourseListView
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name='home'),
    path('detail/<slug:slug_course>/', views.detail_course, name='detail'),
    path('detail/<slug:slug>/<slug:slug_article>/', views.month, name='month'),
    path('price/', views.price, name='price'),
    path('about/', views.about, name='about'),
    path('sale/', views.sale, name='sale'),
]
