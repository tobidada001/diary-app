from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='index'),
    path('diary', views.index, name="diary"),
    path('new-diary/', views.new_diary, name="new_diary"),
    path('register/', views.register, name="register"),
    path('login/', views.signin, name="signin" ),
    path('logout/', views.signout, name="logout" ),
    path('landing-page/', views.landingpage, name="landingpage" ),
    path('open-diary/<int:id>/', views.open_diary, name='open_diary'),

]
