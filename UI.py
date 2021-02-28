"""
File for app UI and interactivity
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from speech import sound




Builder.load_string("""
<CyanBoxLayout@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.694, 1, 0.945, 1
        Rectangle:
            # self here refers to the widget i.e BoxLayout
            pos: self.pos
            size: self.size


<WelcomeScreen>:

    CyanBoxLayout:
        orientation: 'vertical'
        padding: 20
        
        AsyncImage:
            source: 'https://thumbs.dreamstime.com/b/boris-johnson-president-uk-giving-speech-london-uk-brexit-promise-feb-boris-johnson-president-uk-giving-speech-171297714.jpg'
    
        BoxLayout:
            padding: 20
            spacing: 20
        
            Button:
                text: 'Leave'
                on_release: root.manager.current = 'leave'
            Button:
                text: 'Remain'
                on_release: root.manager.current = 'signin'
        
        Label:
            text: 'Hello, this is \\n iBoris, your virtual \\nbodyguard!'
            color: 'black'
            font_size: 40
            text_size: self.size
            halign: 'center'
            valign: 'top'


<LeaveScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
        padding: 20

        Image:
            source: 'img\exclamation-mark.png'

        Label:
            text: 'You MUST stay \\nat home!'
            color: 'red'
            font_size: 40
            text_size: self.size
            halign: 'center'
            valign: 'center'

            
        Button:
            text: 'Back'
            on_release: root.manager.current = 'welcome'
            size_hint: .4, .3
            pos_hint: {'center_x': .5, 'center_y': .5}


<SignInScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
        padding: 20
    
        Label:
            text: 'iBoris'
            font_size: 60
            color: 'black'
            
        TextInput:
            padding: 20
            text: 'Username'
            multiline: False
        
        TextInput:
            padding: 20
            text: 'Password'
            password: True
            multiline: False
        
        Button:
            text: 'Sign In'
            background_color: 0.28, 0.27, 0.27, 1
            on_release: root.manager.current = 'home'


<HomeScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
        
        
        BoxLayout:
        
            Button:
                text: 'Settings'
            Button:
                text: 'Threat Level'
                on_release: root.manager.current = 'threat'
            Button:
                text: 'Speaker'
                on_release: root.manager.current = 'speaker'
        
        Label:
            text: 'Welcome home, the \\n place where you \\n should be!'
            color: 'black'
            font_size: 40
            halign: 'center'
        
        CyanBoxLayout:
            Button:
                text: 'Back'
            
            Button:
                text: 'Home'
                on_release: root.manager.current = 'home'


<SpeakerScreen>
    CyanBoxLayout:
        orientation: 'vertical'
        
        Button:
            background_normal: ''
            background_color: 1, 0, 0, 1
            border: 20, 20 ,20 ,20
            on_release: root.sound(root.threatlevel)
        
        Label:
            text: "Press me to hear the\\nannouncements in my sexy\\nvoice!"
            halign: 'center'
            color: 'black'
            font_size: 40
            size_hint: 
        
        CyanBoxLayout:
            Button:
                text: 'Threat Level'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'threat'
            
            Button:
                text: 'Home'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'home'

<ThreatScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
        
        Button:
            text: 'Press here to hear my speech!'
            font_size: 20
            on_release: root.manager.current = 'speaker'
        
        Label:
            text: f'There are {root.cases} new cases in the UK\\n\
                    The weekly variation between last week and this week is {root.change}\\n\
                    The threatlevel is {root.threatlevel}\\n\
                    Better to stay at home!'
            halign: 'center'
            font_size: 20
            color: 'black'
    
        CyanBoxLayout:
            Button:
                text: 'Back'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'home'
            
            Button:
                text: 'Home'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'home'
""")


class WelcomeScreen(Screen):
    pass


class LeaveScreen(Screen):
    pass


class SignInScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class BackgroundColor(BoxLayout):
    pass


class SpeakerScreen(Screen):

    def sound(self, threatlevel):  # store sound function within UI
        return sound(threatlevel)

    pass


class ThreatScreen(Screen):
    cases = new_cases
    change = weekly_change
    threatlevel = TL

    pass


class MainApp(App):
    # create test app class, use inheritance from kivy's App
    def set_data(self, cases, change, tl):
        self.cases, self.change, self.threatlevel = cases, change, tl
        return self

    def build(self):
        # create screen manager
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(LeaveScreen(name="leave"))
        sm.add_widget(SignInScreen(name="signin"))
        sm.add_widget(HomeScreen(name="home"))

        speaker = SpeakerScreen(name="speaker")
        speaker.threatlevel = self.threatlevel
        sm.add_widget(speaker)

        threat = ThreatScreen(name="threat")
        threat.cases, threat.change, threat.threatlevel = self.cases, self.change, self.threatlevel
        sm.add_widget(threat)

        return sm
