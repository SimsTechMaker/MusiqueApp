from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget




class WidegetsExma(GridLayout):
    my_text = StringProperty("0")

    i = 0
    activ_cont = BooleanProperty(False)
    value_slider = NumericProperty(50)
    text_input = StringProperty("")

    def text_ok(self,text):
        self.text_input = text.text

    def switch_activ(self,switch):
        print(str(switch.active))
        print(self.value_slider)

    def Slider_activ(self, slider):
        print(self.value_slider)
        self.value_slider = int(slider.value)


    def toggel(self, wideget):
        if wideget.state == "normal":
            wideget.text = "OFF"
            self.activ_cont = False
        else:
            wideget.text = "ON"
            self.activ_cont = True
        print(wideget.state)


    def clic_buton(self):
        if self.activ_cont:
            self.i +=1
        print("bonjour le monde")
        self.my_text = str(self.i)


class StackLayoutLab(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayoutLab, self).__init__(**kwargs)
        dim = dp(100)
        for i in range(0, 100):
            b = Button(text=str(i), size_hint=(None, None), size=(dim, dim))
            self.add_widget(b)


class GridLayoutLab(GridLayout):
    pass


class AnchorLayoutLap(AnchorLayout):
    pass


class BoxLayoutLab(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A", color="#c23616")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.orientation = "vertical"
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        """


class MainWidget(Widget):
    pass


class ThelabApp(App):
    pass


class TheRoot():
    def __init__(self):
        self.nom = 20
        self.prenom = 52
    def __str__(self):
        var = self.nom

a = TheRoot

print(a)


ThelabApp().run()
