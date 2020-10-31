import tkinter


class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.label1 = tkinter.Label(self.top_frame, text = "test text label1 top_frame")
        self.label2 = tkinter.Label(self.top_frame, text = "test text label2 top_frame")
        self.label3 = tkinter.Label(self.top_frame, text="test text label2 top_frame")

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text="test text label4 bottom_frame")
        self.label5 = tkinter.Label(self.bottom_frame, text="test text label5 bottom_frame")
        self.label6 = tkinter.Label(self.bottom_frame, text="test text label6 bottom_frame")

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()