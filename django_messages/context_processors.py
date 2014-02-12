from django_messages.models import inbox_count_for

def unseen_message_count(request):
    if request.user.is_authenticated():
        return {'unseen_message_count': inbox_count_for(request.user)}
    else:
        return {}