from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source="actor.username")

    class Meta:
        model = Notification
        fields = ["id", "actor", "actor_username", "verb", "target", "read", "timestamp"]
