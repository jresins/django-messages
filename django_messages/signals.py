#added by jresins@gmail.com
from django.dispatch import Signal
message_state_change = Signal(providing_args=["request", "user"])
post_save = Signal(providing_args=["instance", "raw", "created", "using", "update_fields"])
