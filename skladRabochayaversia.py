#Для преобразования вашего Kivy-кода из декларативного (язык разметки KV) в императивный (на языке Python) код, вам нужно будет создать все элементы интерфейса и их свойства программно. Вот пример, как это можно сделать:

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

from kivymd.uix.datatables import MDDataTable
import csv
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen




from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout


from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
import csv
from kivymd.uix.scrollview import MDScrollView,ScrollView
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import pandas as pd 





class MainApp(MDApp):
    def build(self):
        
        self.mds= MDScrollView( pos_hint={"center_x": .1, "center_y": .4}, size_hint_y=(0.7),size=(350,300))
        self.nav_drawer = MDNavigationDrawer()
        self.screen_manager = ScreenManager()

        # Создание экранов
        self.create_screens()

        # Создание панели навигации
        nav_layout = MDNavigationLayout()
        nav_layout.add_widget(self.nav_drawer)
        nav_layout.add_widget(self.screen_manager)

        # Создание верхней панели приложения
        top_app_bar = MDTopAppBar(
            title="Склад",
            left_action_items=[["menu", lambda x: self.nav_drawer.set_state("open")]]
        )

        # Создание основного макета
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(top_app_bar)
        layout.add_widget(nav_layout)

        return layout

    def create_screens(self):
        # Экран 1
        scr1 = Screen(name="scr 1")
        box_layout = MDBoxLayout( size_hint_x=.8, pos_hint={"center_x": .5, "center_y": .5})

        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            data = [row for row in csvreader]

        # Создаем MDDataTable и передаем данные для отображения
        self.table = MDScreen(MDDataTable(
        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        size_hint=(0.9, 0.6),
            column_data=[("Name", dp(40)), ("dataInput", dp(40)), ("articul", dp(40)), ("price", dp(40)), ("amount", dp(40)), ("summCost", dp(40))],
            row_data=data
        ))

        # Создаем текстовое поле и сохраняем его как атрибут класса
        self.txt = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            on_text_validate=self.on_text_entered,
            hint_text="После ввода нажмите Enter"
        )
        
        self.table.add_widget(self.txt)
                
        box_layout.add_widget(self.table)
  
        scr1.add_widget(box_layout)
        self.screen_manager.add_widget(scr1)
        
        
        
        
        
        
        scr2 = Screen(name="scr 2")
        box_layout = MDBoxLayout( size_hint_x=.9, pos_hint={"center_x": .5, "center_y": .6})
              
      
        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            data = [row for row in csvreader]


        # Создаем текстовое поле и сохраняем его как атрибут класса
        self.txt = MDTextField(
            pos_hint={'center_x': 0.9, 'center_y': 0.73},
        on_text_validate=self.on_text_enterd,
            hint_text="Ввод данных поиска"
        )
        
        self.blw= MDLabel( pos_hint={'center_x': 0.1, 'center_y': 0.5},
        text = "Результат вашего поиска ",size_hint_y=None)
    #    self.bl = bl
    #    self.table.add_widget(self.blw)
        self.mds.add_widget(self.blw)
 #       self.table.add_widget(self.txt)
        
        

        box_layout.add_widget(self.txt)
        box_layout.add_widget(self.mds)
#        box_layout.add_widget(text_field_c)
#        box_layout.add_widget(label)
#        self.mds.add_widget(box_layout)
        
        scr2.add_widget(box_layout)
        
        #(box_layout)
        self.screen_manager.add_widget(scr2)
        
      
            #new
        scr3 = Screen(name="scr 3")
        box_layout = MDBoxLayout(size_hint_x = .9, pos_hint = {"center_x" : .5, "center_y" : .6})    
        
        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            data = [row for row in csvreader]

        
        self.table = MDScreen(MDDataTable(
        pos_hint={'center_x': 0.5, 'center_y': 0.4},
        size_hint=(0.9, 0.6),
            column_data=[("Name", dp(40)), ("dataInput", dp(40)), ("articul", dp(40)), ("price", dp(40)), ("amount", dp(40)), ("summCost", dp(40))],
            row_data=data
        ))

        # Создаем текстовое поле и сохраняем его как атрибут класса
        self.txt = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            on_text_validate=self.on_text_ented,
            hint_text="После ввода нажмите Enter"
        )
        
  
        
        self.table.add_widget(self.txt)
                
        box_layout.add_widget(self.table)
        
        
        scr3.add_widget(box_layout)
        self.screen_manager.add_widget(scr3)
              
                 
                    
                          

        # Добавление элементов в навигационное меню
        self.nav_drawer.add_widget(OneLineListItem(
            text="Добавление",
            on_press=lambda x: self.change_screen("scr 1")
        ))
        
        self.nav_drawer.add_widget(OneLineListItem(
            text="Поиск",
            on_press=lambda x: self.change_screen("scr 2")
        ))
        
        self.nav_drawer.add_widget(OneLineListItem(
            text="Удаление",
            on_press=lambda x: self.change_screen("scr 3")
        ))
#        return self.screen_manager

    def change_screen(self, screen_name):
        self.nav_drawer.set_state("close")
        self.screen_manager.current = screen_name




    def on_text_ented(self, instance_textfield):
        df = pd.read_csv("data.csv")
        input_values = instance_textfield.text.split()  # Получаем список значений

    # Удаляем строки, где значение в столбце 'name' соответствует любому значению из input_values
        df = df[~df['name'].isin(input_values)]  # Используем ~ для фильтрации

        df.to_csv('data.csv', index=False)  # Сохраняем DataFrame обратно в CSV
        
        
        
        
        
        
        
    def on_text_entered(self, instance_textfield):
        # Получаем текст из текстового поля
        input_text = instance_textfield.text.split()
        
        # Открываем файл CSV в режиме добавления
        with open('data.csv', 'a', newline = '', encoding='utf-8') as f_object:
            writer_object = csv.writer(f_object)
            
            # Записываем введенный текст в файл (например, как новую строку)
            writer_object.writerow(input_text)  # Здесь вы можете изменить формат записи
            
        # Очищаем текстовое поле после записи
        instance_textfield.text = ''
        
        
    def on_text_enterd(self, instance_textfield):
        data = pd.read_csv("data.csv") 
        df = pd.DataFrame(data)
    
        filtered_data = df[df['name'] == instance_textfield.text]
        result_string = filtered_data.to_string(index=False)  # Преобразование DataFrame в строку
    
        self.blw.text = result_string  # Установка строки в MDLabel
        

  
        

if __name__ == "__main__":
    MainApp().run()


#В этом коде мы создаем интерфейс приложения с помощью Python вместо KV-файла. Мы создаем экземпляры всех необходимых виджетов и настраиваем их свойства и события. События on_press для элементов списка вызывают метод change_screen, который управляет переходами между экранами.