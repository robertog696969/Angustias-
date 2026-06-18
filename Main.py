from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation

class Pasillo3D(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Fondo de pasillo (colores oscuros estilo 3D)
            Color(0.1, 0.1, 0.2, 1)
            Rectangle(pos=(0, 0), size=(2000, 2000))
            # Una "puerta" sencilla en el centro
            Color(0.6, 0.3, 0.1, 1)
            Rectangle(pos=(400, 300), size=(200, 400))

class MiApp(MDApp):
    def build(self):
        screen = MDScreen()
        self.escenario = Pasillo3D()
        
        self.btn = MDRaisedButton(
            text="ABRIR PUERTA",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_release=self.actualizar
        )
        
        screen.add_widget(self.escenario)
        screen.add_widget(self.btn)
        return screen

    def actualizar(self, instance):
        self.btn.text = "ACTUALIZANDO..."
        self.btn.disabled = True
        # Animación de salida
        anim = Animation(opacity=0, duration=1.5)
        anim.start(self.escenario)

MiApp().run()
