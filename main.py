from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from chatterbot import ChatBot


class UserInput(MDCard):
    text = StringProperty()
    font_size= NumericProperty()

class BotResponce(MDCard):
    text = StringProperty()
    font_size= NumericProperty()

class ChatScreen(Screen):
    chat_area = ObjectProperty()
    message = ObjectProperty()

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.chatbot = ChatBot("Donna")

    def send_message(self):
        self.user_input = self.ids.message.text
        self.ids.message.text = ""
        length = len(self.user_input)

        if length >= 40:
            self.ids.chat_area.add_widget(
                UserInput(text=self.user_input, font_size=17, height = length)
            )
        else:
            self.ids.chat_area.add_widget(
                UserInput(text=self.user_input, font_size=17)
            )
        
    def bot_response(self):
        response = self.chatbot.get_response(self.user_input)
        length = len(str(response))

        if length >= 40:
            self.ids.chat_area.add_widget(
                BotResponce(text="{}".format(response), font_size=17, height=length)
            )
        else:
            self.ids.chat_area.add_widget(
                BotResponce(text="{}".format(response), font_size=17)
            )




class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'Teal'
        sm = ScreenManager()
        sm.add_widget(ChatScreen(name='chat'))
        return sm
    
if __name__=='__main__':
    ChatApp().run()