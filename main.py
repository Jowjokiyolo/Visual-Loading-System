# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
from tkinter import *

from PIL import Image, ImageTk

from plane import *
from plot import mkplot


def main():
    window = Tk()
    window.title("Visual Loading System")
    window.geometry("720x500")
    icon_window = PhotoImage(r"Center_of_Gravity_symbol.png")
    window.iconphoto(True, icon_window)

    lb_zone1 = Label(window, text="Zone 1\n(Max 35)")
    lb_zone1.place(x=30, y=50, width=70, height=40)
    entry_zone1 = Entry(window)
    entry_zone1.place(x=30, y=90, width=70, height=30)

    lb_zone2 = Label(window, text="Zone 2\n(Max 80)")
    lb_zone2.place(x=205, y=50, width=70, height=40)
    entry_zone2 = Entry(window)
    entry_zone2.place(x=205, y=90, width=70, height=30)

    lb_zone3 = Label(window, text="Zone 3\n(Max 140)")
    lb_zone3.place(x=425, y=50, width=70, height=40)
    entry_zone3 = Entry(window)
    entry_zone3.place(x=425, y=90, width=70, height=30)

    lb_zone4 = Label(window, text="Zone 4\n(Max 126)")
    lb_zone4.place(x=600, y=50, width=70, height=40)
    entry_zone4 = Entry(window)
    entry_zone4.place(x=600, y=90, width=70, height=30)

    image1_image = ImageTk.PhotoImage(Image.open(r"img/plane.png").resize((640, 120)))
    image1 = Label(window, image=image1_image)
    image1.place(x=30, y=150, width=640, height=120)

    lb_fuel = Label(window, text="Fuel\n(Max 154229 KG)")
    lb_fuel.place(x=300, y=280, width=110, height=40)
    entry_fuel = Entry(window)
    entry_fuel.place(x=300, y=320, width=110, height=30)

    lbl_cargo_fwd = Label(window, text="Cargo Fwd\n(Max 19799 KG)")
    lbl_cargo_fwd.place(x=100, y=280, width=100, height=40)
    entry_cargo_fwd = Entry(window)
    entry_cargo_fwd.place(x=100, y=320, width=100, height=30)

    lb_cargo_aft = Label(window, text="Cargo Aft\n(Max 16624 KG)")
    lb_cargo_aft.place(x=495, y=280, width=100, height=40)
    entry_cargo_aft = Entry(window)
    entry_cargo_aft.place(x=495, y=320, width=100, height=30)


    def openplot():
        z1 = float(entry_zone1.get())
        z2 = float(entry_zone2.get())
        z3 = float(entry_zone3.get())
        z4 = float(entry_zone4.get())
        fu = float(entry_fuel.get())
        cf = float(entry_cargo_fwd.get())
        ca = float(entry_cargo_aft.get())

        Plane.business.load(z1)
        Plane.econPrem.load(z2)
        Plane.econWing.load(z3)
        Plane.econRear.load(z4)
        Plane.fuelTank.load(fu)
        Plane.fwdCarg.load(cf)
        Plane.aftCarg.load(ca)

        Plane.calBalance(Plane.COMPARTMENTS)
        mkplot(Plane.mac, Plane.weight)


    plotbutton = Button(window, text="Plot", command=openplot)
    plotbutton.place(x=574, y=440, width=96, height=32)

    window.mainloop()

if __name__ == "__main__":
    main()