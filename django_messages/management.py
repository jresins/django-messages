#modified by jresins@gmail.com
#added notification version check support
from django.db.models import get_models, signals
from django.conf import settings
from django.utils.translation import ugettext_noop as _

if "notification" in settings.INSTALLED_APPS:
    from notification import __version__ as notification_version
    from notification import models as notification

    if notification_version>=1.0:
        from notification.models import NoticeType

    def create_notice_types_v1(app, created_models, verbosity, **kwargs):
        NoticeType.create("messages_received", _("Message Received"), _("you have received a message"), default=2)
        NoticeType.create("messages_sent", _("Message Sent"), _("you have sent a message"), default=1)
        NoticeType.create("messages_replied", _("Message Replied"), _("you have replied to a message"), default=1)
        NoticeType.create("messages_reply_received", _("Reply Received"), _("you have received a reply to a message"), default=2)
        NoticeType.create("messages_deleted", _("Message Deleted"), _("you have deleted a message"), default=1)
        NoticeType.create("messages_recovered", _("Message Recovered"), _("you have undeleted a message"), default=1)

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("messages_received", _("Message Received"), _("you have received a message"), default=2)
        notification.create_notice_type("messages_sent", _("Message Sent"), _("you have sent a message"), default=1)
        notification.create_notice_type("messages_replied", _("Message Replied"), _("you have replied to a message"), default=1)
        notification.create_notice_type("messages_reply_received", _("Reply Received"), _("you have received a reply to a message"), default=2)
        notification.create_notice_type("messages_deleted", _("Message Deleted"), _("you have deleted a message"), default=1)
        notification.create_notice_type("messages_recovered", _("Message Recovered"), _("you have undeleted a message"), default=1)

    if notification_version>=1.0:
        signals.post_syncdb.connect(create_notice_types_v1, sender=notification)
    else:
        signals.post_syncdb.connect(create_notice_types, sender=notification)

else:
    print "Skipping creation of NoticeTypes as notification app not found"