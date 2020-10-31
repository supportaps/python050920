import tkinter


class Translator:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.value = tkinter.StringVar()
        self.show_result_label = tkinter.Label(self.top_frame,
                                               textvariable=self.value)
        self.show_result_label.pack(side='left')

        self.sinister_button = tkinter.Button(self.bottom_frame,
                                              text='sinister', command=self.show_translated_message_left)
        self.dexter_button = tkinter.Button(self.bottom_frame,
                                            text='dexter', command=self.show_translated_message_right)
        self.medium_button = tkinter.Button(self.bottom_frame,
                                            text='medium', command=self.show_translated_message_middle)

        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()



        tkinter.mainloop()



    def show_translated_message_left(self):
        self.value.set('Left')
    def show_translated_message_right(self):
        self.value.set('Right')
    def show_translated_message_middle(self):
        self.value.set('Middle')