from django.contrib.contenttypes.models import ContentType
from .models import Activity
import datetime
from django.utils import timezone

# przeciwdziałanie ponownych wystąpień wyświetlanych czynności w strumieniu aktywności
def new_action(user, action, track=None):
    currentTime = timezone.now()
    checkingTime = currentTime - datetime.timedelta(seconds=55)
    almostSame = Activity.objects.filter(user_id=user.id, action=action  )
    if track:
        targetContentType = ContentType.objects.get_for_model(track)
        almostSame = almostSame.filter(targetContentType=targetContentType, targetID=track.id)

    if not almostSame:
        newAction = Activity(user=user, action=action, track=track)
        newAction.save()
        return True
    return False
