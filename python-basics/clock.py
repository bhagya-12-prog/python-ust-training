#!/usr/bin/env python
# coding: utf-8

# In[2]:



import time
import winsound

alarm_time = input("alarm timr>>> ")
sound = "alarm_sound.wav"
repitions = 4

while True:
    date = time.time()
    current_time = date[11:16]
    if current_time == alarm_time:
        for i in range(repitions):
            winsound.playsound(sound,winsound.SND_ASYNC | winsound.SND_ALIAS)
            time.sleep(5)
            winsound.playSound(none,winsound.SND_ALIAS)
            break
            


# In[ ]:




