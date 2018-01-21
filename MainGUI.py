# Code written by '1 + One'

import re
import random
from FeatureExtractor import Emoji_text
import time
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.lang import Builder
from subprocess import call
import os
from subprocess import Popen

Builder.load_string('''

<ScrollableLabel>:
    text: app.text

    Label:
        text: root.text
        font_size: 22
        text_size: self.width, None
        color: [0,1,0,1]
        size_hint_y: None
        pos_hint: {"left":1, "top":1}
        height: self.texture_size[1]

<RootWidget>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10

        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: .1

            TextInput:
                id: txt_inpt
                background_color: [1,1,1,.1]
                foreground_color: [0,1,0,1]
                cursor_color: [0,1,0,1]
                size_hint_x: .8

            Button:
                id: btn
                text: 'Cam'
                size_hint_x: .1
                background_color: [.4, .4, .4, 1]
                color: [0, 1, 0, 1]
                on_press: app.runCamera()
                on_release: app.read()

            Button:
                id: btn
                text: 'Send'
                size_hint_x: .2
                background_color: [.4, .4, .4, 1]
                color: [0, 1, 0, 1]
                on_press: app.runStuff(txt_inpt.text)
                on_release: app.read()

        ScrollableLabel
''')

raspunsuri = (
    ("hi",                   ("Hey! Wassup?","Hey! How's it going?" )),
    ("bye",                    ("Bye Come Back soon !!!", "Bye Come Back soon !!!")),
)

'''pronume = {
    "eu sunt": "tu esti",
    "tu esti": "eu sunt",
    "eu": "tu",
    "tu": "eu",
    "meu": "tau",
    "tau": "meu",
    "al tau": "al meu",
    "al meu": "al tau",
    "noi": "voi",
    "voi": "noi",
    "am fost": "ai fost",
    "ai fost": "am fost",
    "as": "ai",
    "ai": "as",
    "am": "ai",
    "m-au": "te-au",
    "tine": "mine",
    "mine": "tine"
}
'''
random.seed()
print("Program start")


class RootWidget(BoxLayout):
    def displayImage(self):
        #self.ids.image.source=filename
         
        return Image(source=r'C:\Users\Nick007\AppData\Local\Programs\Python\Python36-32\sad.png')
       	#return Image(source=r"/mnt/2CB85A80B85A488A/Don't Open/Projects/Hackathon/emojis/anger.png")


class ScrollableLabel(ScrollView):
    pass

class Widget(BoxLayout):
    def selectImage(self,filename):
        self.ids.image.source=filename
        #return Image(source=r'C:\Users\Nick007\AppData\Local\Programs\Python\Python36-32\sad.png')
        

class MyApp(App):
    text = StringProperty('')
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('Archive.txt', 'w') as f:
            f.write('Welcome to Emoji Predictor' + '\n\n')
            #os.system('start sad.png')
            #f.write()
            
            f.close()
        with open('Archive.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    def runStuff(self, inpt):
        try:
            user = re.split('[\.!?]', inpt.lower().rstrip('.!?'))
            full_reply = ' '
            for sentence in user:
                sentence=sentence.lstrip()
                for pattern in raspunsuri:
                    if re.match(pattern[0], sentence):
                        wildcards = filter(bool, re.split(pattern[0], sentence))
                        # replace pronouns
                        wildcards = [' '.join(pronume.get(word, word) for word in wildcard.split()) for wildcard in wildcards]
                        response = random.choice(pattern[1])
                        response = response.format(*wildcards)
                        full_reply += response + ' '
                        break
                print(full_reply)
                time.sleep(0.5)
                with open('Archive.txt', 'a') as f:
                    f.write('> ' + inpt + '\n')
                    f.write(str(full_reply) + '\n')
                    f.close()
        except:
            pass       

    def runCamera(self):
        try:
            Popen('python Camera.py')
        except:
            pass

    def read(self):
        with open('Archive.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    def build(self):
        #self.ids.image.source=r'C:\Users\Nick007\AppData\Local\Programs\Python\Python36-32\sad.png'
        
        Image(source=r'C:\Users\Nick007\AppData\Local\Programs\Python\Python36-32\sad.png')
        return RootWidget()

if __name__ == '__main__':
    app = MyApp()
    app.run()
