Arabic Speech to text recognition:

Notes:

-You can download the code from the (speech to text AR.py) file.
-After you run the code say something then wait for a bit for the text to appear (after the text appears, you need to run the code one more time if you want your speech to get recognized again). 

instructions:

1-Open Jubyter Notebook and create a new file.

2-Install the required libraries by typing the two lines below:

 !pip install speechrecognition
 !pip install pyAudio
 
The Speechrecognition library acts like a cover for sevral APIs that are built for speech recognition.
The Pyaudio library allows you to record sounds.

3- Type the following three lines:

   import  speech_recognition as sr
   r=sr.Recognizer()
   with sr.Microphone() as src:
   
   sr is a short for speech recognition.
   r is the recognizer variable.
   src is a short for the source which is the audio that the micorophone will catch.

4-Write the two lines of code below:

    print('قل شيئاً..')
    audio=r.listen(src)
    
The first line informs the user to start speaking.

In the second line, the r (recognizer) will listen to the source (the user sound).

5-Lastly, type these 7 lines:

 try:
    t=r.recognize_google(audio,language='ar-AR')
				
    print(t)
    
except sr.UnknownValueError as U:

    print(U)
				
except sr.RequestError as R:

    print(R)

The variable t holds the text that got extracted from the audio variable through the recognizer in Arabic language.




   

 
 






