from __future__ import print_function	# For Py2/3 compatibility
import eel
import os
import clipboard

from gtts import gTTS 

# keyboard out put
#mytext =  clipboard.paste()
#keyboard = Controller()

# TTS set up code
language = 'en'



# Set web files folder

eel.init('web')


@eel.expose                         # Expose this function to Javascript
def text_to_keys(x):
    os.system('xdotool type '+'\''+x+'\'' )
    #keyboard.type(x)
    print(x)

#eel.say_hello_js('Python World!') 

@eel.expose                         # Expose this function to Javascript
def get_text():
    #os.system('python stt.py')
    mytext =   clipboard.paste()
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    os.system("rm web/TTS.mp3")
    myobj.save("web/TTS.mp3") 
    #os.system("mpg123 TTS.mp3") 





#@eel.expose                         # Expose this function to Javascript
#def get_text():
#    stream = os.popen('xclip -o')
#    text  = stream.read()
#    eel.store_this_text(text)
#    print(text)
#@eel.expose                         # Expose this function to Javascript
#def get_text():
   # os.system('xclip -o | say.sh')
   # os.system('sh say.sh')
   #os.system("python stt.py")
   #os.system("rm /tmp/TTS.mp3")
   #myobj.save("TTS.mp3") 
   #os.system("rm /tmp/TTS.mp3")
 



eel.start('hello.html', size=(200, 200))    # Start
