# imports
import tkinter as tk
tk.Tk.debug = 1
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
import os
import json
import subprocess
import random

# -----------------------------------------------------------------------------------------------------------------------------------------
# icons
icon_pfad = "images/ico.ico"
# -----------------------------------------------------------------------------------------------------------------------------------------

app_noten = None
app_home = None
app_stdp = None
app_aufg = None
app_kld = None
app_est = None
button_credits = None
button_datenschutz = None
button_kontakt = None

# -----------------------------------------------------------------------------------------------------------------------------------------
# create the mainwindow
def Home():
    # app
    global app_home
    global app_noten
    global app_stdp
    global app_aufg
    global app_kld
    global app_est
    # andere Fenster schließen
    if app_noten:
        app_noten.destroy()
        app_noten = None
    if app_stdp:
        app_stdp.destroy()
        app_stdp = None
    if app_aufg:
        app_aufg.destroy()
        app_aufg = None
    if app_kld:
        app_kld.destroy()
        app_kld = None
    if app_est:
        app_est.destroy()
        app_est = None
    
    # app
    app_home = tk.Tk()
    app_home.title("Noten-App -- Home")
    app_home.geometry("600x700")
    app_home.resizable(False, False)
    app_home.geometry("+100+100")
    app_home.iconbitmap(icon_pfad)


    # Funktionen für die Aktionen der Buttons
    label_überschrift = tk.Label(app_home, text="Home", font=("Times New Roman", 40, "bold", "underline"))
    label_überschrift.pack()

    label_wilkommensnachricht = tk.Label(app_home, text="Willkommen in der Noten-App!", font=("Times New Roman", 20, "bold"))
    label_wilkommensnachricht.pack()

    # strich
    strich_home=PhotoImage(file='images/strich.png')
    strich_home_label=Label(app_home, image=strich_home)
    strich_home_label.image=strich_home
    strich_home_label.place(x=0, y=100, relwidth=1)

    # Version
    ## create a rechteck
    canvas_version = tk.Canvas(app_home, width=200, height=200)
    canvas_version.pack()
    canvas_version.place(x=10, y=120)
    rectangle = canvas_version.create_rectangle(50, 50, 200, 200)

    ## create a label
    label_version = tk.Label(app_home, text="Version: ", font=("Times New Roman", 20, "bold", "underline"), fg="orange")
    label_version_nr = tk.Label(app_home, text="1.0", font=("Times New Roman", 20, "bold"))
    label_version_nr.pack()
    label_version.pack()
    label_version.place(x=80, y=180)
    label_version_nr.place(x=80, y=250)

    # Neuerungen Update
    ## create a label
    label_news = tk.Label(app_home, text="Neuerungen:", font=("Times New Roman", 20, "bold", "underline"), fg="blue")
    label_news.pack()
    label_news.place(x=300, y=150)

    ## create a listbox
    listbox_news = tk.Listbox(app_home, font=("Times New Roman", 15, "bold"), width=20, height=15)
    listbox_news.pack()
    listbox_news.place(x=280, y=200)

    ################################################# NEWS HIER EINTRAGEN! #################################################
    listbox_news.insert(0, "- Notenrechner")
    listbox_news.insert(1, "- Stundenplan")
    listbox_news.insert(2, "- Notizen")
    listbox_news.insert(3, "- Kalender")
    listbox_news.insert(4, "- Einstellungen")

    # controllbar
    global noten_image
    noten_image = Image.open("images/nt.png")
    noten_image = noten_image.resize((25, 25), resample=Image.LANCZOS)
    noten_image = ImageTk.PhotoImage(noten_image)
    button_noten = tk.Button(app_home, image=noten_image, text="Noten", font=("Arial", 15), bg="white", command=Noten)
    button_noten.pack()
    button_noten.place(x=150, y=650)

    global stundenplan_image
    stundenplan_image = Image.open("images/stdp.png")
    stundenplan_image = stundenplan_image.resize((25, 25), resample=Image.LANCZOS)
    stundenplan_image = ImageTk.PhotoImage(stundenplan_image)
    button_stundenplan = tk.Button(app_home, image=stundenplan_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Stundenplan)
    button_stundenplan.pack()
    button_stundenplan.place(x=250, y=650)

    global aufgaben_image
    aufgaben_image = Image.open("images/afg.png")
    aufgaben_image = aufgaben_image.resize((25, 25), resample=Image.LANCZOS)
    aufgaben_image = ImageTk.PhotoImage(aufgaben_image)
    button_aufgaben = tk.Button(app_home, image=aufgaben_image, text="Aufgaben", font=("Arial", 15), bg="white", command=Aufgaben)
    button_aufgaben.pack()
    button_aufgaben.place(x=350, y=650)

    global kalender_image
    kalender_image = Image.open("images/kld.png")
    kalender_image = kalender_image.resize((25, 25), resample=Image.LANCZOS)
    kalender_image = ImageTk.PhotoImage(kalender_image)
    button_kalender = tk.Button(app_home, image=kalender_image, text="Kalender", font=("Arial", 15), bg="white", command=Kalender)
    button_kalender.pack()
    button_kalender.place(x=450, y=650)

    global einstellungen_image
    einstellungen_image = Image.open("images/est.png")
    einstellungen_image = einstellungen_image.resize((25, 25), resample=Image.LANCZOS)
    einstellungen_image = ImageTk.PhotoImage(einstellungen_image)
    button_einstellungen = tk.Button(app_home, image=einstellungen_image, text="Einstellungen", font=("Arial", 15), bg="white", command=Einstellungen)
    button_einstellungen.pack()
    button_einstellungen.place(x=550, y=650)

    
    app_home.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
