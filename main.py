import pandas as pd
import pywhatkit as pyw
import time
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename
now = datetime.now()
future_minute = now.minute + 2
future_hour = now.hour


Tk().withdraw()
archivo_excel = askopenfilename(
    title="GGGGGGGGGG",
    filetypes=[("AAAAAAAA", "*.xlsx *.xls"), 
               ("Todos los archivos", "*.*")])

phone=pd.read_excel(archivo_excel)

waitting_time_to

for i in range(len(phone)):
    telefono=f"+57{phone.loc[i,"NUMBERS"].astype(str)}"
    nombre=phone.loc[i,"NAME"]
    msmchat=f"cod {nombre} Buen día, esta es una prueba de software de EDUNORTE por favor no contestar"
    time_hour = future_hour
    time_minute = future_minute
    pyw.sendwhatmsg(telefono, msmchat, time_hour, time_minute, waiting_time_to_send, close_tab)
    time.sleep(20)

    # Actualizar hora para el próximo mensaje (+1 minuto)
    future_minute += 1
    if future_minute >= 60:
            future_minute = 0
            future_hour += 1

base.mainloop()