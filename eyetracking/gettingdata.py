from eyetracking.models import GatheredData

def addData(loc, spd, gaz, inc, req):
    current_user = req
    d = GatheredData( location = loc,
                    speed = spd,
                    gaze = gaz,
                    incident = inc,
                    user = current_user, )
    d.save()
