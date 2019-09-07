#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from RotatedArray import GetRotatedArray
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

kv = Builder.load_string('''

BoxLayout:
    padding: 10
    spacing: 10
    orientation:'vertical'
    gri: gri.__self__
    
    BoxLayout:
        padding:10
        spacing:10
        size_hint_y:0.1
        orientation: 'horizontal'
    
        TextInput:
            size_hint_x: 0.8
            hint_text: 'input side请'
            #font_name: 'HYNangong'
            font_size: '32sp'
            multiline: False
            on_text_validate: app.launch()
            id: sideInput
        
        Button:
            size_hint_x: 0.2
            text: 'Launch'
            on_release: app.launch()
        
    GridLayout:
        size_hint_y: 0.9
        id:gri
        
            
        
''')

class RotatedArrayApp(App):
    def build(self):
        # display a button with the text : Hello QPython 
        return kv
    
    def launch(self):
        print 'app.launch()'
        side = int(kv.ids['sideInput'].text)
        print type(side)
        print side
        if (side is not '0'):
            GPA = GetRotatedArray()
            GPA2 = GPA.gen(int(side))
            #gri = kv.ids['gri']
            #gri.cols = side
            #gri.rows = side
            #print type(gri)
            #for Num in GPA2.array:
                #Num.getPrint()
                #gri.add_widget(Label(text=str(Num.num)))
            #gri.add_widget(Label(text='test'))
            gri = kv.gri
            gri.clear_widgets()
            gri.cols = side
            for i in range(side):
                for j in range(side):
                    for Num in GPA2.array:
                        if (Num.x == j) and (Num.y == i):
                            gri.add_widget(Label(font_name='HYNangong', text=str(Num.num)))
            

if __name__ == '__main__':
    RotatedArrayApp().run()









