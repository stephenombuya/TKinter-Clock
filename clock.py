from tkinter import *
import datetime
import platform
import threading
from tkinter import messagebox

# Check the operating system for sound notifications
if platform.system() == "Windows":
    import winsound
else:
    import os

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
            play_sound()
            alarms.remove(alarm_time)  # Remove the alarm after it rings
            update_alarm_list()
    root.after(1000, check_alarms)  # Check alarms every second

def play_sound():
    """
    Plays a notification sound.
    """
    if platform.system() == "Windows":
        winsound.Beep(440, 1000)  # Beep for 1 second
    else:
        os.system('say "Alarm ringing!"')

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

def delete_alarm():
    """
    Deletes a selected alarm from the list.
    """
    selected_alarm = alarm_listbox.get(ACTIVE)
    if selected_alarm in alarms:
        alarms.remove(selected_alarm)
        update_alarm_list()
    else:
        messagebox.showwarning("No Alarm Selected", "Please select an alarm to delete.")

def update_alarm_list():
    """
    Updates the displayed list of active alarms.
    """
    alarm_listbox.delete(0, END)
    for alarm in alarms:
        alarm_listbox.insert(END, alarm)

# Create the main window
root = Tk()
root.title("Clock with Alarm")
root.geometry("400x400")
root.resizable(False, False)

# Create frames for better layout management
clock_frame = Frame(root)
clock_frame.pack(pady=10)

alarm_frame = Frame(root)
alarm_frame.pack(pady=10)

list_frame = Frame(root)
list_frame.pack(pady=10)

# Create labels for time and date
time_label = Label(clock_frame, font=("Arial", 48), fg="blue")
date_label = Label(clock_frame, font=("Arial", 20))

# Create alarm entry field and buttons
alarm_label = Label(alarm_frame, text="Set Alarm (HH:MM):")
alarm_entry = Entry(alarm_frame)
set_alarm_button = Button(alarm_frame, text="Set Alarm", command=set_alarm)
delete_alarm_button = Button(alarm_frame, text="Delete Selected Alarm", command=delete_alarm)

# Create alarm list display
alarm_listbox = Listbox(list_frame, font=("Arial", 14), height=8, width=25, selectmode=SINGLE)
alarm_scrollbar = Scrollbar(list_frame, orient=VERTICAL, command=alarm_listbox.yview)
alarm_listbox.config(yscrollcommand=alarm_scrollbar.set)

# Arrange widgets
# Clock frame
time_label.pack()
date_label.pack()

# Alarm frame
alarm_label.grid(row=0, column=0, padx=5, pady=5)
alarm_entry.grid(row=0, column=1, padx=5, pady=5)
set_alarm_button.grid(row=1, column=0, columnspan=2, pady=5)
delete_alarm_button.grid(row=2, column=0, columnspan=2, pady=5)

# List frame
alarm_listbox.grid(row=0, column=0)
alarm_scrollbar.grid(row=0, column=1, sticky="ns")

# Initialize alarm list
alarms = []

# Start updating the clock and checking alarms
update_clock()
check_alarms()

# Start the GUI event loop
root.mainloop()
