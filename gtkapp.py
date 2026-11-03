import gi

import plot

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk

from plane import Plane


class CambalacheApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.example.cambalache_demo")

    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("vls.ui")

        self.window = builder.get_object("mainWindow")
        self.window.set_application(self)

        def do_plot(self):
            ez1 = int(builder.get_object("ez1").get_text())
            ez2 = int(builder.get_object("ez2").get_text())
            ez3 = int(builder.get_object("ez3").get_text())
            ez4 = int(builder.get_object("ez4").get_text())
            ecf = float(builder.get_object("ecf").get_text())
            eca = float(builder.get_object("eca").get_text())
            ebf = float(builder.get_object("ebf").get_text())
            etf = float(builder.get_object("etf").get_text())

            Plane.business.load(ez1)
            Plane.econPrem.load(ez2)
            Plane.econWing.load(ez3)
            Plane.econRear.load(ez4)
            Plane.fuelTank.load(ebf)
            Plane.fwdCarg.load(ecf)
            Plane.aftCarg.load(eca)

            Plane.calBalance(Plane.COMPARTMENTS, "tow")
            Plane.calLaw(Plane.COMPARTMENTS, ebf, etf)
            Plane.calZfw(Plane.COMPARTMENTS)
            plot.mkplot(
                Plane.mac_tow,
                Plane.tow,
                Plane.mac_law,
                Plane.law,
                Plane.mac_zfw,
                Plane.zfw,
            )

        bplot = builder.get_object("bplot")
        bplot.connect("clicked", do_plot)
        self.window.present()


if __name__ == "__main__":
    app = CambalacheApp()
    app.run(None)
