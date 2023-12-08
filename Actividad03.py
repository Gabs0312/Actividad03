import tkinter as tk
ventana = tk.Tk()
ventana.geometry("910x300")
ventana.title("Conversor de Coordenadas")
ventana.config(bg='pink')
etiq_DD = tk.Label(ventana, text = 'Grados Decimales', bg= "pink", justify= 'center', font= 'Helvetica 15')
etiq_DD.grid(row = 1, column= 2)
etiq_latDD = tk.Label(ventana, text = "Latitud:", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_latDD.grid(row= 2, column=1)
caja_DDlat = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_DDlat.grid(row= 2, column= 2 )
etiq_signolati = tk.Label(ventana, text = '°', bg= "pink", font= 'Helvetica 14', anchor=tk.W)
etiq_signolati.grid(row=2, column=3) 
etiq_lonDD = tk.Label(ventana, text = "Longitud:", bg= "pink", justify= 'left', font= 'Helvetica 14')
etiq_lonDD.grid(row= 3, column=1)
caja_DDlon = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_DDlon.grid(row= 3, column= 2 )
etiq_signolon = tk.Label(ventana, text = '°', bg= "pink", font= 'Helvetica 14')
etiq_signolon.grid(row=3, column=3) 
etiq_GMS = tk.Label(ventana, text = 'Grados', bg= "pink", justify= 'center', font= 'Helvetica 15')
etiq_GMS.grid(row = 7, column= 2)
etiq_MGMS = tk.Label(ventana, text = 'Minutos', bg= "pink", justify= 'center', font= 'Helvetica 15')
etiq_MGMS.grid(row = 7, column= 4)
etiq_GMSS = tk.Label(ventana, text = 'Segundos', bg= "pink", justify= 'center', font= 'Helvetica 15')
etiq_GMSS.grid(row = 7, column= 6)
etiq_GMSlat = tk.Label(ventana, text = "Latitud", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_GMSlat.grid(row= 8, column= 1)
caja_GMSlatG = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlatG.grid(row= 8, column= 2 )
etiq_signolatig = tk.Label(ventana, text = '°', bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolatig.grid(row=8, column=3) 
caja_GMSlatM = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlatM.grid(row= 8, column= 4 )
etiq_signolatim = tk.Label(ventana, text = "'", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolatim.grid(row=8, column= 5)
caja_GMSlatS = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlatS.grid(row= 8, column= 6 )
etiq_signolatis = tk.Label(ventana, text = "''", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolatis.grid(row=8, column= 7)
etiq_GMSlon = tk.Label(ventana, text = "Longitud:", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_GMSlon.grid(row= 9, column= 1) 
caja_GMSlonG = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlonG.grid(row= 9, column= 2 )
etiq_signolong = tk.Label(ventana, text = '°', bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolong.grid(row=9, column=3)
caja_GMSlonM = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlonM.grid(row= 9, column= 4 )
etiq_signolonm = tk.Label(ventana, text = "'", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolonm.grid(row=9, column= 5)
caja_GMSlonS = tk.Entry(ventana, font= 'Helvetica 14', justify= 'center')
caja_GMSlonS.grid(row= 9, column= 6 )
etiq_signolons = tk.Label(ventana, text = "''", bg= "pink", justify= 'center', font= 'Helvetica 14')
etiq_signolons.grid(row=9, column= 7)
direc_lat = tk.StringVar(ventana)
direc_lat.set('N')
opcion_direclat = ['N', 'S']
direcciones = tk.OptionMenu(ventana, direc_lat, *opcion_direclat)
direcciones.grid(row=8, column=8)
direc_lon = tk.StringVar(ventana)
direc_lon.set('E')
opcion_direclon = ['E', 'W']
direccion = tk.OptionMenu(ventana, direc_lon, *opcion_direclon)
direccion.grid(row=9, column=8)
def DDlat_DMS():
    lat = float(caja_DDlat.get())
    lat_grd = float(caja_DDlat.get())
    result3 = int(abs(lat))
    caja_GMSlatG.delete(0, tk.END)
    caja_GMSlatG.insert(tk.END, result3)
    result_min = (abs(lat)-result3) * 60 
    result4 = int(result_min)
    if result4 < 0:
        result4 *= -1
    caja_GMSlatM.delete(0, tk.END)
    caja_GMSlatM.insert(tk.END, result4)
    result5 = (result_min - result4) * 60
    if result5 <0:
        result5*= -1
    caja_GMSlatS.delete(0, tk.END)
    caja_GMSlatS.insert(tk.END, round( result5, 3))
    if lat > 0:
        direc_lat.set('N')
    else:
        direc_lat.set('S')    
def DDlon_DMS():
    lon = float(caja_DDlon.get())
    lon_grd = float(caja_DDlon.get())
    result = int(abs(lon))
    caja_GMSlonG.delete(0, tk.END)
    caja_GMSlonG.insert(tk.END, result)
    lon_min_res = (abs(lon) - result) * 60
    result1 =int(lon_min_res)
    if result1 <0:
        result1*= -1
    caja_GMSlonM.delete(0, tk.END)
    caja_GMSlonM.insert(tk.END, result1)
    result2 =  (lon_min_res - result1 ) * 60
    if result2 <0:
        result2*= -1
    caja_GMSlonS.delete(0, tk.END)
    caja_GMSlonS.insert(tk.END, round (result2, 3))
    if lon > 0:
        direc_lon.set('E')
    else:
        direc_lon.set('W')
def DDmain():
    DDlat_DMS() 
    DDlon_DMS()
def GMSlat_DD():
    GMSlat_G = float(caja_GMSlatG.get())
    GMSlat_M = float(caja_GMSlatM.get())
    GMSlat_S = float(caja_GMSlatS.get())
    result5 = float(GMSlat_G) + GMSlat_M /60.0 + GMSlat_S/3600.0
    caja_DDlat.delete(0, tk.END)
    if direc_lat.get() != opcion_direclat[1]:
        caja_DDlat.insert(tk.END, round(result5, 3))
    else:
        caja_DDlat.insert(tk.END, round(-result5, 3))
def GMSlon_DD():
    GMSlon_G = float(caja_GMSlonG.get())
    GMSlon_M = float(caja_GMSlonM.get())
    GMSlon_S = float(caja_GMSlonS.get())
    result6 = float(GMSlon_G) + GMSlon_M /60.0 + GMSlon_S/3600.0
    caja_DDlon.delete(0, tk.END)
    if direc_lon.get() != opcion_direclon[1]:
        caja_DDlon.insert(tk.END, round(result6, 3))
    else:
        caja_DDlon.insert(tk.END, round(-result6, 3))
def GMSconver():
    GMSlon_DD()
    GMSlat_DD()
botonDD_GMS =tk.Button(text= 'Convertir DD a GMS', font= 'Helvetica 14', command = DDmain)
botonDD_GMS.grid(row = 3, column = 4)
botonGMS_DD =tk.Button(text= 'Convertir GMS a DD', font= 'Helvetica 14', command = GMSconver)
botonGMS_DD.grid(row = 11, column = 2)
ventana.mainloop()    