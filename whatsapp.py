import tkinter as tk
import pywhatkit as py
from tkinter import messagebox

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = phone_entry.get()
    message = message_text.get("1.0", tk.END)
    try:
        py.sendwhatmsg(phone_number, message, int(hour_entry.get()), int(minute_entry.get()))
        messagebox.showinfo("Success", "Message sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("WhatsApp Message Sender")

# Create labels
phone_label = tk.Label(app, text="Phone Number:")
phone_label.pack()
hour_label = tk.Label(app, text="Hour:")
hour_label.pack()
minute_label = tk.Label(app, text="Minute:")
minute_label.pack()
message_label = tk.Label(app, text="Message:")
message_label.pack()

# Create entry fields
phone_entry = tk.Entry(app)
phone_entry.pack()
hour_entry = tk.Entry(app)
hour_entry.pack()
minute_entry = tk.Entry(app)
minute_entry.pack()
message_text = tk.Text(app, height=5, width=30)
message_text.pack()

# Create a button to send the message
send_button = tk.Button(app, text="Send Message", command=send_whatsapp_message)
send_button.pack()

# Start the GUI main loop
app.mainloop()
