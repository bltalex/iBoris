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
        
        AsyncImage:
            source: 'https://thumbs.dreamstime.com/b/boris-johnson-president-uk-giving-speech-london-uk-brexit-promise-feb-boris-johnson-president-uk-giving-speech-171297714.jpg'
    
        BoxLayout:
            padding: 20
            spacing: 20
        
            size: 0.6, 0.3
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
            valign: 'center'


<SignInScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
    
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
            height_hint: 0.3
        
            Button:
                text: 'Settings'
            Button:
                text: 'Regional Danger'
                on_release: root.manager.current = 'threat'
            Button:
                text: 'Speaker'
                on_release: root.manager.current = 'speaker'
            Button:
                source: 'Home'
        
        Label:
            height_hint: 0.7
            text: 'Welcome home, the \\n place where you \\n should be!'
            color: 'black'
            font_size: 40
            halign: 'center'


<LeaveScreen>:
    CyanBoxLayout:
        orientation: 'vertical'

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
            text: 'go back'
            on_release: root.manager.current = 'welcome'


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

<ThreatScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
    
        CyanBoxLayout:
            Button:
                text: 'Back'
            
            Button:
                text: 'Home'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'home'
            
<SettingScreen>:
    CyanBoxLayout:
        orientation: 'vertical'
        
        
        
        
""")


class WelcomeScreen(Screen):
    pass


class SignInScreen(Screen):
    pass


class HomeScreen(Screen):
    pass

class LeaveScreen(Screen):
    pass

class BackgroundColor(BoxLayout):
    pass


class SpeakerScreen(Screen):

    def sound(self, threatlevel):  # store sound function within UI
        return sound(threatlevel)

    pass


class ThreatScreen(Screen):
  pass

class SettingScreen(Screen):
    pass


class MainApp(App):
    # create test app class, use inheritance from kivy's App
    def set_threatlevel(self, tl):
        self.threatlevel = tl
        return self

    def build(self):
        # create screen manager
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(SignInScreen(name="signin"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LeaveScreen(name="leave"))
        speaker = SpeakerScreen(name="speaker")
        speaker.threatlevel = self.threatlevel
        sm.add_widget(speaker)
        sm.add_widget(ThreatScreen(name="threat"))

        return sm







"""
Home Screen: 
cyan colourbackground: #B1FFF1;

/* boris-johnson-president-uk-giving-speech-london-uk-brexit-promise-feb-boris-johnson-president-uk-giving-speech-171297714 1 */


position: absolute;
width: 330px;
height: 283px;
left: 22px;
top: 51px;

background: url(boris-johnson-president-uk-giving-speech-london-uk-brexit-promise-feb-boris-johnson-president-uk-giving-speech-171297714.jpg);
filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
backdrop-filter: blur(4px);
/* Note: backdrop-filter has minimal browser support */

border-radius: 116px;
height: 283px;
width: 330px;
left: 22px;
top: 51px;
border-radius: 116px;

Rectangle 1:
height: 44px;
width: 130px;
left: 52px;
top: 391px;
border-radius: 25px;

Text Leave: 
height: 32px;
width: 101px;
left: 67px;
top: 397px;
border-radius: nullpx;

Rectangle 2
height: 44px;
width: 130px;
left: 192px;
top: 391px;
border-radius: 25px;



/* Remain */
height: 32px;
width: 101px;
left: 206px;
top: 397px;
border-radius: nullpx;

position: absolute;
width: 101px;
height: 32px;
left: 206px;
top: 397px;

font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 24px;
line-height: 28px;
text-align: center;

color: #484646;

/* Gray 3 */

border: 1px solid #828282;

/* Hello! This is iBoris, your virtual bodyguard! */


position: absolute;
width: 243px;
height: 113px;
left: 69px;
top: 491px;

font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 28px;
line-height: 33px;
text-align: center;

color: #484646;

letter-spacing: 0em;


/* Battery icons
FULL 

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

Status 4 bars 

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

Status 3 bars
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

/* You must stay at home page */
/*Exclamation mark*/
height: 180px;
width: 180px;
left: 98px;
top: 207px;
border-radius: 0px;
position: absolute;

/* You must stay at home! */


position: absolute;
width: 242px;
height: 101px;
left: 67px;
top: 447px;

font-family: Roboto;
font-style: normal;
font-weight: bold;
font-size: 36px;
line-height: 42px;
text-align: center;

color: #E2574C;

Battery 1 status
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


"""
