# image_property.py
import os
import tkinter as tk
import pygubu


class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('image_property.ui')

        #3: Set images path before creating any widget
        img_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'img')
        img_path = os.path.abspath(img_path)
        builder.add_resource_path(img_path)

        #4: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)

        self.set_title('Image property')


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()
