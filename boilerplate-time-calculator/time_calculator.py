import re
def add_time(time, hour_min, day=None):
  switch_am_pm = {"AM":"PM","PM":"AM"}
  am_pm_hrs = {"AM":0,"PM":12}
  no_days = {1:"Monday",
         2:"Tuesday",
         3:"Wednesday",
         4:"Thursday",
         5:"Friday",
         6:"Saturday",
         7:"Sunday"}
  days_no =     dict(zip(list(no_days.values()),list(no_days.keys())))
  hrs_min = re.findall('([0-9]+)',time)
  am_pm = re.findall('([a-zA-Z]+)',time)[0]
  hrs_min_add = re.findall('([0-9]+)',hour_min)
  # print(hrs_min, am_pm, hrs_min_add)
  hrs = int(hrs_min[0])+int(hrs_min_add[0])
  mins = int(hrs_min[1])+int(hrs_min_add[1])
  days = 0

  new_hrs = hrs + am_pm_hrs[am_pm] + mins/60
  days = new_hrs//24
  new_hrs = new_hrs%24
  hrs = int(hrs_min[0]) + am_pm_hrs[am_pm] + int(hrs_min[1])/60
  if ((new_hrs >= 0 and new_hrs < 12) and (hrs >= 0 and hrs < 12)) or ((new_hrs >= 12 and new_hrs < 24) and (hrs >= 12 and hrs < 24)):
    am_pm_n = am_pm
  else:
    am_pm_n = switch_am_pm[am_pm]
  
  if day and days:
    day = day.lower().capitalize()
    if (days_no[day]+days)%7==0:
      day_n = no_days[7]
    else:
      day_n = no_days[(days_no[day]+days)%7]
  elif day:
    day_n = day
  else:
    day_n = ""

  new_hr = int(abs(new_hrs - am_pm_hrs[am_pm_n]))%12
  if new_hr==0:
    new_hr = 12
  new_min = round(round(new_hrs - int(new_hrs),3)*60)
  base = "{: >2}:{:0>2} {}".format(new_hr,new_min,am_pm_n)
  if day_n:
    base =base +", "+ day_n
  
  if days == 0 and am_pm_n == "AM" and am_pm_n!=am_pm:
    base += " (next day)"
  elif days==1:
    base += " (next day)"
  elif days>1:
    base += f' ({int(days)} days later)'
  return base.lstrip()
