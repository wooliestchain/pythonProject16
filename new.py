from tkinter import *


class NavSidebar(Frame):
    def __init__(self, master=None):
        super().__init__(master=master, bg="#202020", width=200)

        # logo
        self.logo = Label(self, text="MyApp", font=("Helvetica", 20), bg="#202020", fg="white", pady=20)
        self.logo.pack()

        # menu
        self.menu_items = ["Dashboard", "Settings", "Help"]
        self.menu_buttons = []
        for item in self.menu_items:
            button = Button(self, text=item, font=("Helvetica", 14), bg="#202020", fg="white", bd=0,
                            activebackground="#303030", padx=20, pady=10)
            button.pack(fill=X, padx=10, pady=5)
            self.menu_buttons.append(button)

        # spacer
        spacer = Frame(self, bg="#202020", height=50)
        spacer.pack()

        # logout button
        self.logout_button = Button(self, text="Logout", font=("Helvetica", 14), bg="#202020", fg="white", bd=0,
                                    activebackground="#303030", padx=20, pady=10)
        self.logout_button.pack(side=BOTTOM, fill=X, padx=10, pady=10)


class MyApp(Frame):
    def __init__(self, master=None):
        super().__init__(master=master, bg="#303030")

        # navbar
        self.navbar = NavSidebar(self)
        self.navbar.pack(side=LEFT, fill=Y)

        # content
        self.content = Frame(self, bg="#303030")
        self.content.pack(expand=True, fill=BOTH)


        # add some sample content
        label = Label(self.content, text="This is some content", font=("Helvetica", 24), fg="white", pady=50)
        label.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("MyApp")
    root.geometry("900x700")
    app = MyApp(root)
    app.pack(expand=True, fill=BOTH)
    root.mainloop()
