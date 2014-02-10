from django_messages.models import inbox_count_for

def message_inbox_count_unseen(request):
    if request.user.is_authenticated():
        return {'messages_inbox_count_unseen': inbox_count_for(request.user)}
    else:
        return {}
