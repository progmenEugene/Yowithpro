from django.urls import path, include

from .views import RegistrationView, profile
from django.contrib.auth import views
from .views import  VideoCreateView, VideoDetailView, VideoDeleteView, VideoUpdateView, VideoLinksView, SignUpView

urlpatterns = [


    path('accounts/profile/', profile, name = 'profile'),
	path('accounts/profile/videos/', VideoLinksView.as_view(), name = 'videolink' ),
	path('accounts/profile/videos/<int:pk>/', VideoDetailView.as_view(), name = 'videodetail'),
	path('accounts/profile/videos/new/', VideoCreateView.as_view(), name ='videocreate'),
	path('accounts/profile/videos/<int:pk>/update/', VideoUpdateView.as_view(), name ='videoupdate'),
	path('accounts/profile/videos/<int:pk>/delete/', VideoDeleteView.as_view(), name = 'videodelete'),
    path('accounts/', include('django.contrib.auth.urls')),












path('register/signup/', SignUpView.as_view(), name = 'signup'),
    path('register/', RegistrationView.as_view(), name='teacher_signup'),
    path('register/done/', views.PasswordResetDoneView.as_view(), {
        'template_name': 'registration/initial-done.html'}, name='register-done'),

    path('register/password/?P<uidb64>[0-9A-Za-z_\-]+/?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/', views.PasswordResetConfirmView.as_view(), {
        'template_name': 'registration/initial_confirm.html',
        'post_reset_redirect': 'accounts:register-complete',
    }, name='register-confirm'),
    path('register/complete/', views.PasswordResetCompleteView.as_view(), {
        'template_name': 'registration/initial-change.html',
    }, name='register-complete'),
]