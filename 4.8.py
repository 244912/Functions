###
# Formatuje czas na tekst (12-godzinny format z am/pm)
#
def time_string(hour, minute, format_type):
    h_str = f"{hour:02d}"
    m_str = f"{minute:02d}"
    
    if hour == 0:
        display_hour = 12
    elif hour > 12:
        display_hour = hour - 12
    else:
        display_hour = hour
    
    display_h_str = f"{display_hour:02d}"

    if hour < 12:
        ampm = "am"
    else:
        ampm = "pm"
    
    return f"{display_h_str}:{m_str}{ampm}"


print(time_string(0, 5, '12'))      
print(time_string(7, 30, '12'))     
print(time_string(12, 46, '12'))    
print(time_string(13, 10, '12'))    
print(time_string(19, 2, '12'))