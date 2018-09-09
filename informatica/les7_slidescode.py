import tkinter

# Basis GUI
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()
        tkinter.mainloop()
"""

# Text en label
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()
        self.label2 = tkinter.Label(self.main_window, text='Hallo Bi1!')
        self.label2.pack()
        tkinter.mainloop()

"""

# Parameteriseren
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Hello World!',\
                                    bg="red",relief="sunken")
        self.label1.pack(side="top")
        self.label2 = tkinter.Label(self.bottom_frame, text='Hallo Bi1!',\
                                    relief="raised",bg="yellow",\
                                    fg="blue")
        self.label2.pack(side="top")
        self.top_frame.pack()
        self.bottom_frame.pack()        
        tkinter.mainloop()

"""

# Frames
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Hello World!')
        self.label1.pack(side="top")
        self.label2 = tkinter.Label(self.bottom_frame, text='Hallo Bi1!')
        self.label2.pack(side="top")
        self.top_frame.pack()
        self.bottom_frame.pack()        
        tkinter.mainloop()

"""

# Buttons en Dialogen
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()
        self.my_button = tkinter.Button(self.main_window, text='klik!',\
                                        command=self.doe_iets)
        self.my_button.pack()
        tkinter.mainloop()
    def doe_iets(self):
        tkinter.messagebox.showinfo('response','Bedankt voor het klikken!')

"""

# Entry Widget
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',\
                                        command=self.doe_iets)
        self.my_button.pack()
        self.invoer = tkinter.Entry (self.main_window,width=10)
        self.invoer.pack()
        self.frame.pack()        
        tkinter.mainloop()

    def doe_iets(self):
        tekst = self.invoer.get()
        tkinter.messagebox.showinfo('response','Invoer is '+tekst)

"""

# Labels als output
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',\
                                        command=self.doe_iets)
        self.my_button.pack()
        self.invoer = tkinter.Entry (self.main_window,width=10)
        self.invoer.pack()
        
        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.main_window, \
                                         textvariable=self.value)
        self.value_label.pack()
        self.frame.pack()        
        tkinter.mainloop()

    def doe_iets(self):
        tekst = self.invoer.get()
        self.value.set(tekst)
"""

# Radiobuttons
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',\
                                        command=self.doe_iets)
        self.my_button.pack()
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.frame, \
                        text='Keuze 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.frame, \
                        text='Keuze 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.frame, \
                        text='Keuze 3', variable=self.radio_var, value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.frame.pack()        
        tkinter.mainloop()

    def doe_iets(self):
        tekst = str(self.radio_var.get())
        tkinter.messagebox.showinfo('response','Invoer is '+tekst)
"""


# Checkboxes
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',\
                                        command=self.doe_iets)
        self.my_button.pack()
        
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        self.cb1 = tkinter.Checkbutton(self.frame, \
                        text='Keuze 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame, \
                        text='Keuze 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame, \
                        text='Keuze 3', variable=self.cb_var3)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.frame.pack()        
        tkinter.mainloop()

    def doe_iets(self):
        self.message = "Keuzes:\n"
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'
        tkinter.messagebox.showinfo('response',self.message)
"""

my_gui = MyGUI()
