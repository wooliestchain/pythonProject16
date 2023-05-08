import tkinter as tk
from suds.client import Client


class MyLayout(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Hello World Client")

        # Création des widgets
        self.name_label = tk.Label(self, text="Nom :")
        self.name_label.pack()

        self.name_input = tk.Entry(self)
        self.name_input.pack()

        self.submit_button = tk.Button(self, text="Soumettre", command=self.on_submit)
        self.submit_button.pack()

        self.message_output = tk.Label(self, text="")
        self.message_output.pack()

        self.client = Client('http://localhost:8000/?wsdl')

    def on_submit(self):
        name = self.name_input.get()
        response = self.client.service.say_hello(name)
        self.message_output.config(text=response)


def main():
    root = tk.Tk()
    app = MyLayout(master=root)
    app.pack()
    app.mainloop()


if __name__ == '__main__':
    main()