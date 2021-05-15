# https://replit.com/@JackHung0111/boilerplate-time-calculator-1

def add_time(start, duration, day = "none"):
    start_hr,start_mins = start.split()[0].split(':')
    start_hr,start_mins = int(start_hr), int(start_mins)
    if start.split()[1] == "PM":
        start_hr += 12
    duration_hr,duration_mins = duration.split(':')
    duration_hr,duration_mins = int(duration_hr), int(duration_mins)
    result = [start_hr + duration_hr,start_mins + duration_mins," AM","",""]
    if result[1] >= 60:
        result[1] -= 60
        result[0] += 1
    day_count = int(result[0]/24)
    result[0] %= 24
    if result[0]%24 >= 12 :
        result[2] = " PM"
        result[0] -= 12
    if result[0] == 0:
        result[0] = 12 
    days = ["none", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    date = days.index(day.lower())
    if date > 0:
        date1 = (date + day_count)%7 if (date + day_count)%7 > 0 else 7
        result[3] = ", " + days[date1].capitalize()
    if day_count == 1:
        result[4] = " (next day)"
    elif day_count > 1:
        result[4] = " (" + str(day_count) + " days later)"
    return str(result[0]) + ":" + str(result[1]).rjust(2,"0") + result[2] + result[3] + result[4]
    