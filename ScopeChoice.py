# Program ScopeChoice v.1 Author: Maciej Mindziak
import tkinter as Tk
from tkinter import messagebox
import Telescope as Tsc

def clear_window():

    fvalue_label.config(text='Światłosiła teleskopu:')
    maxzoom_label.config(text='Maksymalne użyteczne powiększenie:')
    minzoom_label.config(text='Minimalne użyteczne powiększenie:')
    max_eyepiece_focal_label.config(text='Maksymalna użyteczna ogniskowa okularu:')
    min_eyepiece_focal_label.config(text='Minimalna użyteczna ogniskowa okularu:')
    max_resolution_label.config(text='Zdolność rozdzielcza teleskopu:')
    max_magnitudo_label.config(text='Maksymalny zasięg teleskopu pod ciemnym niebem:')

def telescope_importer(event):

    clear_window()
    telescope = Tsc.Telescope()
    error_message =''
    try:
        focal = float(focal_entry.get())
    except ValueError:
        error_message = 'Nieprawidłowa wartość ogniskowej. Wpisz liczbę od 15 do 6,000'
    try:        
        diameter = float(diameter_entry.get())
    except ValueError:
        error_message = error_message + 'Nieprawidłowa wartość średnicy lustra. Wpisz liczbę od 30 do 2,000'
    try:        
        pupil = float(pupil_entry.get())
    except ValueError:
        error_message = error_message + 'Nieprawidłowa wartość źrenicy wyjściowej. Wpisz liczbę od 0 do 7'
    try:        
        multiplier = float(multiplier_entry.get())
    except ValueError:
        error_message = error_message + 'Nieprawidłowa wartość mnożnika średnicy teleskopu. Wpisz liczbę od 1 do 3'
    try:        
        skymag = float(skymag_entry.get())
    except ValueError:
        error_message = error_message + 'Nieprawidłowa wartość magnitudo. Wpisz liczbę od 0 do 7.5'        

    if error_message != '':
        messagebox.showerror(title='Sprawdź wartości',message=error_message)
    else:
        try:
            telescope.add_diameter_focal(focal,diameter)
            telescope.pupil = pupil
            telescope.multiplier = multiplier
            telescope.skymag = skymag
        except Exception as e:
            messagebox.showerror(title='Sprawdź wartości',message=e,)    

        fvalue_txt = 'Światłosiła teleskopu: F/' + str(telescope.calculate_fvalue())
        fvalue_label.config(text=fvalue_txt)

        maxzoom_txt = 'Maksymalne użyteczne powiększenie: ' + str(telescope.calculate_maxzoom()) + 'x'
        maxzoom_label.config(text=maxzoom_txt)
    
        minzoom_txt = 'Minimalne użyteczne powiększenie: ' + str(telescope.calculate_minzoom()) + 'x'
        minzoom_label.config(text=minzoom_txt)

        max_eyepiece_txt = 'Maksymalna użyteczna ogniskowa okularu: ' + str(telescope.calculate_max_eyepiece_focal()) + ' mm'
        max_eyepiece_focal_label.config(text=max_eyepiece_txt)

        min_eyepiece_txt = 'Minimalna użyteczna ogniskowa okularu: ' + str(telescope.calculate_min_eyepiece_focal()) + ' mm'
        min_eyepiece_focal_label.config(text=min_eyepiece_txt)

        max_resolution_txt = 'Zdolność rozdzielcza teleskopu: ' + str(telescope.calculate_resolution()) + '\"'
        max_resolution_label.config(text=max_resolution_txt)

        max_magnitudo_txt = 'Maksymalny zasięg teleskopu pod ciemnym niebem: ' + str(telescope.calculate_maxmagnitudo())+ ' mag'
        max_magnitudo_label.config(text=max_magnitudo_txt)


