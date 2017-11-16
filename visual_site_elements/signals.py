from django.dispatch import receiver


from django_cleanup.signals import cleanup_pre_delete

# https://github.com/un1t/django-cleanup
# def sorl_delete(**kwargs):
#     from sorl.thumbnail import delete
#     delete(kwargs['file'])
#
# cleanup_pre_delete.connect(sorl_delete)


@receiver(cleanup_pre_delete)  # tüm objeler pre_delete olmadan çalışıyor...
def image_pre_delete_receiver(**kwargs):
    from sorl.thumbnail import delete
    delete(kwargs['file'])


