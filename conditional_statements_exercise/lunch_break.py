from math import ceil
tv_show = input()
tv_episode_duration = int(input())
break_duration = int(input())
lunch_duration = break_duration * 1/8
relax_time = break_duration * 1/4
time_left = break_duration - lunch_duration - relax_time
diff = abs(time_left - tv_episode_duration)
if time_left >= tv_episode_duration:
    print(f"You have enough time to watch {tv_show} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {ceil(diff)} more minutes.")
