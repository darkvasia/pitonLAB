import tkinter as tk
from threading import Thread
import socket

class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("Чат-клієнт")

        self.chat_area = tk.Text(master, state='disabled')
        self.chat_area.pack(padx=10, pady=10, expand=True, fill='both')

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(padx=10, pady=10, fill='x')

        self.send_button = tk.Button(master, text="Надіслати", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        self.receive_thread = Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        self.client_socket.send(message.encode())
        self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.config(state='disabled')
                self.chat_area.see(tk.END)
            except OSError:
                break

if __name__ == "__main__":
    root = tk.Tk()
    chat_client = ChatClient(root)
    root.mainloop()
