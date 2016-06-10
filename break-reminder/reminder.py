import time
import multiprocessing
import itertools

import webview
import remi.gui as gui
import remi.server as server
from remi import start, App


SCHEDULE = [{'pause_before': 50,
             'exposition_time': 10,
             'url': 'static/reminders/close_yo_eyes.html'},
            {'pause_before': 50,
             'exposition_time': 10,
             'url': 'static/reminders/blink.html'}
            ]


class GUIEditor(App):
    def __init__(self, *args):
        super(GUIEditor, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=500, height=400)
        self.lbl = gui.Label('Hello')
        self.bt = gui.Button('Press me?')

        self.bt.set_on_click_listener(self, 'on_button_pressed')

        container.append(self.lbl)
        container.append(self.bt)

        return container

    def on_button_pressed(self):
        self.lbl.set_text('Spejson przejmuje ten program')
        self.bt.set_text('Walu pilnuje butona')


class Reminder:
    def __init__(self, schedule):
        self.schedule = schedule

    def run(self):
        for element in itertools.cycle(self.schedule):
            time.sleep(element['pause_before'])
            self.show_reminder(element['url'], 'Elo',
                               element['exposition_time'])

    def show_reminder(self, url, title, exposition_time):
        p = multiprocessing.Process(target=self.open_reminder,
                                    args=(url, title))
        p.start()
        p.join(exposition_time)
        if p.is_alive():
            p.terminate()

    @staticmethod
    def open_reminder(reminder_url, title):
        webview.create_window(title, reminder_url)

if __name__ == "__main__":
    server.StandaloneServer(GUIEditor, start=True)
