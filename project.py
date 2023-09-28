import tkinter
import pygame
import pymsgbox

# python -m PyInstaller --onefile project.py

# python -m pip install auto-py-to-exe
# python -m auto_py_to_exe


class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # Initialize pygame for sounds
        pygame.mixer.init()
        self.sound_alarm = pygame.mixer.Sound(
            r"C:\Users\gabriela\Documents\Cursos online\CS50's Introduction to Programming with Python\final_project\sound.mp3"
        )  # Modify chosen sound (.mp3)

        self.title_label = tkinter.Label(
            master, text="Pomodoro Timer", font=("Helvetica", 22, "bold")
        )
        self.title_label.pack(pady=5)

        self.phase_label = tkinter.Label(master, font=("Times", 18))
        self.phase_label.pack(pady=1)

        # Button font and size
        button_font = ("Helvetica", 10)

        self.start_button = tkinter.Button(
            master, text="Start", command=self.start_timer, font=button_font
        )
        self.start_button.pack(pady=10)

        self.stop_button = tkinter.Button(
            master,
            text="Stop",
            command=self.stop_timer,
            state=tkinter.DISABLED,
            font=button_font,
        )
        self.stop_button.pack(pady=10)

        self.reset_phase_button = tkinter.Button(
            master,
            text="Reset Phase",
            command=self.reset_phase_timer,
            state=tkinter.DISABLED,
            font=button_font,
        )
        self.reset_phase_button.pack(pady=10)

        self.reset_button = tkinter.Button(
            master,
            text="Reset",
            command=self.reset_timer,
            state=tkinter.DISABLED,
            font=button_font,
        )
        self.reset_button.pack(pady=10)

        self.timer_label = tkinter.Label(master, font=("Times", 24, "bold"))
        self.timer_label.pack()

        # Toggle button to keep timer window in the foreground
        self.topmost_button = tkinter.Button(
            master,
            text="❗",
            font=("Helvetica", 10),
            command=self.toggle_topmost,
            fg="red",
        )
        self.topmost_enabled = False  # Initial state (Background)
        self.topmost_button.pack(pady=10)

        self.pomodoro_length = 25 * 60  # 25 minutes
        self.short_break_length = 5 * 60  # 5 minutes
        self.long_break_length = 15 * 60  # 15 minutes

        self.pomodoros_completed = 0
        self.timer_running = False
        self.current_timer = self.pomodoro_length
        self.timeformat()
        self.current_phase = f"Phase {self.pomodoros_completed + 1}"
        self.phase_label.config(text=self.current_phase)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tkinter.DISABLED)
            self.stop_button.config(state=tkinter.NORMAL)
            self.reset_phase_button.config(state=tkinter.NORMAL)
            self.reset_button.config(state=tkinter.NORMAL)
            self.timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state=tkinter.NORMAL)
            self.stop_button.config(state=tkinter.DISABLED)
            self.reset_phase_button.config(state=tkinter.NORMAL)
            self.reset_button.config(state=tkinter.NORMAL)

    def reset_phase_timer(self):
        if self.timer_running:
            self.stop_timer()
        if self.current_phase == "Short Break":
            self.current_timer = self.short_break_length
        elif self.current_phase == "Long Break":
            self.current_timer = self.long_break_length
        else:
            self.current_timer = self.pomodoro_length
        self.timeformat()

    def reset_timer(self):
        self.pomodoros_completed = 0  # Reset Pomodoros completed count
        if self.timer_running:
            self.stop_timer()
        self.current_timer = self.pomodoro_length
        self.timeformat()
        self.current_phase = f"Phase {self.pomodoros_completed + 1}"
        self.phase_label.config(text=self.current_phase)

    def timeformat(self):
        minutes, seconds = divmod(self.current_timer, 60)
        timeformat = "{:02d}:{:02d}".format(minutes, seconds)
        self.timer_label.config(text=timeformat)

    def timer(self):
        if self.timer_running:
            self.timeformat()

            if self.current_timer >= 0:
                self.current_timer -= 1
                self.master.after(1000, self.timer)
            else:
                self.timer_running = False
                self.start_button.config(state=tkinter.NORMAL)
                self.stop_button.config(state=tkinter.DISABLED)
                self.reset_phase_button.config(state=tkinter.DISABLED)
                self.reset_button.config(state=tkinter.NORMAL)
                self.sound_alarm.play()  # Play preset sound when timer reaches zero
                self.handle_phase()

    def handle_phase(self):
        if self.current_phase == f"Phase {self.pomodoros_completed + 1}":
            self.pomodoros_completed += 1

            if self.pomodoros_completed % 4 == 0:
                self.current_timer = self.long_break_length
                self.current_phase = "Long Break"
            else:
                self.current_timer = self.short_break_length
                self.current_phase = "Short Break"

        elif self.current_phase == "Short Break":
            self.current_timer = self.pomodoro_length
            self.current_phase = f"Phase {self.pomodoros_completed + 1}"
        elif self.current_phase == "Long Break":
            self.current_timer = self.pomodoro_length
            self.current_phase = f"Phase {self.pomodoros_completed + 1}"
        self.phase_label.config(text=self.current_phase)
        self.timeformat()

    def toggle_topmost(self):
        if self.topmost_enabled:
            pymsgbox.alert("Stay in front DISABLED.")
            self.master.wm_attributes("-topmost", 0)
            self.topmost_enabled = False
        else:
            pymsgbox.alert("Stay in front ENABLED.")
            self.master.wm_attributes("-topmost", 1)
            self.topmost_enabled = True


if __name__ == "__main__":
    root = tkinter.Tk()
    # root.wm_attributes("-topmost", 1)
    timer = PomodoroTimer(root)
    root.mainloop()
