from eyetracking.models import GatheredData
from django.contrib.auth.models import User

def addData(loc, spd, gaz, inc, req):
    current_user = req
    userObj = User.objects.get(username = current_user)

    d = GatheredData( location = loc,
                    speed = spd,
                    gaze = gaz,
                    incident = inc,
                    user = userObj, )
    d.save()
