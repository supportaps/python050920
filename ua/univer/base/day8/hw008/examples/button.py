import tkinter
import tkinter.messagebox


class Button():
    def __init__(self):

            self.main_window = tkinter.Tk()

            self.my_button = tkinter.Button(self.main_window, text="Press me!", command=self.do_something)
            self.quit_button = tkinter.Button(self.main_window, text="Exit", command=self.main_window.destroy)

            self.my_button.pack()
            self.quit_button.pack()

            tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Message Info','Thanks for a press of the button')
