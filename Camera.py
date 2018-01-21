from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from subprocess import Popen
import os

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        #Emoji_text=''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        camera.export_to_png("z_Image.png")
        print("Captured")
        try:
            Popen('python FeatureExtractor.py')
            time.sleep(2)
            from FeatureExtractor import Emoji_text
            if Emoji_text == "happiness":
                os.system('start happy.png')
            elif Emoji_text =="neutral":
                os.system('start neutral.png')
            elif Emoji_text =="anger":
                os.system('start anger.png')
            elif Emoji_text =="surprise":
                os.system('start surprise.png')
            elif Emoji_text =="contempt":
                os.system('start contempt.png')
            elif Emoji_text =="fear":
                os.system('start fear.png')
            elif Emoji_text =="sadness":
                os.system('start sad.png')
            else:   #disgust
                os.system('start disgust.png')
            
        except Exception as e:
            print(e)
            
class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
