from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.boards.models import Board
from apps.projects.models import Project
from hackachieve.utils import START_UP_BOARD_LIST

GOAL_STATUS = {
    'standby': 1,
    'ongoing': 2,
    'completed': 3
}


# method for updating order_position with fo
@receiver(post_save, sender=Project)
def create_boards(sender, instance, **kwargs):
    if instance.id and instance.user:
        for item in START_UP_BOARD_LIST:
            Board.objects.create(name=item['name'], description=item['description'], project_id=instance.id,
                                 user_id=instance.user.id)