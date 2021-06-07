from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from main_gusto.models import UserMessages
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists() or u.is_staff, login_url='/error/')
def messages_view(request):
    messages = UserMessages.objects.filter(
        is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 4)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'messages_views.html', context={'items': messages_page})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists() or u.is_staff, login_url='/error/')
def message_processed(request, message):
    message = UserMessages.objects.get(pk=message)
    message.is_processed = True
    message.save()
    # return render(request, "/", context={'message': message})
    return redirect("/view/")


def error(request):
    return render(request, 'error.html')
