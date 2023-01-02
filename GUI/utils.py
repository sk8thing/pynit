import os
from qt_material import apply_stylesheet

def load_theme(app):
    try:
        apply_stylesheet(app, theme="dark_amber.xml", extra={'font_family': 'Consolas'})
        stylesheet = app.styleSheet()
        absolute_path = os.path.dirname(__file__)
        with open(os.path.join(absolute_path, "ui/themes/style.css")) as file:
            app.setStyleSheet(stylesheet + file.read())
    except:
        raise Exception("Couldn't load theme.")
