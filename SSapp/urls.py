from django.urls import path
from SSapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('contactSS', views.contactSS, name="contactSS"),
    path('info/',views.info,name="info"),
    path('features/',views.features,name="features"),
    path('services/',views.services,name="services"),
    path('register_crt', views.CrtView.as_view(), name="register_crt"),
    path('register_user', views.UsrView.as_view(), name="register_user"),
    path('register_crim', views.CrimView.as_view(), name="register_crim"),
    path('sgin_crt', views.sgin_crt, name="sgin_crt"),
    path('sgin_user', views.sgin_user, name="sgin_user"),
    path('sgin_crim', views.sgin_crim, name="sgin_crim"),
    path('sginpg_user', views.sginpg_user, name="sginpg_user"),
    path('sginpg_crim', views.sginpg_crim, name="sginpg_crim"),
    path('sginpg_crt', views.sginpg_crt, name="sginpg_crt"),
    path('search/', views.search, name="search"),
    path("crim_edit", views.update_data, name="update_data"),
    path("usr_edit", views.update_usr_data, name="update_usr_data"),
    path("change_pass_usr", views.change_pass_usr, name="change_pass_usr"),
    path("change_pass_crim", views.change_pass_crim, name="change_pass_crim"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('letsout', views.letsout, name="letsout"),
    path("contact2",views.contact2,name='contact2'),
    path("contact",views.contact,name='contact'),
    path("services",views.services,name="services"),
    path("indexo",views.indexo,name="indexo"),
    path("upload",views.uploadImage,name="uploadImage"),
    path('TO/', views.indexTO, name='indexTO'),
    path('list/', views.to_do, name='to_do'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    


]
