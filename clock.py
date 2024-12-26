from tkinter import *
import time
import datetime

def get_time():
    """
    Fetches the current time and date.

    Returns:
        tuple: A tuple containing the current time (string) and date (string).
    """
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    return current_time, current_date

def update_clock():
    """
    Updates the displayed time and date on the GUI.
    """
    current_time, current_date = get_time()
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_clock)  # Schedule next update after 1 second

def set_alarm():
    """
    Sets an alarm based on user input.
    """
    alarm_time = alarm_entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        while True:
            now = datetime.datetime.now()
            if now.hour == alarm_hour and now.minute == alarm_minute:
                print("Alarm ringing!")
                # Add your alarm sound or notification logic here
                break
            time.sleep(1)
    except ValueError:
        print("Invalid alarm time format. Please use HH:MM.")

# Create the main window
root = Tk()
root.title("Clock with Alarm")

# Create labels for time and date
time_label = Label(root, font=("Arial", 48), fg="blue")
date_label = Label(root, font=("Arial", 20))

# Create alarm entry field
alarm_label = Label(root, text="Set Alarm (HH:MM):")
alarm_entry = Entry(root)
set_alarm_button = Button(root, text="Set Alarm", command=set_alarm)

# Arrange widgets using grid layout
time_label.grid(row=0, column=0, columnspan=2)
date_label.grid(row=1, column=0, columnspan=2)
alarm_label.grid(row=2, column=0)
alarm_entry.grid(row=2, column=1)
set_alarm_button.grid(row=3, column=0, columnspan=2)

# Initial update of clock
update_clock()

# Start the GUI event loop
root.mainloop()
