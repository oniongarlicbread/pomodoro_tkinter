import tkinter as tk
from tkinter import PhotoImage

from pomodoro.flavortext import flavortext
from timer import CountdownTimer as Cd
import flavortext as fl

session_count = 3
session_duration = 5

root = tk.Tk()
root.geometry('480x360')
root.title('Pomodoro Timer')

# Create timer instance
timer = Cd(session_duration)

# top text. will show which session is done
header = tk.Label(root, text=f'pomodoro 0/{session_count}', font=('Arial', 18))
header.pack(pady=15)

# flavortext display
# first, creates a container frame with fixed size
guide_frame = tk.Frame(root, width=400, height=160, relief='solid', bd=1)
guide_frame.pack()
guide_frame.pack_propagate(False)  # prevent frame from shrinking to fit the contents

# then, put the label inside the frame
guide = tk.Label(guide_frame, text=fl.tooltip(1), wraplength=400,
                 justify="left", font=('Arial', 12), anchor='nw')
guide.pack(fill='both', expand=True, padx=5, pady=5)

# display time remaining
text = tk.Label(root, text=timer.show(), font=('Arial', 18))
text.pack(pady=10)

current_session = 1

# Function to start timer and update GUI
def start_timer():
    global current_session
    timer.start()
    guide.config(text=fl.flavortext())
    update_display()

# Function to update the display
def update_display():
    finished = timer.update()
    text.config(text=timer.show())

    if not finished and timer.is_running():
        root.after(100, update_display)
    elif finished:
        global current_session
        current_session += 1

        if current_session <= session_count:
            # Show next session tooltip
            guide.config(text=fl.tooltip(2))  # Rest instructions
            header.config(text=f'pomodoro {current_session}/{session_count}')
        else:
            guide.config(text="All sessions complete! Great work!")


# tomato button
timer_photo = PhotoImage(file='tomato.png')
timer_toggle = tk.Button(root, image=timer_photo, command=start_timer)
timer_toggle.pack()

root.mainloop()