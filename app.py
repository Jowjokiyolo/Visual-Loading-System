# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
from tkinter import *

from PIL import Image, ImageTk

window = Tk()
window.title("Visual Loading System")
window.geometry("720x500")
icon_window = PhotoImage(r"Center_of_Gravity_symbol.png")
window.iconphoto(True, icon_window)

label2 = Label(window, text="Zone 1\n(Max 35)")
label2.place(x=30, y=50, width=70, height=40)

entry1 = Entry(window)
entry1.place(x=30, y=90, width=70, height=30)

label3 = Label(window, text="Zone 2\n(Max 80)")
label3.place(x=205, y=50, width=70, height=40)

entry2 = Entry(window)
entry2.place(x=205, y=90, width=70, height=30)

label4 = Label(window, text="Zone 3\n(Max 140)")
label4.place(x=425, y=50, width=70, height=40)

entry3 = Entry(window)
entry3.place(x=425, y=90, width=70, height=30)

label5 = Label(window, text="Zone 4\n(Max 126)")
label5.place(x=600, y=50, width=70, height=40)

entry4 = Entry(window)
entry4.place(x=600, y=90, width=70, height=30)

# Kept on  or Python garbage-collects it and the image goes blank.
image1_image = ImageTk.PhotoImage(Image.open("image.png").resize((640, 120)))
image1 = Label(window, image=image1_image)
image1.place(x=30, y=150, width=640, height=120)

label6 = Label(window, text="Fuel\n(Max 154229 KG)")
label6.place(x=300, y=280, width=110, height=40)

entry5 = Entry(window)
entry5.place(x=300, y=320, width=110, height=30)

label7 = Label(window, text="Cargo Fwd\n(Max 19799 KG)")
label7.place(x=100, y=280, width=100, height=40)

entry6 = Entry(window)
entry6.place(x=100, y=320, width=100, height=30)

entry7 = Entry(window)
entry7.place(x=495, y=320, width=100, height=30)

label8 = Label(window, text="Cargo Aft\n(Max 16624 KG)")
label8.place(x=495, y=280, width=100, height=40)

button1 = Button(window, text="Plot", command=print)
button1.place(x=574, y=440, width=96, height=32)

window.mainloop()