# create the notenwindow
def Noten():
    from PIL import ImageTk, Image
    # app
    global app_noten
    global app_home
    global app_stdp
    global app_aufg
    global app_kld
    global app_est
    # andere Fenster schließen
    if app_home:
        app_home.destroy()
        app_home = None
    if app_stdp:
        app_stdp.destroy()
        app_stdp = None
    if app_aufg:
        app_aufg.destroy()
        app_aufg = None
    if app_kld:
        app_kld.destroy()
        app_kld = None
    if app_est:
        app_est.destroy()
        app_est = None
    

    # app
    app_noten = tk.Tk()
    app_noten.title("Noten-App -- Noten")
    app_noten.geometry("600x700")
    app_noten.resizable(False, False)
    app_noten.geometry("+100+100")
    app_noten.iconbitmap(icon_pfad)


    label_noten_überschrift = tk.Label(app_noten, text="Noten", font=("Times New Roman", 40, "bold", "underline"))
    label_noten_überschrift.pack()

    label_noten_einleitung = tk.Label(app_noten, text="Hier kannst du Noten/Fächer eintragen, Speichern, und berechnen lassen.", font=("Times New Roman", 13, "bold"))
    label_noten_einleitung.pack()

    # strich
    strich_noten=PhotoImage(file='images/strich.png')
    strich_noten_label=Label(app_noten, image=strich_noten)
    strich_noten_label.image=strich_noten
    strich_noten_label.place(x=0, y=100, relwidth=1)

    label_fach = tk.Label(text="Fach:", font=("Times New Roman", 20, "bold", "underline"))
    label_fach.pack()
    label_fach.place(x=10, y=150)

    label_note = tk.Label(text="Note:", font=("Times New Roman", 20, "bold", "underline"))
    label_note.pack()
    label_note.place(x=10, y=200)

    global average_label
    average_label = tk.Label(app_noten, text="", font=("Times New Roman", 20, "bold"))
    average_label.pack()
    average_label.place(x=10, y=500)

    button_add = tk.Button(text="Note hinzufügen", font=("Times New Roman", 15, "bold"), bg="green", fg="white", command=add_note)
    button_add.pack()
    button_add.place(x=100, y=250)
    
    global noten_entry
    noten_entry = tk.Entry(font=("Times New Roman", 15, "bold"))
    noten_entry.pack()
    noten_entry.place(x=100, y=205)

    global fach_entry
    fach_entry = tk.Entry(font=("Times New Roman", 15, "bold"))
    fach_entry.pack()
    fach_entry.place(x=100, y=155)

    global noten_listbox
    noten_listbox = tk.Listbox(font=("Times New Roman", 15, "bold"), width=23, height=14)
    noten_listbox.pack()
    noten_listbox.place(x=320, y=150)

    visible_rows = min(len(noten_listbox.get(0, "end")), 15)
    scrollbar = tk.Scrollbar(app_noten, orient=tk.VERTICAL, command=noten_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.pack_forget()  # Entfernt die Scrollbar

    noten_listbox.config(yscrollcommand=scrollbar.set)

    noten_listbox.bind("<ButtonRelease-1>", on_item_selected)  # Linksklick
    noten_listbox.bind("<ButtonRelease-3>", on_item_right_click)  # Rechtsklick

    # controllbar
    home_noten_image = Image.open("images/hb.png")
    home_noten_image = home_noten_image.resize((25, 25), resample=Image.LANCZOS)
    home_noten_image = ImageTk.PhotoImage(home_noten_image)
    button_noten_home = tk.Button(app_noten, image=home_noten_image, text="Home", font=("Arial", 15), bg="white", command=Home)
    button_noten_home.pack()
    button_noten_home.place(x=50, y=650)

    stundenplan_noten_image = Image.open("images/stdp.png")
    stundenplan_noten_image = stundenplan_noten_image.resize((25, 25), resample=Image.LANCZOS)
    stundenplan_noten_image = ImageTk.PhotoImage(stundenplan_noten_image)
    button_noten_stundenplan = tk.Button(app_noten, image=stundenplan_noten_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Stundenplan)
    button_noten_stundenplan.pack()
    button_noten_stundenplan.place(x=250, y=650)

    aufgaben_noten_image = Image.open("images/afg.png")
    aufgaben_noten_image = aufgaben_noten_image.resize((25, 25), resample=Image.LANCZOS)
    aufgaben_noten_image = ImageTk.PhotoImage(aufgaben_noten_image)
    button_noten_aufgaben = tk.Button(app_noten, image=aufgaben_noten_image, text="Aufgaben", font=("Arial", 15), bg="white", command=Aufgaben)
    button_noten_aufgaben.pack()
    button_noten_aufgaben.place(x=350, y=650)

    kalender_noten_image = Image.open("images/kld.png")
    kalender_noten_image = kalender_noten_image.resize((25, 25), resample=Image.LANCZOS)
    kalender_noten_image = ImageTk.PhotoImage(kalender_noten_image)
    button_noten_kalender = tk.Button(app_noten, image=kalender_noten_image, text="Kalender", font=("Arial", 15), bg="white", command=Kalender)
    button_noten_kalender.pack()
    button_noten_kalender.place(x=450, y=650)

    einstellungen_noten_image = Image.open("images/est.png")
    einstellungen_noten_image = einstellungen_noten_image.resize((25, 25), resample=Image.LANCZOS)
    einstellungen_noten_image = ImageTk.PhotoImage(einstellungen_noten_image)
    button_noten_einstellungen = tk.Button(app_noten, image=einstellungen_noten_image, text="Einstellungen", font=("Arial", 15), bg="white", command=Einstellungen)
    button_noten_einstellungen.pack()
    button_noten_einstellungen.place(x=550, y=650)

    show_notes()
    app_noten.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
# create the stundenplanwindow
import tkinter as tk
from tkinter import simpledialog
from PIL import ImageTk, Image

global times
global days_of_week
global stundenplan

def save_stundenplan(stundenplan):
    with open("stdp.json", "w") as json_file:
        json.dump(stundenplan, json_file, indent=4)

def load_stundenplan():
    try:
        with open("stdp.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

def change_times():
    # Diese Funktion ermöglicht das Ändern der Uhrzeiten
    new_times = []  # Hier können Sie die neuen Uhrzeiten eintragen
    for i in range(7):
        new_time = simpledialog.askstring("Uhrzeiten ändern", f"Geben Sie die Uhrzeit für Stunde {i+1} ein:")
        if new_time:
            new_times.append(new_time)
    
    # Heben Sie das Dialogfeld an, um es ganz oben auf dem Bildschirm anzuzeigen
    app_stdp.lift()

    return new_times

def Stundenplan():
    from PIL import ImageTk, Image

    # app
    global app_noten
    global app_home
    global app_stdp
    global app_aufg
    global app_kld
    global app_est

    # andere Fenster schließen
    if app_noten:
        app_noten.destroy()
        app_noten = None
    if app_home:
        app_home.destroy()
        app_home = None
    if app_aufg:
        app_aufg.destroy()
        app_aufg = None
    if app_kld:
        app_kld.destroy()
        app_kld = None
    if app_est:
        app_est.destroy()
        app_est = None

    # app
    app_stdp = tk.Tk()
    app_stdp.title("Noten-App -- Stundenplan")
    app_stdp.geometry("1100x700")
    app_stdp.resizable(False, False)
    app_stdp.geometry("+100+100")
    app_stdp.iconbitmap(icon_pfad)

    label_stdp_überschrift = tk.Label(app_stdp, text="Stundenplan", font=("Times New Roman", 40, "bold", "underline"))
    label_stdp_überschrift.grid(row=0, column=0, columnspan=6)

    # Wochentage und Uhrzeiten
    days_of_week = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

    # Laden Sie den Stundenplan
    stundenplan = load_stundenplan()

    if "times" in stundenplan:
        times = stundenplan["times"]
    else:
        # Hier können Sie die Uhrzeiten ändern
        times = change_times()

        if not times:
            times = ["7:30 - 8:15", "8:15 - 9:00", "9:20 - 10:05", "10:15 - 11:00", "11:10 - 11:55", "12:15 - 13:00", "13:10 - 13:55"]
            stundenplan["times"] = times

    # Erstellen Sie Labels für Wochentage
    for col, day in enumerate(days_of_week):
        label = tk.Label(app_stdp, text=day, font=("Arial", 12, "bold"))
        label.grid(row=1, column=col+1)

    # Erstellen Sie Labels für Uhrzeiten
    for row, time in enumerate(times):
        time_label = tk.Label(app_stdp, text=time, font=("Arial", 12, "bold"))
        time_label.grid(row=row+2, column=0)

    # Erstellen Sie Einträge für den Stundenplan
    for row, time in enumerate(times):
        for col, day in enumerate(days_of_week):
            entry = tk.Entry(app_stdp, font=("Arial", 12))
            entry.grid(row=row+2, column=col+1)
            key = f"{day} - Stunde {row+1}"
            entry.insert(0, stundenplan.get(key, ""))

    # Speichern Sie den Stundenplan beim Schließen des Fensters
    def on_closing():
        for row, time in enumerate(times):
            for col, day in enumerate(days_of_week):
                entry = app_stdp.grid_slaves(row=row+2, column=col+1)[0]
                key = f"{day} - Stunde {row+1}"
                stundenplan[key] = entry.get()

        # Speichern Sie die "times" separat
        stundenplan["times"] = times

        save_stundenplan(stundenplan)
        app_stdp.destroy()
        
    label_hinweis_stdp = tk.Label(app_stdp, text="Hinweis: Wenn Sie den Stundenplan oder die Uhrzeit geändert haben, müssen Sie die App direkt neu starten ohne die Kategorie zu wechseln.", font=("Arial", 12, "bold"), fg="red")
    label_hinweis_stdp.grid(row=10, column=0, columnspan=6)
    
    # controllbar
    home_stdp_image = Image.open("images/hb.png")
    home_stdp_image = home_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    home_stdp_image = ImageTk.PhotoImage(home_stdp_image)
    button_stdp_home = tk.Button(app_stdp, image=home_stdp_image, text="Home", font=("Arial", 15), bg="white", command=Home)
    button_stdp_home.grid()
    button_stdp_home.place(x=50, y=650)

    noten_stdp_image = Image.open("images/nt.png")
    noten_stdp_image = noten_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    noten_stdp_image = ImageTk.PhotoImage(noten_stdp_image)
    button_stdp_noten = tk.Button(app_stdp, image=noten_stdp_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Noten)
    button_stdp_noten.grid()
    button_stdp_noten.place(x=150, y=650)

    aufgaben_stdp_image = Image.open("images/afg.png")
    aufgaben_stdp_image = aufgaben_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    aufgaben_stdp_image = ImageTk.PhotoImage(aufgaben_stdp_image)
    button_stdp_aufgaben = tk.Button(app_stdp, image=aufgaben_stdp_image, text="Aufgaben", font=("Arial", 15), bg="white", command=Aufgaben)
    button_stdp_aufgaben.grid()
    button_stdp_aufgaben.place(x=350, y=650)

    kalender_stdp_image = Image.open("images/kld.png")
    kalender_stdp_image = kalender_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    kalender_stdp_image = ImageTk.PhotoImage(kalender_stdp_image)
    button_stdp_kalender = tk.Button(app_stdp, image=kalender_stdp_image, text="Kalender", font=("Arial", 15), bg="white", command=Kalender)
    button_stdp_kalender.grid()
    button_stdp_kalender.place(x=450, y=650)

    einstellungen_stdp_image = Image.open("images/est.png")
    einstellungen_stdp_image = einstellungen_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    einstellungen_stdp_image = ImageTk.PhotoImage(einstellungen_stdp_image)
    button_stdp_einstellungen = tk.Button(app_stdp, image=einstellungen_stdp_image, text="Einstellungen", font=("Arial", 15), bg="white", command=Einstellungen)
    button_stdp_einstellungen.grid()
    button_stdp_einstellungen.place(x=550, y=650)

    app_stdp.protocol("WM_DELETE_WINDOW", on_closing)
    app_stdp.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
# aufgabenwindow erstellen
def Aufgaben():
    from PIL import ImageTk, Image
    # app
    global app_noten
    global app_home
    global app_stdp
    global app_aufg
    global app_kld
    global app_est
    # andere Fenster schließen
    if app_home:
        app_home.destroy()
        app_home = None
    if app_stdp:
        app_stdp.destroy()
        app_stdp = None
    if app_noten:
        app_noten.destroy()
        app_noten = None
    if app_kld:
        app_kld.destroy()
        app_kld = None
    if app_est:
        app_est.destroy()
        app_est = None

    # app
    app_aufg = tk.Tk()
    app_aufg.title("Noten-App -- Notizen")
    app_aufg.geometry("600x700")
    app_aufg.resizable(False, False)
    app_aufg.geometry("+100+100")
    app_aufg.iconbitmap(icon_pfad)


    label_aufg_überschrift = tk.Label(app_aufg, text="Notizen", font=("Times New Roman", 40, "bold", "underline"))
    label_aufg_überschrift.pack()

    label_noten_einleitung = tk.Label(app_noten, text="Hier kannst du dir schnelle Notizen machen und auch Speichern.", font=("Times New Roman", 15, "bold"))
    label_noten_einleitung.pack()

    # strich
    strich_noten=PhotoImage(file='images/strich.png')
    strich_noten_label=Label(app_noten, image=strich_noten)
    strich_noten_label.image=strich_noten
    strich_noten_label.place(x=0, y=100, relwidth=1)

    # Notizfeld erstellen
    notizfeld = tk.Text(app_aufg, font=("Arial", 15), width=50, height=20)
    notizfeld.pack()
    notizfeld.place(x=22, y=130)

    # Button zum Speichern der Notiz
    def save_note():
        with open("writes.json", "w") as file:
            file.write(notizfeld.get("1.0", tk.END))

    save_button = tk.Button(app_aufg, text="Speichern", command=save_note, font=("Arial", 12, "bold"), bg="green", fg="white")
    save_button.pack()
    save_button.place(x=22, y=600)

    # auto laden
    try:
        with open("writes.json", "r") as file:
            notizfeld.insert(tk.END, file.read())
    except FileNotFoundError:
        pass

    # controllbar
    home_stdp_image = Image.open("images/hb.png")
    home_stdp_image = home_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    home_stdp_image = ImageTk.PhotoImage(home_stdp_image)
    button_stdp_home = tk.Button(app_stdp, image=home_stdp_image, text="Home", font=("Arial", 15), bg="white", command=Home)
    button_stdp_home.pack()
    button_stdp_home.place(x=50, y=650)

    noten_stdp_image = Image.open("images/nt.png")
    noten_stdp_image = noten_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    noten_stdp_image = ImageTk.PhotoImage(noten_stdp_image)
    button_stdp_noten = tk.Button(app_noten, image=noten_stdp_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Noten)
    button_stdp_noten.pack()
    button_stdp_noten.place(x=150, y=650)

    stdp_aufg_image = Image.open("images/stdp.png")
    stdp_aufg_image = stdp_aufg_image.resize((25, 25), resample=Image.LANCZOS)
    stdp_aufg_image = ImageTk.PhotoImage(stdp_aufg_image)
    button_aufg_stdp = tk.Button(app_stdp, image=stdp_aufg_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Stundenplan)
    button_aufg_stdp.pack()
    button_aufg_stdp.place(x=250, y=650)

    kalender_stdp_image = Image.open("images/kld.png")
    kalender_stdp_image = kalender_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    kalender_stdp_image = ImageTk.PhotoImage(kalender_stdp_image)
    button_stdp_kalender = tk.Button(app_stdp, image=kalender_stdp_image, text="Kalender", font=("Arial", 15), bg="white", command=Kalender)
    button_stdp_kalender.pack()
    button_stdp_kalender.place(x=450, y=650)

    einstellungen_stdp_image = Image.open("images/est.png")
    einstellungen_stdp_image = einstellungen_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    einstellungen_stdp_image = ImageTk.PhotoImage(einstellungen_stdp_image)
    button_stdp_einstellungen = tk.Button(app_stdp, image=einstellungen_stdp_image, text="Einstellungen", font=("Arial", 15), bg="white", command=Einstellungen)
    button_stdp_einstellungen.pack()
    button_stdp_einstellungen.place(x=550, y=650)

    app_aufg.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
# create the kalenderwindow
def Kalender():
    from PIL import ImageTk, Image
    # app
    global app_noten
    global app_home
    global app_stdp
    global app_aufg
    global app_kld
    global app_est
    # andere Fenster schließen
    if app_home:
        app_home.destroy()
        app_home = None
    if app_stdp:
        app_stdp.destroy()
        app_stdp = None
    if app_noten:
        app_noten.destroy()
        app_noten = None
    if app_aufg:
        app_aufg.destroy()
        app_aufg = None
    if app_est:
        app_est.destroy()
        app_est = None

    # app
    app_kld = tk.Tk()
    app_kld.title("Noten-App -- Kalender")
    app_kld.geometry("600x700")
    app_kld.resizable(False, False)
    app_kld.geometry("+100+100")
    app_kld.iconbitmap(icon_pfad)


    label_kld_überschrift = tk.Label(app_kld, text="Kalender", font=("Times New Roman", 40, "bold", "underline"))
    label_kld_überschrift.pack()

    label_kld_einleitung = tk.Label(app_kld, text="Der Kalender ist noch nicht vollendet, bitte warten Sie auf nächste Updates.", font=("Times New Roman", 13, "bold"))
    label_kld_einleitung.pack()

    # strich
    strich_kld=PhotoImage(file='images/strich.png')
    strich_kld_label=Label(app_kld, image=strich_kld)
    strich_kld_label.image=strich_kld
    strich_kld_label.place(x=0, y=100, relwidth=1)

    # Kalender

    # controllbar
    home_stdp_image = Image.open("images/hb.png")
    home_stdp_image = home_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    home_stdp_image = ImageTk.PhotoImage(home_stdp_image)
    button_stdp_home = tk.Button(app_stdp, image=home_stdp_image, text="Home", font=("Arial", 15), bg="white", command=Home)
    button_stdp_home.pack()
    button_stdp_home.place(x=50, y=650)

    noten_stdp_image = Image.open("images/nt.png")
    noten_stdp_image = noten_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    noten_stdp_image = ImageTk.PhotoImage(noten_stdp_image)
    button_stdp_noten = tk.Button(app_noten, image=noten_stdp_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Noten)
    button_stdp_noten.pack()
    button_stdp_noten.place(x=150, y=650)

    stdp_aufg_image = Image.open("images/stdp.png")
    stdp_aufg_image = stdp_aufg_image.resize((25, 25), resample=Image.LANCZOS)
    stdp_aufg_image = ImageTk.PhotoImage(stdp_aufg_image)
    button_aufg_stdp = tk.Button(app_stdp, image=stdp_aufg_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Stundenplan)
    button_aufg_stdp.pack()
    button_aufg_stdp.place(x=250, y=650)

    aufg_stdp_image = Image.open("images/afg.png")
    aufg_stdp_image = aufg_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    aufg_stdp_image = ImageTk.PhotoImage(aufg_stdp_image)
    button_stdp_aufg = tk.Button(app_kld, image=aufg_stdp_image, text="Aufgaben", font=("Arial", 15), bg="white", command=Aufgaben)
    button_stdp_aufg.pack()
    button_stdp_aufg.place(x=350, y=650)

    einstellungen_stdp_image = Image.open("images/est.png")
    einstellungen_stdp_image = einstellungen_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    einstellungen_stdp_image = ImageTk.PhotoImage(einstellungen_stdp_image)
    button_stdp_einstellungen = tk.Button(app_stdp, image=einstellungen_stdp_image, text="Einstellungen", font=("Arial", 15), bg="white", command=Einstellungen)
    button_stdp_einstellungen.pack()
    button_stdp_einstellungen.place(x=550, y=650)

    app_kld.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
# create settingswindow
def Einstellungen():
    from PIL import ImageTk, Image
    # app
    global app_noten
    global app_home
    global app_stdp
    global app_aufg
    global app_kld
    global app_est
    # andere Fenster schließen
    if app_home:
        app_home.destroy()
        app_home = None
    if app_stdp:
        app_stdp.destroy()
        app_stdp = None
    if app_noten:
        app_noten.destroy()
        app_noten = None
    if app_aufg:
        app_aufg.destroy()
        app_aufg = None
    if app_kld:
        app_kld.destroy()
        app_kld = None

    # app
    app_est = tk.Tk()
    app_est.title("Noten-App -- Einstellungen")
    app_est.geometry("600x700")
    app_est.resizable(False, False)
    app_est.geometry("+100+100")
    app_est.iconbitmap(icon_pfad)

    label_est_überschrift = tk.Label(app_est, text="Einstellungen", font=("Times New Roman", 40, "bold", "underline"))
    label_est_überschrift.pack()

    label_est_einleitung = tk.Label(app_est, text="", font=("Times New Roman", 20, "bold"))
    label_est_einleitung.pack()

    # strich
    strich_est=PhotoImage(file='images/strich.png')
    strich_est_label=Label(app_est, image=strich_est)
    strich_est_label.image=strich_est
    strich_est_label.place(x=0, y=100, relwidth=1)

    # Einstellungen
    def credits():
        messagebox.showinfo(title="Credits", message="Noten-App wurde von Jason Moser entwickelt. Viel Spaß beim nutzen! ✌️")
    credits_button = tk.Button(app_est, text="Credits", font=("Arial", 15), command=credits, bg="orange", fg="white", width=10)
    credits_button.pack()
    credits_button.place(x=50, y=150)

    # Hilfe
    def help():
        messagebox.showinfo(title="Hilfe", message="Wenn Sie Hilfe benötigen oder Vorschläge haben, wenden Sie sich bitte an mich über Discord: captain556788#7459")
    help_button = tk.Button(app_est, text="Hilfe", font=("Arial", 15), command=help, bg="green", fg="white", width=10)
    help_button.pack()
    help_button.place(x=50, y=350)

    # Version
    def version():
        messagebox.showinfo(title="Version", message="Version: 1.0")
    version_button = tk.Button(app_est, text="Version", font=("Arial", 15), command=version, bg="blue", fg="white", width=10)
    version_button.pack()
    version_button.place(x=300, y=150)

    # Datenschutz
    def datenschutz():
        messagebox.showinfo(title="Datenschutz", message="Es werden keine Daten gesammelt.")
    datenschutz_button = tk.Button(app_est, text="Datenschutz", font=("Arial", 15), command=datenschutz, bg="red", fg="white", width=10)
    datenschutz_button.pack()
    datenschutz_button.place(x=300, y=350)
    
    # controllbar
    home_stdp_image = Image.open("images/hb.png")
    home_stdp_image = home_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    home_stdp_image = ImageTk.PhotoImage(home_stdp_image)
    button_stdp_home = tk.Button(app_stdp, image=home_stdp_image, text="Home", font=("Arial", 15), bg="white", command=Home)
    button_stdp_home.pack()
    button_stdp_home.place(x=50, y=650)

    noten_stdp_image = Image.open("images/nt.png")
    noten_stdp_image = noten_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    noten_stdp_image = ImageTk.PhotoImage(noten_stdp_image)
    button_stdp_noten = tk.Button(app_noten, image=noten_stdp_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Noten)
    button_stdp_noten.pack()
    button_stdp_noten.place(x=150, y=650)

    stdp_aufg_image = Image.open("images/stdp.png")
    stdp_aufg_image = stdp_aufg_image.resize((25, 25), resample=Image.LANCZOS)
    stdp_aufg_image = ImageTk.PhotoImage(stdp_aufg_image)
    button_aufg_stdp = tk.Button(app_stdp, image=stdp_aufg_image, text="Stundenplan", font=("Arial", 15), bg="white", command=Stundenplan)
    button_aufg_stdp.pack()
    button_aufg_stdp.place(x=250, y=650)

    aufg_stdp_image = Image.open("images/afg.png")
    aufg_stdp_image = aufg_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    aufg_stdp_image = ImageTk.PhotoImage(aufg_stdp_image)
    button_stdp_aufg = tk.Button(app_kld, image=aufg_stdp_image, text="Aufgaben", font=("Arial", 15), bg="white", command=Aufgaben)
    button_stdp_aufg.pack()
    button_stdp_aufg.place(x=350, y=650)

    kld_stdp_image = Image.open("images/kld.png")
    kld_stdp_image = kld_stdp_image.resize((25, 25), resample=Image.LANCZOS)
    kld_stdp_image = ImageTk.PhotoImage(kld_stdp_image)
    button_stdp_kld = tk.Button(app_kld, image=kld_stdp_image, text="Kalender", font=("Arial", 15), bg="white", command=Kalender)
    button_stdp_kld.pack()
    button_stdp_kld.place(x=450, y=650)


    app_est.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
def Credits():
    messagebox.showinfo(title="Credits", message="Dieses Programm wurde von Jason Moser entwickelt.")

def Datenschutz():
    messagebox.showinfo(title="Datenschutz", message="Dieses Programm speichert keine Daten von Ihnen.")

def Kontakt():
    messagebox.showinfo(title="Kontakt", message="Kontaktieren Sie mich über Discord: captain556788#7459")
# -----------------------------------------------------------------------------------------------------------------------------------------

def validate_grade(P):
    # Diese Funktion überprüft, ob der eingegebene Wert eine gültige Note (1 bis 6) ist.
    if P.isdigit():
        grade = int(P)
        if 1 <= grade <= 6:
            return True
    return False

def add_note():
    noten_entry_text = noten_entry.get()
    fach_entry_text = fach_entry.get()


    if validate_grade(noten_entry_text):
        try:
            with open("notes.json", "r") as json_file:
                data = json.load(json_file)
        
        except FileNotFoundError:
            data = []

        found = False
        for entry in data:
            if entry.get("Fach") == fach_entry_text:
                entry["Noten"].append(noten_entry_text)
                found = True
                break

        if not found:
            new_entry = {"Fach": fach_entry_text, "Noten": [noten_entry_text]}
            data.append(new_entry)

        with open("notes.json", "w") as json_file:
            json.dump(data, json_file)

        noten_entry.delete(0, tk.END)

        # Aktualisieren Sie die Listbox, um die neuen Fächer anzuzeigen
        show_notes()
    else:
        messagebox.showerror(title="Fehler", message="Bitte geben Sie eine gültige Note ein. (1 bis 6)")

# -----------------------------------------------------------------------------------------------------------------------------------------
# noten anzeigen
def show_notes():
    try:
        with open("notes.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    noten_listbox.delete(0, tk.END)
    for entry in data:
        fach = entry.get("Fach")
        noten_listbox.insert(tk.END, fach)
# -----------------------------------------------------------------------------------------------------------------------------------------

def on_item_selected(event):
    # Diese Funktion wird aufgerufen, wenn ein Element in der Listbox ausgewählt wird
    selected_item = noten_listbox.get(noten_listbox.curselection())
    
    # Füge das ausgewählte Fach in das Eingabefeld für das Fach ein
    fach_entry.delete(0, tk.END)  # Lösche den aktuellen Inhalt des Eingabefelds
    fach_entry.insert(0, selected_item)  # Füge das ausgewählte Fach ein

    show_average_grades(selected_item)  # Zeige den Durchschnitt automatisch an


def on_item_right_click(event):
    # Diese Funktion wird aufgerufen, wenn mit der rechten Maustaste auf ein Fach in der Listbox geklickt wird
    selected_item = noten_listbox.get(noten_listbox.nearest(event.y))
    show_context_menu(event.x_root, event.y_root, selected_item)

def show_context_menu(x, y, selected_item):
    # Diese Funktion zeigt das Kontextmenü an
    context_menu = tk.Menu(app_noten, tearoff=0)
    context_menu.add_command(label="Noten anzeigen", command=lambda: show_grades(selected_item))
    context_menu.add_command(label="Fach bearbeiten", command=lambda: edit_subject(selected_item))
    context_menu.add_command(label="Fach löschen", command=lambda: delete_subject(selected_item))
    noten_listbox.context_menu = context_menu
    context_menu.post(x, y)

def show_grades(selected_item):
    try:
        with open("notes.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    for entry in data:
        if entry.get("Fach") == selected_item:
            grades = entry.get("Noten")
            messagebox.showinfo(title="Noten", message=f"Die Noten für das Fach {selected_item} sind: {grades}")
            break

def edit_subject(selected_item):
    new_name = simpledialog.askstring("Fach bearbeiten", f"Neuer Name für {selected_item}:")
    if new_name:
        # Aktualisieren Sie das Fach in der Listbox
        noten_listbox.delete(noten_listbox.curselection())
        noten_listbox.insert(tk.END, new_name)

        # Aktualisieren Sie das Fach in der JSON-Datei
        update_subject(selected_item, new_name)

def update_subject(old_name, new_name):
    try:
        with open("notes.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    for entry in data:
        if entry.get("Fach") == old_name:
            entry["Fach"] = new_name
            break

    with open("notes.json", "w") as json_file:
        json.dump(data, json_file)

def delete_subject(selected_item):
    response = messagebox.askyesno("Fach löschen", f"Möchten Sie das Fach {selected_item} wirklich löschen?")
    if response:
        noten_listbox.delete(noten_listbox.curselection())
    with open("notes.json", "r") as json_file:
        data = json.load(json_file)
    for entry in data:
        if entry.get("Fach") == selected_item:
            data.remove(entry)
            break
    with open("notes.json", "w") as json_file:
        json.dump(data, json_file)
    
# -----------------------------------------------------------------------------------------------------------------------------------------
# noten ausrrechnen
def calculate_average_grades(fach_name):
    try:
        with open("notes.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    except Exception as e:
        messagebox.showerror(title="Fehler", message=f"Fehler beim Laden der Daten: {str(e)}")

    grades = []  # Eine Liste, um die Noten für das Fach zu speichern

    for entry in data:
        if entry.get("Fach") == fach_name:
            # Annahme: Noten werden als Liste von Zeichenketten im "Noten" Feld gespeichert
            grades.extend([float(grade) for grade in entry.get("Noten", []) if grade.isdigit()])

    if grades:
        average = sum(grades) / len(grades)
        return average
    else:
        return None  # Keine Noten gefunden

# Zeigen Sie den Durchschnitt der Noten als Label an
def show_average_grades(selected_item):
    average = calculate_average_grades(selected_item)
    if average is not None:
        message = f"Durchschnittsnote für {selected_item}: {average:.2f}"
    else:
        message = f"Keine Noten gefunden für {selected_item}"
    
    # Aktualisieren Sie das Label mit dem Durchschnitt
    average_label.config(text=message)


# -----------------------------------------------------------------------------------------------------------------------------------------
Home()