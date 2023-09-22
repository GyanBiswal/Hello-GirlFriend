import tkinter as tk
from tkinter import ttk
import pywhatkit as kit
import datetime

from tkinter import PhotoImage

from apscheduler.schedulers.blocking import BlockingScheduler


def send_whatsapp_message():
    phone_number = phone_number_entry.get()
    message = message_entry.get()
    hour = int(hour_combobox.get())
    minute = int(minute_combobox.get())

    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        result_label.config(text="Message scheduled successfully!", foreground="green")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", foreground="red")
        print("Error:", e)


app = tk.Tk()

app.title("Hello-GirlFriend")
# Set the dimensions of the GUI window
app.geometry("400x300")  # Width x Height

# Create and place UI elements
phone_label = ttk.Label(app, text="Darling's Phone Number:")
phone_label.pack()
phone_number_entry = ttk.Entry(app)
phone_number_entry.pack()

message_label = ttk.Label(app, text="Message Content:")
message_label.pack()
message_entry = ttk.Entry(app)
message_entry.pack()

time_label = ttk.Label(app, text="Scheduling Time:")
time_label.pack()

hour_combobox = ttk.Combobox(app, values=[str(i) for i in range(24)])
hour_combobox.pack()
hour_combobox.set("10")  # Default hour

minute_combobox = ttk.Combobox(app, values=[str(i) for i in range(60)])

minute_combobox.pack()
minute_combobox.set("30")  # Default minute

schedule_button = ttk.Button(app, text="Schedule Message", command=send_whatsapp_message)
schedule_button.pack()

result_label = ttk.Label(app, text="", font=("Helvetica", 12))
result_label.pack()

app.mainloop()
