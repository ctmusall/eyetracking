from eyetracking.models import GatheredData, UserProfile

def addData(loc, spd, gaz, inc):
    d = GatherData( location = loc,
                    speed = spd,
                    gaze = gaz,
                    incident = inc)
