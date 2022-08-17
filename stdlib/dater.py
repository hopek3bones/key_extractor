from datetime import datetime

def getdatetime(dt, timezone=None):
    if type(timezone) is int:
        timestamp = datetime.timestamp(dt);
        timestamp += timezone * 3600;
        dt_object = datetime.fromtimestamp(timestamp);

        return dt_object;

    else:
        return dt;
