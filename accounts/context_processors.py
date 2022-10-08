from datetime import datetime


def get_time(request):
    time_bishkek = datetime.now()
    return {"time": time_bishkek}


