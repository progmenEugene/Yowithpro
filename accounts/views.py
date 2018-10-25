from django.shortcuts import render

from django.shortcuts import render
from django import forms
# Create your views here.
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages
from .forms import RegistrationForm, TeacherProfileUpdateForm, UserUpdateForm
from .models import User, TeacherProfile, VideoLink
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


def home(request):

	return render(request, 'home.html')

class SignUpView(TemplateView):
	template_name = 'registration/signup.html'




class RegistrationView(CreateView):
    template_name = 'accounts/user_form.html'
    form_class = RegistrationForm
    success_url = 'accounts:register-done'
    model = User

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(User.objects.make_random_password())
        obj.is_active = True  # PasswordResetForm won't send to inactive users.
        obj.save()

        # This form only requires the "email" field, so will validate.
        reset_form = PasswordResetForm(self.request.POST)
        reset_form.is_valid()  # Must trigger validation
        # Copied from django/contrib/auth/views.py : password_reset
        opts = {
            #'use_https': self.request.is_secure(),
            'email_template_name': 'registration/verification.html',
            'subject_template_name': 'registration/verification_subject.txt',
            'request': self.request,
            # 'html_email_template_name': provide an HTML content template if you desire.
        }
        # This form sends the email on save()
        reset_form.save(**opts)

        return redirect('register-done')























# profile view for teacher and maybe for buyer
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = TeacherProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            TeacherProfile.objects.create(**{
                'name' : 'name', 'city': 'city', 'club': 'club', 'url_link': 'url.com', 'desctiption': 'desc'
            })
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = TeacherProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)









#Videos links view
def videolink(request):
    context = {'videos': VideoLink.objects.all()}
    return render(request, 'accounts/videolink.html')

#Add video links for teacher profile
class VideoLinksView(ListView):
    model = VideoLink
    template_name = 'accounts/videolink.html'
    #<app>/<model>_<viewstype>
    context_object_name = 'videos'
    ordering = ['-pub_date']


class VideoDetailView(DetailView):
    model = VideoLink
    template_name = 'accounts/videolink_detail.html'

class DateInput(forms.DateInput):
    input_type = 'date'

class VideoCreateView(LoginRequiredMixin, CreateView):
    model = VideoLink

    template_name = 'accounts/videolink_form.html'
    fields = ['title','title_image', 'link_url', 'pub_date', 'short_description']





    def form_valid(self, form):

        form.instance.teacher = self.request.user


        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VideoLink
    fields = ['title', 'title_image', 'link_url', 'pub_date', 'short_description']
    template_name = 'accounts/videolink_form.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user

        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.teacher:
            return True
        return False





class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VideoLink
    success_url = '/'
    template_name = 'accounts/videolink_confirm_delete.html'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.teacher:
            return True
        return False