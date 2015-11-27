#!/usr/bin/python

#
# CS50 Project: ROT Cipher (Python Tkinter GUI)
#
# Author: Paulo Mota (2015)
#

import tkinter


class rotGui(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # LABELS
        self.entry1 = tkinter.Label(self, text="Message to change: ")
        self.entry1.grid(column=0, row=0, sticky='E')

        self.entry2 = tkinter.Label(self, text="Key (-26 to 26): ")
        self.entry2.grid(column=0, row=1, sticky='E')

        self.entry3 = tkinter.Label(self, text="Resulting text: ")
        self.entry3.grid(column=0, row=2, sticky='E')

        # DEFINING THE KEY VARIABLE BOX
        self.keyVariable = tkinter.StringVar()  # define entry variable
        self.entry = tkinter.Entry(self, textvariable=self.keyVariable,
                                   fg="gray")
        self.entry.grid(column=1, row=1, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)  # Bind ENTER event
        self.keyVariable.set(u"0")  # Initial text

        # DEFINING THE INPUT BOX
        self.inputBox = tkinter.StringVar()  # define entry variable
        self.entry = tkinter.Entry(self, textvariable=self.inputBox,
                                   fg="gray")
        self.entry.grid(column=1, row=0, columnspan=3, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)  # Bind ENTER event
        self.inputBox.set(u"Text to encrypt")  # Initial text

        # CONTROL BUTTONS
        # Encrypt Button
        button = tkinter.Button(self, text=u"Encrypt",
                                command=self.OnButtonClick)
        button.grid(column=2, row=1)

        # Quit Button
        button = tkinter.Button(self, text=u"Quit",
                                command=self.destroy)
        button.grid(column=3, row=1)

        # DEFINING THE RESULT BOX
        self.resultBox = tkinter.StringVar()  # define label variable
        label = tkinter.Label(self, textvariable=self.resultBox,
                              anchor="w", fg="black", bg="lightgray")
        label.grid(column=1, row=2, columnspan=3, sticky='EW')
        self.resultBox.set(u"Awaiting input...")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def encryptInput(self, message):
        rotated = ''

        # Converting a non-iterable StringVar() into a iterable list
        message = list(self.inputBox.get())

        # Converting StringVar() into an integer
        key = int(self.keyVariable.get())

        for char in message:
            if char.isalpha():
                val = ord(char)
                val += key  # allows negative values, decryption

                if char.isupper():
                    if val > ord('Z'):
                        val -= 26
                    elif val < ord('A'):
                        val += 26
                elif char.islower():
                    if val > ord('z'):
                        val -= 26
                    elif val < ord('a'):
                        val += 26

                rotated += chr(val)
            else:
                rotated += char
        return rotated

    def OnButtonClick(self):
        rotmessage = self.encryptInput('')
        self.resultBox.set(rotmessage)
        self.entry.focus_set()

    def OnPressEnter(self, event):
        rotmessage = self.encryptInput('')
        self.resultBox.set(rotmessage)
        self.entry.focus_set()


if __name__ == "__main__":
    app = rotGui(None)
    app.title('CS50: ROT Cipher (Python GUI)')
    app.mainloop()
