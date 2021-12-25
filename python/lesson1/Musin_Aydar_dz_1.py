# ДЗ № 1


def convert_time(duration: int) -> str:
    day = duration // 86400
    hour = (duration - (day * 86400)) // 3600
    minutes = (duration - (3600 * (duration // 3600))) // 60
    seconds = (duration - (3600 * (duration // 3600))) - (minutes * 60)
    return day, hour, minutes, seconds


duration = 4153
result = convert_time(duration)
print(result)

#result = convert_time(duration)

