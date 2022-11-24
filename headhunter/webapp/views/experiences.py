from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.forms.experiences import ExperienceForm
from webapp.models import Resumes, Educations, Experiences


class CreateExperienceView(PermissionRequiredMixin, CreateView):
    template_name = 'experiences/create_experience.html'
    model = Experiences
    form_class = ExperienceForm
    permission_required = 'webapp.add_experiences'

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        resume = get_object_or_404(Resumes, pk=pk)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            resume.experience.add(experience)
            return redirect('resume', pk=pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def has_permission(self):
        resume = get_object_or_404(Resumes, pk=self.kwargs.get('pk'))
        return (super().has_permission() or resume.author.username == str(self.request.user)
                or self.request.user.is_superuser)


class EditExperienceView(PermissionRequiredMixin, UpdateView):
    template_name = 'experiences/edit_experience.html'
    model = Experiences
    form_class = ExperienceForm
    permission_required = 'webapp.change_experiences'

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.kwargs.get('upk')})

    def has_permission(self):
        resume = get_object_or_404(Resumes, pk=self.kwargs.get('pk'))
        return (super().has_permission() or resume.author.username == str(self.request.user)
                or self.request.user.is_superuser)


class DeleteExperienceView(PermissionRequiredMixin, DeleteView):
    template_name = 'educations/delete_education.html'
    model = Experiences
    context_object_name = 'experience'
    permission_required = 'webapp.delete_experiences'

    def get(self, request, *args, **kwargs):
        self.resume_pk = kwargs.get('upk')
        return super(DeleteExperienceView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['resume_pk'] = self.resume_pk
        return super(DeleteExperienceView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.kwargs.get('upk')})

    def has_permission(self):
        resume = get_object_or_404(Resumes, pk=self.kwargs.get('pk'))
        return (super().has_permission() or resume.author.username == str(self.request.user)
                or self.request.user.is_superuser)