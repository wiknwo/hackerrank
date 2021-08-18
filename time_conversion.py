def timeConversion(s):
    # Write your code here
    # AM = ante meridiem, PM = post meridiem
    tokens = s.split(':')
    hours, minutes = int(tokens[0]), int(tokens[1])
    seconds, meridiem = int(tokens[2][0:2]), tokens[2][2:4]
    twenty_four_hour_format = ''
    
    if meridiem == 'AM' and hours == 12:
        twenty_four_hour_format = '{:02}:{:02}:{:02}'.format(0, minutes, seconds)
    elif meridiem == 'PM' and hours != 12:
        twenty_four_hour_format = '{:02}:{:02}:{:02}'.format(hours + 12, minutes, seconds)
    else:
        twenty_four_hour_format = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    
    return twenty_four_hour_format