from django.conf import settings
from django.db import models
import uuid


class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=800)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ticket_user_creator")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                related_name="ticket_user_manager", null=True, default=None)
    status = models.ForeignKey(
        "Status", on_delete=models.DO_NOTHING, default=1
    )

    class Meta:
        db_table = "ticket"

    def __str__(self) -> str:
        return self.title


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "status"

    def __str__(self) -> str:
        return self.name
