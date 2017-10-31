from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView


from .forms import ContactForm


# Artık bu view 'ı her yerde kullanabiliriz.
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')  # Buraya kendi URL 'sini yazalım.

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        title_align_center = False

        context['form'] = self.get_form()
        context['title'] = "Bize Yazın"
        context['title_align_center'] = title_align_center,
        context['section'] = "İletişim"
        return context

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        subject = 'Karnas İletişim Formu'
        # from_email = settings.EMAIL_HOST_USER
        from_email = "info@karnas.com.tr"
        to_email = [from_email, email]
        contact_message = '%s : %s \n e-posta: %s' % (full_name, message, email)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
        messages.success(self.request, "Mesajınız için teşekkür ederiz. Size en kısa sürede dönüş yapacağız.")
        return super(ContactView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        return FormView.post(self, request, *args, **kwargs)
