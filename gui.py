import tkinter as tk
from tkinter import PhotoImage

from pomodoro.flavortext import flavortext
from timer import CountdownTimer as Cd
import flavortext as fl

session_count = 3
session_duration = 1
current_session = 25 * 60
all_sessions_complete = False

root = tk.Tk()
root.geometry('480x360')
root.title('Pomodoro Timer')

# Create timer instance
timer = Cd(session_duration)

# top text. will show which session is done
header = tk.Label(root, text=f'pomodoro 1/{session_count}', font=('Arial', 18))
header.pack(pady=15)

# flavortext display
# first, creates a container frame with fixed size
guide_frame = tk.Frame(root, width=410, height=160, relief='solid', bd=1)
guide_frame.pack()
guide_frame.pack_propagate(False)  # prevent frame from shrinking to fit the contents

# then, put the label inside the frame
guide = tk.Label(guide_frame, text=fl.tooltip(1), wraplength=405,
                 justify="left", font=('Arial', 12), anchor='nw')
guide.pack(fill='both', expand=True)

# display time remaining
text = tk.Label(root, text=timer.show(), font=('Arial', 18))
text.pack(pady=10)


# Function to reset everything
def reset_pomodoro():
    global current_session, all_sessions_complete
    current_session = 1
    all_sessions_complete = False
    timer.reset()
    header.config(text=f'pomodoro 1/{session_count}')
    guide.config(text=fl.tooltip(1))
    text.config(text=timer.show())


# Function to start timer and update GUI
def start_timer():
    global current_session, all_sessions_complete

    # If all sessions are complete, reset instead of starting
    if all_sessions_complete:
        reset_pomodoro()
        return

    timer.start()
    # Change to countdown flavortext when timer starts
    guide.config(text=fl.flavortext())
    update_display()


# Function to update the display
def update_display():
    global current_session, all_sessions_complete

    # Update the timer
    finished = timer.update()

    # Update timer display
    text.config(text=timer.show())

    # Schedule next update if timer is still running
    if not finished and timer.is_running():
        root.after(100, update_display)  # Update every 100ms
    elif finished:
        # Timer finished - move to next session or complete
        current_session += 1

        if current_session <= session_count:
            # Show rest instructions for short break
            guide.config(text=fl.tooltip(2))
            header.config(text=f'pomodoro {current_session}/{session_count}')
            timer.reset()  # Reset for next session
        else:
            # All sessions complete
            all_sessions_complete = True
            guide.config(text="All sessions complete! Great work!\n\n" +
                              "You must take a 30-minute rest before using this timer again.\n" +
                              "Click the tomato to reset when you're ready to start fresh.")
            header.config(text="Sessions Complete!")


# tomato button
timer_photo = PhotoImage(file='tomato.png')
timer_toggle = tk.Button(root, image=timer_photo, command=start_timer)
timer_toggle.pack()

root.mainloop()
