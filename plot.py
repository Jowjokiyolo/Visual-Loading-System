import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def mkplot(
    mac_tow: float,
    tow: float,
    mac_law: float,
    law: float,
    mac_zfw: float,
    zfw: float,
):
    # Main Bounds
    x_mac = (
        26.9,
        34.1,
        44.0,
        44.0,
        44.0,
        38.1,
        27.4,
        22.0,
        17.8,
        15.4,
        11.5,
        10.5,
        7.5,
        7.5,
    )
    y_gw = (
        130000,
        158031,
        224029,
        279911,
        304814,
        343414,
        351534,
        351534,
        345455,
        325996,
        251290,
        237682,
        204116,
        130000,
    )

    # Main Plot
    plt.figure(figsize=(720, 720, "px"))
    plt.title("C.G. Limits Boeing 777-300ER")
    plt.xlabel("Center of Gravity - %MAC")
    plt.ylabel("Gross Weight - KG")
    plt.plot(x_mac, y_gw, color="black")

    # No Take-Off Area
    x_no_to = (34.1, 44.0)
    y_no_to = (158031, 279911)
    plt.fill_between(
        x_no_to, y_no_to, (158031, 224029), color="black", alpha=1 / 3
    )
    plt.annotate(
        "Do not operate\nin shaded area\nduring takeoff",
        xy=(41, 220000),
        xytext=(41, 150000),
        ha="center",
        fontsize=8,
        arrowprops={"arrowstyle": "-", "color": "black", "linewidth": 0.8},
    )

    # Max Zero Fuel Weight Line
    x_mzfw = (10.5, 44.0)
    y_mzfw = (237682, 237682)
    plt.plot(x_mzfw, y_mzfw, c="black", ls="--", alpha=1 / 2)
    plt.text(11.5, 237700, "MZFW", ha="left", va="bottom")
    plt.text(11.5, 236500, "237682 KG", ha="left", va="top")

    # Max Landing Weight
    x_mlw = (11.5, 44.0)
    y_mlw = (251290, 251290)
    plt.plot(x_mlw, y_mlw, c="black", ls="--", alpha=1 / 2)
    plt.text(15, 251500, "MLW", ha="left", va="bottom")
    plt.text(15, 250500, "251290 KG", ha="left", va="top")

    # TOW Point
    icon = img.imread(r"img/Center_of_Gravity_symbol.png")
    icon_box = AnnotationBbox(
        OffsetImage(icon, zoom=0.05),
        (mac_tow, tow),
        frameon=False,
    )
    plt.gca().add_artist(icon_box)
    plt.annotate(
        "TOW",
        xy=(mac_tow, tow),
        xytext=(5, 5),
        textcoords="offset points",
        ha="left",
        va="bottom",
    )

    # LAW Point
    law_icon_box = AnnotationBbox(
        OffsetImage(icon, zoom=0.05),
        (mac_law, law),
        frameon=False,
    )
    plt.gca().add_artist(law_icon_box)
    plt.annotate(
        "LAW",
        xy=(mac_law, law),
        xytext=(5, 5),
        textcoords="offset points",
        ha="left",
        va="bottom",
    )

    # ZFW Point
    zfw_icon_box = AnnotationBbox(
        OffsetImage(icon, zoom=0.05),
        (mac_zfw, zfw),
        frameon=False,
    )
    plt.gca().add_artist(zfw_icon_box)
    plt.annotate(
        "ZFW",
        xy=(mac_zfw, zfw),
        xytext=(5, 5),
        textcoords="offset points",
        ha="left",
        va="bottom",
    )

    plt.show(block=False)