if __name__ == '__main__':

    root = Tk.Tk()
    root.title('Kalkulator parametrów teleskopu')
    frame = Tk.Frame(root, borderwidth=5)
    frame.grid(row=0, column=0)


    focal_label = Tk.Label(frame, text='Wpisz długość ogniskowej (zakres 15 mm - 6,000 mm):')
    focal_label.grid(sticky=Tk.E, row=1, column=0, padx=5, pady=5)
    focal_entry = Tk.Entry(frame, width=20)
    focal_entry.grid(sticky=Tk.W, row=1, column=1, padx=5, pady=5)

    diameter_label = Tk.Label(frame, text='Podaj średnicę lustra (zakres 30 mm - 2,000 mm) :')
    diameter_label.grid(sticky=Tk.E, row=2, column=0, padx=5, pady=5)
    diameter_entry = Tk.Entry(frame, width=20)
    diameter_entry.grid(sticky=Tk.W, row=2, column=1, padx=5, pady=5)

    pupil_label = Tk.Label(frame, text='Podaj maksymalną średnicę swojej źrenicy (zakres 0.5 mm - 7 mm):')
    pupil_label.grid(sticky=Tk.E, row=3, column=0, padx=5, pady=5)
    pupil_entry = Tk.Entry(frame, width=20)
    pupil_entry.grid(sticky=Tk.W, row=3, column=1, padx=5, pady=5)

    multiplier_label = Tk.Label(frame, text='Podaj mnożnik dla teleskopu w zależności sprawności optycznej (zakes 1- 3):')
    multiplier_label.grid(sticky=Tk.E, row=4, column=0, padx=5, pady=5)
    multiplier_entry = Tk.Entry(frame, width=20)
    multiplier_entry.grid(sticky=Tk.W, row=4, column=1, padx=5, pady=5)

    skymag_label = Tk.Label(frame, text='Podaj poziom jakości ciemnego nieba w magnitudo (zakres 0.0 mag - 7.5 mag):')
    skymag_label.grid(sticky=Tk.E, row=5, column=0, padx=5, pady=5)
    skymag_entry = Tk.Entry(frame, width=20)
    skymag_entry.grid(sticky=Tk.W, row=5, column=1, padx=5, pady=5)

    calculation_button = Tk.Button(frame, text='Pokaż parametry teleskopu')
    calculation_button.grid(sticky=Tk.E+Tk.W, row=6, column=0, columnspan=2,padx=5, pady=5)
    calculation_button.bind("<Button-1>", telescope_importer)


    fvalue_label = Tk.Label(frame, text='Światłosiła teleskopu:')
    fvalue_label.grid(sticky=Tk.E+Tk.W, row=7, column=0, columnspan=2, padx=5, pady=5)

    maxzoom_label = Tk.Label(frame, text='Maksymalne użyteczne powiększenie:')
    maxzoom_label.grid(sticky=Tk.E+Tk.W, row=8, column=0, columnspan=2, padx=5, pady=5)

    minzoom_label = Tk.Label(frame, text='Minimalne użyteczne powiększenie:')
    minzoom_label.grid(sticky=Tk.E+Tk.W, row=9, column=0, columnspan=2, padx=5, pady=5)

    max_eyepiece_focal_label = Tk.Label(frame, text='Maksymalna użyteczna ogniskowa okularu:')
    max_eyepiece_focal_label.grid(sticky=Tk.E+Tk.W, row=10, column=0, columnspan=2, padx=5, pady=5) 

    min_eyepiece_focal_label = Tk.Label(frame, text='Minimalna użyteczna ogniskowa okularu:')
    min_eyepiece_focal_label.grid(sticky=Tk.E+Tk.W, row=11, column=0, columnspan=2, padx=5, pady=5) 

    max_resolution_label = Tk.Label(frame, text='Zdolność rozdzielcza teleskopu:')
    max_resolution_label.grid(sticky=Tk.E+Tk.W, row=12, column=0, columnspan=2, padx=5, pady=5)

    max_magnitudo_label = Tk.Label(frame, text='Maksymalny zasięg teleskopu pod ciemnym niebem:')
    max_magnitudo_label.grid(sticky=Tk.E+Tk.W, row=13, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()
