from tkinter import *
import time
import datetime
import threading
from tkinter import messagebox
import winsound  # For sound notifications on Windows

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

def check_alarms():
    """
    Periodically checks if any alarm should ring.
    """
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    for alarm_time in alarms:
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", f"Alarm ringing for {alarm_time}!")
            # Play a sound
            winsound.Beep(440, 1000)  # Beep for 1 second
            alarms.remove(alarm_time)  # Remove the alarm after it rings
            update_alarm_list()
    root.after(1000, check_alarms)  # Check alarms every second

def set_alarm():
    """
    Sets an alarm based on user input.
    """
    alarm_time = alarm_entry.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")  # Validate time format
        if alarm_time not in alarms:
            alarms.append(alarm_time)
            update_alarm_list()
            alarm_entry.delete(0, END)  # Clear the input field
        else:
            messagebox.showwarning("Duplicate Alarm", "This alarm is already set.")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")

def update_alarm_list():
    """
    Updates the displayed list of active alarms.
    """
    alarm_list_label.config(text="\n".join(alarms) if alarms else "No active alarms.")

# Create the main window
root = Tk()
root.title("Clock with Alarm")
root.geometry("400x300")

# Create labels for time and date
time_label = Label(root, font=("Arial", 48), fg="blue")
date_label = Label(root, font=("Arial", 20))

# Create alarm entry field and buttons
alarm_label = Label(root, text="Set Alarm (HH:MM):")
alarm_entry = Entry(root)
set_alarm_button = Button(root, text="Set Alarm", command=set_alarm)

# Create alarm list display
alarm_list_label = Label(root, text="No active alarms.", justify=LEFT, font=("Arial", 14))

# Arrange widgets using grid layout
time_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))
date_label.grid(row=1, column=0, columnspan=2)
alarm_label.grid(row=2, column=0, pady=(20, 0))
alarm_entry.grid(row=2, column=1, pady=(20, 0))
set_alarm_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))
alarm_list_label.grid(row=4, column=0, columnspan=2, pady=(20, 0))

# Initialize alarm list
alarms = []

# Start updating the clock and checking alarms
update_clock()
check_alarms()

# Start the GUI event loop
root.mainloop()
