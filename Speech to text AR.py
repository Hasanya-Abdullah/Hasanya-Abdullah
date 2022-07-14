#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install speechrecognition')
get_ipython().system('pip install gtts')
get_ipython().system('pip install pyAudio')
        
    
        


# In[8]:


from gtts import gTTS
from playsound import playsound 
import  speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as src:
    print('قل شيئاً..')
    audio=r.listen(src)
try:
    t=r.recognize_google(audio,language='ar-AR')
    print(t)
    f=open('text.txt','a',encoding='utf-8')
    f.writelines(t+'\n')
    f.close()
    obj=gTTS(text=t,lang='ar',slow=False)
except sr.UnknownValueError as U:
    print(U)
except sr.RequestError as R:
    print(R)
    


# In[ ]:





# In[ ]:




