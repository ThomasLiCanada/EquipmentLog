from django.contrib import admin
from django.urls import path, include
from equipments.views import home_view,home_view_after_input, popup_temperature_view, popup_overdue_view
from equipments.views import edit_equipment_view, edit_last_equipment_view, home_view_for_correction
from equipments.views import home_for_search_view, popup_overdue_and_temperature_view
from django.contrib.auth import views as auth_views
from a02_account.views import registration_view, logout_view, login_view, account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,{}, name="home"),
    path('home_for_correction', home_view_for_correction, {}, name="home_for_correction"),
    path('home_for_search', home_for_search_view, {}, name="home_for_search"),


    path('equipments/', include('equipments.urls', 'equipments')),
    path('home_after_input', home_view_after_input, name="home_after_input"),
    path('pop_temperature', popup_temperature_view, name="pop_temperature"),
    path('pop_overdue', popup_overdue_view, name="pop_overdue"),
    path('pop_overdue_temperature', popup_overdue_and_temperature_view, name="pop_overdue_temperature"),

    path('edit_equipment/<int:equipment_id>/', edit_equipment_view, name='edit_equipment'),
    path('edit_last_equipment/', edit_last_equipment_view, name='edit_last_equipment'),


    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
