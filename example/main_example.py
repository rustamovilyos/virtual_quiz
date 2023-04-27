import datetime
import os.path
import subprocess
import sys
import time
import tkinter as tk
import cv2

import utils
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1000x600+180+60")

        self.login_button_main_window = utils.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=700, y=300)

        self.registration_button_main_window = utils.get_button(self.main_window, 'registration', 'gray',
                                                                self.registration, fg="black")
        self.registration_button_main_window.place(x=700, y=400)

        self.webcam_label = utils.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=650, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = "./db"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if "cap" not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        self.most_recent_capture_arr = frame

        image_1 = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(image_1)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        unknown_img_path = './.tmp.jpg'

        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

        output = str(subprocess.check_output(["face_recognition", self.db_dir, unknown_img_path]))

        name = output.split(',')[1][:-5]
        # print(name)
        if name in ["unknown_person", "no_persons_found"]:
            utils.msg_box('Error❗', 'Unknown user.\nPlease register as a new user or try again!')
        else:
            utils.msg_box('Welcome back', f'Welcome {name}\n'
                                          f'After a while you can run the test.')
            with open(self.log_path, 'a') as f:
                f.write(f'User:{name}\n'
                        f'Time:{datetime.datetime.now()}\n\n')
                f.close()
            self.main_window.destroy()
            cv2.destroyAllWindows()
            # import subjects
            subject = __import__('subjects')
            subject

    def registration(self):
        self.registration_window = tk.Toplevel(self.main_window)
        self.registration_window.geometry("1000x650+190+70")

        self.accept_button_registration_window = utils.get_button(self.registration_window, 'Accept', 'green',
                                                                  self.accept_registration_user)
        self.accept_button_registration_window.place(x=715, y=300)

        self.try_again_button_registration_window = utils.get_button(self.registration_window, 'Try again', 'red',
                                                                     self.try_again_registration_user)
        self.try_again_button_registration_window.place(x=715, y=400)

        self.capture_label = utils.get_img_label(self.registration_window)
        self.capture_label.place(x=10, y=0, width=650, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_registration_user = utils.get_entry_text(self.registration_window)
        self.entry_text_registration_user.place(x=700, y=150)

        self.text_label_registration_user = utils.get_text_label(self.registration_window, 'Please,\ninput your name:')
        self.text_label_registration_user.place(x=700, y=50)

    def try_again_registration_user(self):
        self.registration_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.registration_capture = self.most_recent_capture_arr.copy()

    def accept_registration_user(self):
        name = self.entry_text_registration_user.get(1.0, "end-1c")
        cv2.imwrite(os.path.join(self.db_dir, f"{name}.jpg"), self.registration_capture)
        utils.msg_box('Success!', 'User was registered successfully!')

        self.registration_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
