import datetime

def dateformat():
    today = datetime.datetime.now()
    month = today.month
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    day = today.day
    if day<10:
        day = '0'+str(day)
    else:
        day = str(day)

    return([month,day])
