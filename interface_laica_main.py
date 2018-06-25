import tkinter as tk
from tkinter import ttk
import csv
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
import numpy as np

''' Importando Bibliotecas --> UBUNTU:
        sudo pip3 install pandas
        sudo apt-get install python3-pil python3-pil.imagetk
        sudp apt install PIL
    Importante Bibliotecas --> Windows:
        python -m pip insall --upgrade pip
        pip install Pillow
        pip instal Image
        pip install pandas
'''

class LaicaApp(tk.Frame):

    def __init__(self,master):
        # Criando Frame
        self.frame_total = tk.Frame.__init__(self, master)
        self.pack()

        # importando estacoes
        data_estacoes = pd.read_csv("estacoes.csv", sep=",")
        estacaoList = data_estacoes['estacao'].values.tolist()

        # Editando Frame Master
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width_of_window = 500
        height_of_window = 250

        x_coordinate = (screen_width/2) - (width_of_window/2)
        y_coordinate = (screen_height/2) - (height_of_window/2)
        self.master.title("Data Quality Software")
        self.master.configure(bg="white")
        self.master.overrideredirect(False)
        self.master.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        # Estilo da Frame Master
        tk.Label(self.master, height=1, bg="#66cccc").pack(fill= tk.BOTH)

        # Fontes
        label_titulo= 'Verdana 12'
        label_frases= ' Verdana 9'





        def criando_abas():
            self.abas = ttk.Notebook(self.frame_total)
            # ABA1
            self.frame_aba1 = tk.Frame(self.abas)
            self.abas.add(self.frame_aba1, text= "Importar Arquivo")
            self.frame_aba1.configure(bg="white")
            # ABA2
            self.frame_aba2 = tk.Frame(self.abas)
            self.abas.add(self.frame_aba2, text= "Qualificações")
            self.frame_aba2.configure(bg="white")

            self.abas.pack(fill=tk.BOTH, expand=1)
        criando_abas()

        # Labelframe -> Importar Arquivo
        def importarLabelFrame():
            self.importar_labelframe = tk.LabelFrame(self.frame_aba1, text="Importar Arquivo", font=label_titulo)
            self.importar_labelframe.configure(bg="white")
            self.importar_labelframe.pack(fill=tk.BOTH, padx=15, pady=(20, 0))

            self.importarLabel = tk.Label(self.importar_labelframe, text="Importe o arquivo em formato .csv: ", bg="white", font=label_frases).pack(side=tk.LEFT, padx=(30,0), pady=20)
        importarLabelFrame()


        def res_texto(res):
            self.label_verifica_arquivo.config(text=res)

        #Verificando se o arquivo está adequado
        def verificarArquivo(ncol):
            if ncol >= 4:
                res = "O arquivo está correto."
                res_texto(res)

            elif ncol<4 :
                res = "O arquivo está incorreto."
                res_texto(res)


        #Abrindo para pesquisar o diretório e definindo data
        def diretorio():
            diretorio_nome = filedialog.askopenfilename(initialdir="C:/Users/Username/Documents/",
                                   filetypes=(("Text CSV", "*.csv"),("Text File", "*.txt")),
                                   title="Escolha o arquivo para qualificar" )

            data= pd.read_csv(diretorio_nome, sep=",")
            ncol = len(data.columns)
            verificarArquivo(ncol)

        self.botao2 = tk.Button(self.importar_labelframe, text="Procurar Arquivo", bg="#66cccc", width=20, command=(lambda: diretorio()))
        self.botao2.pack(side=tk.LEFT, padx=55, ipady=5)
        res = " "
        self.label_verifica_arquivo = tk.Label(self.importar_labelframe, text=res, bg="white", font=label_frases)
        self.label_verifica_arquivo.pack(side=tk.LEFT)


        # Labelframe -> Selecionar Estação
        self.selecionar_labelframe = tk.LabelFrame(self.frame_aba1, text="Selecione a estação",bg="white", font=label_titulo)
        self.selecionar_labelframe.pack(fill= tk.BOTH, padx=15, pady=(20,0))


        # Criando combobox

        estacao_var = tk.StringVar()
        estacao_var.set('Selecione a estação')
        self.combo = ttk.Combobox(self.selecionar_labelframe, textvariable = estacao_var, values = estacaoList, width=30)
        self.combo.pack(side=tk.LEFT,anchor=tk.NW,padx=(40,0), pady=(30,0))

        # check das variaveis
        year_check1 = tk.IntVar()
        day_check1 = tk.IntVar()
        mit_check1 = tk.IntVar()
        glo_check1 = tk.BooleanVar()
        dni_check1 = tk.BooleanVar()
        dif_check1 = tk.BooleanVar()
        lw_check1 = tk.BooleanVar()
        par_check1 = tk.BooleanVar()
        lux_check1 = tk.BooleanVar()
        tp_check1 = tk.BooleanVar()
        umi_check1 = tk.BooleanVar()
        press_check1 = tk.BooleanVar()
        rain_check1 = tk.BooleanVar()
        wspe_check1 = tk.BooleanVar()
        wdr_check1 = tk.BooleanVar()


        # convertendo decimais:


        def conversao_lat(graus, minutos, segundos):
            lat = float(graus) + float(minutos)/60 + float(segundos)/3600
            print("Latitude ok:%s" % lat)
            return(lat)
        def conversao_lon(grauss, minutoss, segundoss):
            lon = float(grauss) + float(minutoss)/60 + float(segundoss)/3600
            print("Longitude ok:%s" % lon)
            return(lon)

        #Validando Entrys

        def check_estacao(estacao):
            i = 0
            for letra in range(len(estacao)):
                try:
                    int(estacao[letra])
                    i = i + 1
                except ValueError:
                    None

            if (i == 0):
                estacao = str(estacao)
                print("Estação Ok")
            else:
                print("Estação contêm nome inválido")

        def check_estado(estado):
            i = 0
            for letra in range(len(estado)):
                try:
                    int(estado[letra])
                    i = i + 1
                except ValueError:
                    None

            if (i == 0):
                estado = str(estado)
                check_estacao_texto = ""
            else:
                check_estacao_texto = "Estação contêm um nome inválido."

        def check_lat_graus(graus):
            try:
                float(graus)
                check_lat_gtexto = ""

            except ValueError:
                check_lat_gtexto = "Graus da latitude inválida."

        def check_lat_min(minutos):
            try:
                float(minutos)
                check_lon_mtexto = ""
            except ValueError:
                check_lon_mtexto = "Minutos da latitude inválida."

        def check_lat_seg(segundos):
            try:
                float(segundos)
                check_lat_stexto = ""
            except ValueError:
                check_lat_stexto = "Segundos da latitude inválida."

        def check_lon_graus(grauss):
            try:
                float(grauss)
                check_lon_gtexto = ""
            except ValueError:
                check_lon_gtexto = "Graus da longitude inválda."

        def check_lon_min(minutoss):
            try:
                float(minutoss)
                check_lon_mtexto = ""
            except ValueError:
                check_lon_mtexto = "Minutos da longitude inválida."

        def check_lon_seg(segundoss):
            try:
                float(segundoss)
                check_lon_stexto = ""
            except ValueError:
                check_lon_stexto = "Segundos da longitude inválida."

        def check_alt(alt):
            try:
                float(alt)
                check_alt_texto = ""
            except ValueError:
                check_alt_texto = "Altitude inválida."

        def check_temp_max(temp_max):
            try:
                float(temp_max)
                check_tempo_max_texto = ""

            except ValueError:
                check_tempo_max_texto = "Temperatura Máxima inválida."

        def check_temp_min(temp_min):
            try:
                float(temp_min)
                check_tempo_min_texto = ""

            except ValueError:
                check_tempo_min_texto = "Temperatura Minima inválida."

        def check_rain_max(rain_max):
            try:
                float(rain_max)
                check_rain_max_texto = ""
            except ValueError:
                check_rain_max_texto = "Precipitação máxima inválida"

        def hello():
            messagebox.showinfo("Say Hello", "Hello World")

        #Adicionando uma nova estação
        def adcionar_estacao():
            estacao = self.entry_nome.get()
            check_estacao(estacao)

            estado = self.entry_estado.get()
            check_estado(estado)

            graus = self.latgraus.get()
            check_lat_graus(graus)

            minutos = self.latmin.get()
            check_lat_min(minutos)
            segundos = self.latseg.get()
            check_lat_seg(segundos)
            lat = conversao_lat(graus,minutos,segundos)

            grauss = self.longraus.get()
            check_lon_graus(grauss)
            minutoss = self.lonmin.get()
            check_lon_min(minutoss)
            segundoss = self.lonseg.get()
            check_lon_seg(segundoss)
            lon = conversao_lon(grauss,minutoss,segundoss)

            alt = self.entry_altitude.get()
            check_alt(alt)

            temp_max = self.entry_tmax_abs.get()
            check_temp_max(temp_max)

            temp_min = self.entry_tmin_abs.get()
            check_temp_min(temp_min)

            rain_max = self.entry_precipitacao.get()
            check_rain_max(rain_max)

            hello()



            with open('estacoes.csv', 'a', newline='') as estacaoFile:
                estacaoFileWriter = csv.writer(estacaoFile)
                estacaoFileWriter.writerow([estacao,estado,lat,lon,alt,temp_max,temp_min,rain_max])

            estacaoFile.close()
            print( "Estacao: %s, Estado: %s, Latitude: %s, Longitude: %s, Altitude: %s, Temperatura Máxima: %s, Temperatura Mínima: %s, Precipitação: %s" % (estacao,estado,lat,lon,alt,temp_max,temp_min,rain_max))
            day = 15
            mit = 1548
            const_Sa(day)
            cos_M0(lat,lon,day,mit)

        def continuar():

            modo2 = "disable"
            bg_botao2 = "#E6E6E6"
            modo_voltar_2(modo2, bg_botao2)

            pegando_variaveis()
            criandolabel_parametros()

            index_var = tk.StringVar()
            index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            #######

            parametro_ano(year_check1, index, index_var)
            parametro_dia(day_check1, index, index_var)
            parametro_min(mit_check1, index, index_var)
            parametro_glo(glo_check1, index, index_var)
            parametro_dni(dni_check1, index, index_var)
            parametro_dif(dif_check1, index, index_var)
            parametro_lw(lw_check1, index, index_var)
            parametro_lux(lux_check1, index, index_var)
            parametro_par(par_check1, index, index_var)
            parametro_tp(tp_check1, index, index_var)
            parametro_press(press_check1, index, index_var)
            parametro_umi(umi_check1, index, index_var)
            parametro_rain(rain_check1, index, index_var)
            parametro_wdr(wdr_check1, index, index_var)
            parametro_wspe(wspe_check1, index, index_var)
            botoes_parametros()
            botoes_parametro2()


        def voltar():
            self.outra_labelframe.destroy()
            modo = "normal"
            bg_botao = "#66cccc"
            modo_voltar(modo, bg_botao)

        def voltar2():
            self.parametros_labelframe_total.destroy()

            modo = "normal"
            bg_botao = "#66cccc"
            modo_voltar(modo, bg_botao)

        def voltar3():
            self.parametros_labelframe_total.destroy()

            modo2 = "normal"
            bg_botao2 = "#66cccc"
            modo_voltar_2(modo2, bg_botao2)


        def modo_voltar(modo, bg_botao):
            self.botao.config(state=modo, bg= bg_botao)

        def modo_voltar_2(modo2, bg_botao2):
            self.butao_outros_3.config(state=modo2, bg=bg_botao2)



        def check():
            if estacao_var.get() == 'Outros':
                modo = "disable"
                bg_botao = "#E6E6E6"
                cor_certa = "#FAFAFA"
                cor_certa_2 = "black"
                modo_voltar(modo, bg_botao)
                self.outra_labelframe = tk.LabelFrame(self.frame_aba1, text="Nova Estação", font=label_titulo)
                self.outra_labelframe.configure(bg="white")
                self.outra_labelframe.pack(fill= tk.BOTH, padx=15, pady=(20,0))

                # Entrada de dados da estação #
                ttk.Style().configure("TEntry", padding=10, relief="flat", background="#ccc")
                #Nome_Estação

                titulo_estacao = "Nome da Estação:"
                self.nomeLabel = tk.Label(self.outra_labelframe,text=titulo_estacao, bg="white", font="Verdana 8").grid(row=0, column=0, sticky=tk.E, pady=10, padx=(30,30))
                self.nome_nova_estacao = tk.StringVar()
                self.entry_nome = tk.Entry(self.outra_labelframe, textvariable=self.nome_nova_estacao, width=25)

                self.entry_nome.config(bg = cor_certa, fg= cor_certa_2)
                self.entry_nome.grid(row=0, column=1)
                #Nome_Esstado
                titulo_estado = "Estado da Estação: "
                self.estadoLabel = tk.Label(self.outra_labelframe, text=titulo_estado, bg="white")
                self.estadoLabel.grid(row=1, column=0, sticky=tk.E, pady=(0,10), padx=(30,30))
                self.novo_estado = tk.StringVar()
                self.entry_estado = tk.Entry(self.outra_labelframe, textvariable=self.novo_estado, width=25)
                self.entry_estado.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_estado.grid(row=1, column=1)

                # Latitude
                titulo_latitude = "Latitude(graus): "
                self.latitudeLabel = tk.Label(self.outra_labelframe, text=titulo_latitude, bg="white")
                self.latitudeLabel.grid(row=2,column=0,sticky=tk.E,pady=(0, 10),padx=(30, 30))

                # frame
                self.nova_latFrame = tk.Frame(self.outra_labelframe, bg="white")
                self.nova_latFrame.grid(row=2, column=1)
                # Graus
                self.labelgraus = tk.Label(self.nova_latFrame, text="°", bg="white", font=14)
                self.labelgraus.grid(row=0, column=1)

                self.latgraus = tk.StringVar()
                self.entry_latitude_graus = tk.Entry(self.nova_latFrame, textvariable=self.latgraus, width=5)
                self.entry_latitude_graus.config(bg=cor_certa, fg=cor_certa_2)

                self.entry_latitude_graus.grid(row=0, column=0)

                # Minuto

                self.latmin = tk.StringVar()
                self.entry_latitude_min = tk.Entry(self.nova_latFrame, textvariable=self.latmin, width=6)
                self.entry_latitude_min.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_latitude_min.grid(row=0, column=2)
                self.labelmin = tk.Label(self.nova_latFrame, text="'", bg="white", font=14)
                self.labelmin.grid(row=0, column=3)

                # Segundos

                self.latseg = tk.StringVar()
                self.entry_latitude_seg = tk.Entry(self.nova_latFrame, textvariable=self.latseg, width=6)
                self.entry_latitude_seg.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_latitude_seg.grid(row=0, column=4)
                self.labelseg = tk.Label(self.nova_latFrame, text="''", bg="white", font=14)
                self.labelseg.grid(row=0, column=5)

                # Longitude
                titulo_longitude = "Longitude(graus): "
                self.longitudeLabel = tk.Label(self.outra_labelframe, bg="white")
                self.longitudeLabel.config(text=titulo_longitude)
                self.longitudeLabel.grid(row=3,column=0,sticky=tk.E,pady=(0, 10),padx=(30, 30))

                # frame
                self.nova_lonFrame = tk.Frame(self.outra_labelframe, bg="white")
                self.nova_lonFrame.grid(row=3, column=1)
                # Graus
                self.labelgrauss = tk.Label(self.nova_lonFrame, text="°", bg="white", font=14)
                self.labelgrauss.grid(row=0, column=1)

                self.longraus = tk.StringVar()
                self.entry_longitude_graus = tk.Entry(self.nova_lonFrame, textvariable=self.longraus, width=5)
                self.entry_longitude_graus.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_longitude_graus.grid(row=0, column=0)

                # Minuto

                self.lonmin = tk.StringVar()
                self.entry_longitude_min = tk.Entry(self.nova_lonFrame, textvariable=self.lonmin, width=6)
                self.entry_longitude_min.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_longitude_min.grid(row=0, column=2)
                self.labelminn = tk.Label(self.nova_lonFrame, text="'", bg="white", font=14)
                self.labelminn.grid(row=0, column=3)

                # Segundos

                self.lonseg = tk.StringVar()
                self.entry_longitude_seg = tk.Entry(self.nova_lonFrame, textvariable=self.lonseg, width=6)
                self.entry_longitude_seg.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_longitude_seg.grid(row=0, column=4)
                self.labelsegg = tk.Label(self.nova_lonFrame, text="''", bg="white", font=10)
                self.labelsegg.grid(row=0, column=5)

                #Altitude
                titulo_altitude =  "Altitude(m): "
                self.altitudeLabel = tk.Label(self.outra_labelframe,text=titulo_altitude, bg="white")
                self.altitudeLabel.grid(row=0, column=2, sticky=tk.E, pady=(0,10), padx=(50,30))
                self.nova_altitude = tk.StringVar()
                self.entry_altitude = tk.Entry(self.outra_labelframe, textvariable=self.nova_altitude, width=25)
                self.entry_altitude.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_altitude.grid(row=0, column=3)

                #Temperatura maxima absoluta
                titulo_t_max = "Temperatura máxima absoluta(°C): "
                self.tmaxLabel = tk.Label(self.outra_labelframe, text=titulo_t_max, bg="white")
                self.tmaxLabel.grid(row=1, column=2, sticky=tk.E, pady=(0,10), padx=(50,30))
                self.nova_tmax_abs = tk.StringVar()
                self.entry_tmax_abs = tk.Entry(self.outra_labelframe, textvariable=self.nova_tmax_abs, width=25)
                self.entry_tmax_abs.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_tmax_abs.grid(row=1, column=3)

                #Temperatura minima absoluyta
                titulo_t_min = "Temperatura mínima absoluta(°C): "
                self.tminLabel = tk.Label(self.outra_labelframe, text=titulo_t_min, bg="white")
                self.tminLabel.grid(row=2, column=2, sticky=tk.E, pady=(0,10), padx=(50,30))
                self.nova_tmin_abs = tk.StringVar()
                self.entry_tmin_abs = tk.Entry(self.outra_labelframe, textvariable=self.nova_tmin_abs, width=25)
                self.entry_tmin_abs.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_tmin_abs.grid(row=2, column=3)
                #Precipitação
                titulo_rain = "Precipitação máxima absoluta(mm): "
                self.tminLabel = tk.Label(self.outra_labelframe, text=titulo_rain,bg="white")
                self.tminLabel.grid(row=3, column=2, sticky=tk.E, pady=(0,10), padx=(50,30))
                self.nova_precipitacao = tk.StringVar()
                self.entry_precipitacao = tk.Entry(self.outra_labelframe, textvariable=self.nova_precipitacao, width=25)
                self.entry_precipitacao.config(bg=cor_certa, fg=cor_certa_2)
                self.entry_precipitacao.grid(row=3, column=3)


                # Botao #

                modo2 = "normal"
                bg_botao2 = "#66cccc"
                self.butao_outros = tk.Button(self.outra_labelframe, text = "Salvar nova estação", command=adcionar_estacao, bg="#66cccc", width= 30)
                self.butao_outros.grid(row=4, column=1,ipady=5, pady=20)

                self.butao_outros_2 = tk.Button(self.outra_labelframe, text="Continuar" , command=continuar, bg="#66cccc", width= 20)
                self.butao_outros_2.grid(row=4, column=2, ipady=5, pady=20)


                self.butao_outros_3 = tk.Button(self.outra_labelframe, text="Voltar",command=voltar, width=20)
                self.butao_outros_3.config(state=modo2, bg=bg_botao2)
                self.butao_outros_3.grid(row=4, column=3, ipady=5, pady=20)

            elif estacao_var.get() == 'Selecione a estação':
                None

            else:
                modo = "disable"
                bg_botao = "#E6E6E6"
                modo_voltar(modo,bg_botao)
                pegando_variaveis()
                criandolabel_parametros()

                index_var = tk.StringVar()
                #pegar o index do data
                index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


                #######

                parametro_ano(year_check1, index, index_var)
                parametro_dia(day_check1, index, index_var)
                parametro_min(mit_check1, index, index_var)
                parametro_glo(glo_check1, index, index_var)
                parametro_dni(dni_check1, index, index_var)
                parametro_dif(dif_check1, index, index_var)
                parametro_lw(lw_check1, index, index_var)
                parametro_lux(lux_check1, index, index_var)
                parametro_par(par_check1, index, index_var)
                parametro_tp(tp_check1, index, index_var)
                parametro_press(press_check1, index, index_var)
                parametro_umi(umi_check1, index, index_var)
                parametro_rain(rain_check1, index, index_var)
                parametro_wdr(wdr_check1, index, index_var)
                parametro_wspe(wspe_check1, index, index_var)



                botoes_parametros()
                botoes_parametro1()


        modo = "normal"
        bg_botao ="#66cccc"
        self.botao = tk.Button(self.selecionar_labelframe, text="Verificar", command=check, width= 20)
        self.botao.config(state=modo, bg=bg_botao)
        self.botao.pack(side=tk.LEFT,anchor=tk.NW,padx=(73,0), pady=(25,0), ipady=5)

        photo1 = ImageTk.PhotoImage(Image.open("estacoes.png"))
        self.imagem_selecionar = tk.Label(self.selecionar_labelframe, image=photo1, bg="white")
        self.imagem_selecionar.img = photo1
        self.imagem_selecionar.pack(side=tk.TOP, anchor=tk.NE, padx=(0,20), pady=(0,5))
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width_of_window = 500
        height_of_window = 250

        x_coordinate = (screen_width/2) - (width_of_window/2)
        y_coordinate = (screen_height/2) - (height_of_window/2)
        def pop(msg):
            popup = tk.Tk()
            popup.wm_title("Info")
            popup.configure(bg="white")
            popup.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window, x_coordinate, y_coordinate))
            tk.Label(popup, height=1, bg="#66cccc").pack(fill=tk.BOTH)

            label = tk.Label(popup, text=msg, font = label_frases, bg="white")
            label.pack(side="top", fill="x", padx=10, pady=10)
            bt1 = tk.Button(popup, text="Voltar", command = popup.destroy, bg="#66cccc", width= 10)
            bt1.pack(ipady=2)
            popup.mainloop()

        def pegando_variaveis():
            variaveisList = data_estacoes.columns.values.tolist()
            dic_nomeEstacoes = {}
            dic_estacaoEscolhida = {}

            for estacao in range(len(estacaoList)):
                dic_nomeEstacoes[estacaoList[estacao]] = "%s" % estacao
            indexEstacao = int(dic_nomeEstacoes[estacao_var.get()])

            for nome_variavel in variaveisList:
                dic_estacaoEscolhida[nome_variavel] = data_estacoes.loc[indexEstacao][nome_variavel]
            estacao = str(dic_estacaoEscolhida['estacao'])
            estado = str(dic_estacaoEscolhida['estado'])
            lat = float(dic_estacaoEscolhida['lat'])
            lon = float(dic_estacaoEscolhida['lon'])
            alt = float(dic_estacaoEscolhida['alt'])
            temp_max = float(dic_estacaoEscolhida['temp_max'])
            temp_min = float(dic_estacaoEscolhida['temp_min'])
            rain_max = float(dic_estacaoEscolhida['rain_max'])

            print(
                "Estacao: %s, Estado: %s, Latitude: %s, Longitude: %s, Altitude: %s, Tempe Max: %s, Temp Min: %s, Rain: %s" % (
                    estacao, estado, lat, lon, alt, temp_max, temp_min, rain_max))

            day= 25
            mit= 125
            const_Sa(day)
            cos_M0(lat, lon, day, mit)

        def const_Sa(day):
            S0 = 1367  # Solar constant in W/m^2
            G = 2 * np.pi * (day - 1) / 365  # Day angle (G)
            E0 = 1.000110 + 0.034221 * np.cos(G) + 0.001280 * np.sin(G) + 0.000719 * np.cos(2 * G) + 0.000077 * np.sin(2 * G)  # Eccentricity correction factor (E0)
            Sa = S0 * E0
            print("Sa = %s" % Sa)
            return Sa

        # Zenith angle cosine (M0)
        def cos_M0(lat, lon, day, mit):  # latitude, longitude, day of the year and minute of the day
            G = 2 * np.pi * (day - 1) / 365  # Day angle (G)
            te = (0.000075 + 0.001868 * np.cos(G) - 0.032077 * np.sin(G) - 0.014615 * np.cos(2 * G) - 0.04089 * np.sin(2 * G)) * (229.18)  # Time Equation (Te) in minutes
            sh = mit + 4 * (lon) + te  # Solar hour (sh) in minutes
            w = (12 - (sh / 60)) * 15 * np.pi / 180  # Hour angle in radians
            d = 0.006918 - 0.399912 * np.cos(G) + 0.070257 * np.sin(G) - 0.006758 * np.cos(2 * G) + 0.000907 * np.sin(2 * G) - 0.02697 * np.cos(3 * G) + 0.00148 * np.sin(3 * G)  # declination in radians
            M0 = np.sin(d) * np.sin(lat) + np.cos(d) * np.cos(w) * np.cos(lat)  # Zenith angle cosine in radians
            print("M0 = %s" % M0)
            return M0

        def criandolabel_parametros():
            self.parametros_labelframe_total = tk.LabelFrame(self.frame_aba1, text="Selecione as variáveis para qualificar", font=label_titulo)
            self.parametros_labelframe_total.configure(bg="white")
            self.parametros_labelframe_total.pack(fill=tk.BOTH, padx=15, pady=(20, 0))
            self.parametros_infoFrame = tk.Frame(self.parametros_labelframe_total, bg="white")
            self.parametros_infoFrame.pack(anchor=tk.W)
            self.parametros_infoLabel = tk.Label(self.parametros_infoFrame,  text="Indique a coluna correspondente da planilha com a variável", bg="white", font=label_frases)
            self.parametros_infoLabel.grid(row=0, column=0, padx=20, pady=15)
            self.parametros_labelframe=tk.Frame(self.parametros_labelframe_total, bg="white")
            self.parametros_labelframe.pack(side=tk.LEFT)

        def parametro_ano(year_check1,index, index_var):

            msg = "O arquivo deve conter obrigatoriamente\na primeira coluna indicando o ano dos dados coletados."

            V1 = tk.Checkbutton(self.parametros_labelframe, text="Ano", variable=year_check1, onvalue=1, offvalue=0,
                                bg="white")
            B1 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C1 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V1.grid(row=0, column=2, sticky=tk.W, pady=2, padx=(1, 0))
            B1.grid(row=0, column=1, sticky=tk.W, pady=2, padx=0)
            C1.grid(row=0, column=0, pady=2, padx=(20, 0))


        def parametro_dia(day_check1,index, index_var):
            msg = "A segunda coluna é obrigatoriamente referente aos minutos.\n O arquivo deve conter uma sequência temporal de minuto a minuto.\nExemplo: 0,1,2...1439,0,1. \n\nLembrando que um dia possui de 0 à 1439 minutos"

            V2 = tk.Checkbutton(self.parametros_labelframe, text="Dia", variable=day_check1, onvalue=1, offvalue=0, bg="white")
            B2 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C2 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V2.grid(row=1, column=2, sticky=tk.W, pady=2, padx=(1, 0))
            B2.grid(row=1, column=1, sticky=tk.W, pady=2, padx=0)
            C2.grid(row=1, column=0, padx=(20, 0))

        def parametro_min(mit_check1,index, index_var):
            msg = "O arquivo deve conter obrigatoriamente\na terceira coluna indicando os dias dos dados coletados."
            V3 = tk.Checkbutton(self.parametros_labelframe, text="Minuto (1-1439)", variable=mit_check1, onvalue=1,offvalue=0, bg="white")
            B3 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C3 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V3.grid(row=2, column=2, sticky=tk.W, pady=2, padx=(1, 0))
            B3.grid(row=2, column=1, sticky=tk.W, pady=2, padx=0)
            C3.grid(row=2, column=0, padx=(20, 0))

        def parametro_glo(glo_check1,index, index_var):
            msg = 'Radiações Global, Direta, Difusa são medida em W/m²'
            V4 = tk.Checkbutton(self.parametros_labelframe, text="Radiação Global (W/m²)", variable=glo_check1, onvalue=True,offvalue=False, bg="white")
            B4 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C4 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V4.grid(row=3, column=2, sticky=tk.W, pady=2, padx=(1, 0))
            B4.grid(row=3, column=1, sticky=tk.W, pady=2, padx=0)
            C4.grid(row=3, column=0, padx=(20, 0))

        def parametro_dni(dni_check1,index, index_var):
            msg = 'Radiações Global, Direta, Difusa são medida em W/m²'
            V5 = tk.Checkbutton(self.parametros_labelframe, text="Radiação Direta (W/m²)", variable=dni_check1, onvalue=True,offvalue=False, bg="white")
            B5 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C5 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)

            V5.grid(row=0, column=5, sticky=tk.W, pady=2, padx=(5, 0))
            B5.grid(row=0, column=4, sticky=tk.W, pady=2, padx=0)
            C5.grid(row=0, column=3, padx=(20, 0))


        def parametro_dif(dif_check1,index, index_var):
            msg = 'Radiações Global, Direta, Difusa são medida em W/m²'
            V6 = tk.Checkbutton(self.parametros_labelframe, text="Radiação Difusa (W/m²)", variable=dif_check1, onvalue=True,offvalue=False, bg="white")
            B6 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C6 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V6.grid(row=1, column=5, sticky=tk.W, pady=2, padx=(5, 0))
            B6.grid(row=1, column=4, sticky=tk.W, pady=2, padx=0)
            C6.grid(row=1, column=3, padx=(20, 0))

        def parametro_lw(lw_check1, index, index_var):
            msg = 'Radiações de Onda Longa é medida em W/m².\nNecessário saber Temperatura do ar.'
            V7 = tk.Checkbutton(self.parametros_labelframe, text="Radiação de Onda Longa (W/m²)", variable=lw_check1, onvalue=True,offvalue=False,
                                bg="white")
            B7 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C7 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V7.grid(row=2, column=5, sticky=tk.W, pady=2, padx=(5, 0))
            B7.grid(row=2, column=4, sticky=tk.W, pady=2, padx=0)
            C7.grid(row=2, column=3, padx=(20, 0))

        def parametro_par(par_check1: object, index: object, index_var) -> object:
            msg = 'Radiações PAR é medida em W/m²'
            V8 = tk.Checkbutton(self.parametros_labelframe, text="Radiação PAR (W/m²)", variable=par_check1,onvalue=True,offvalue=False, bg="white")
            B8 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C8 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V8.grid(row=3, column=5, sticky=tk.W, pady=2, padx=(5, 0))
            B8.grid(row=3, column=4, sticky=tk.W, pady=2, padx=0)
            C8.grid(row=3, column=3, padx=(20, 0))


        def parametro_lux(lux_check1, index, index_var):
            msg = 'Iluminância é o fluxo luminoso que incide sobre uma\n superfície situada a uma certa distância da fonte.\nMedida em W/m².'
            V9 = tk.Checkbutton(self.parametros_labelframe, text="Iluminância (W/m²)", variable=lux_check1,onvalue=True,offvalue=False, bg="white")
            B9 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C9 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V9.grid(row=0, column=8, sticky=tk.W, pady=2, padx=(5, 0))
            B9.grid(row=0, column=7, sticky=tk.W, pady=2, padx=0)
            C9.grid(row=0, column=6, padx=(20, 0))

        def parametro_tp(tp_check1: object, index: object, index_var) -> object:
            msg = ' '
            V10 = tk.Checkbutton(self.parametros_labelframe, text="Temperatura(°C)", variable=tp_check1, onvalue=True,offvalue=False,bg="white")
            B10 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C10 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V10.grid(row=1, column=8, sticky=tk.W, pady=2, padx=(5, 0))
            B10.grid(row=1, column=7, sticky=tk.W, pady=2, padx=0)
            C10.grid(row=1, column=6, padx=(20, 0))

        def parametro_umi(umi_check1, index, index_var):
            msg = ' '
            V11 = tk.Checkbutton(self.parametros_labelframe, text="Umidade (%)", variable=umi_check1,onvalue=True,offvalue=False, bg="white")
            B11 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C11 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V11.grid(row=2, column=8, sticky=tk.W, pady=2, padx=(5, 0))
            B11.grid(row=2, column=7, sticky=tk.W, pady=2, padx=0)
            C11.grid(row=2, column=6, padx=(20, 0))

        def parametro_press(press_check1, index, index_var):
            msg = ' '
            V12 = tk.Checkbutton(self.parametros_labelframe, text="Pressão (hPa ou mbar)", variable=press_check1, onvalue=True,offvalue=False,bg="white")
            B12 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C12 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V12.grid(row=3, column=8, sticky=tk.W, pady=2, padx=(5, 0))
            B12.grid(row=3, column=7, sticky=tk.W, pady=2, padx=0)
            C12.grid(row=3, column=6, padx=(20, 0))

        def parametro_rain(rain_check1, index, index_var):
            msg = ' '
            V13 = tk.Checkbutton(self.parametros_labelframe, text="Precipitação da Chuva (mm)", variable=rain_check1,onvalue=True,offvalue=False,bg="white")
            B13 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C13 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V13.grid(row=0, column=11, sticky=tk.W, pady=2, padx=(5, 0))
            B13.grid(row=0, column=10, sticky=tk.W, pady=2, padx=0)
            C13.grid(row=0, column=9, padx=(20, 0))

        def parametro_wspe(wspe_check1, index, index_var):
            msg = ' '
            V14 = tk.Checkbutton(self.parametros_labelframe, text="Velocidade do Vento (m/s)", variable=wspe_check1,onvalue=True,offvalue=False,
                                 bg="white")
            B14 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C14 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V14.grid(row=1, column=11, sticky=tk.W, pady=2, padx=(5, 0))
            B14.grid(row=1, column=10, sticky=tk.W, pady=2, padx=0)
            C14.grid(row=1, column=9, padx=(20, 0))

        def parametro_wdr(wdr_check1, index, index_var):
            msg = ' '
            V15 = tk.Checkbutton(self.parametros_labelframe, text="Direção do Vento (graus)", variable=wdr_check1,onvalue=True,offvalue=False, bg="white")
            B15 = tk.Button(self.parametros_labelframe, text="(?)", relief="flat", bg="white", fg="blue", command=lambda: pop(msg))
            C15 = ttk.Combobox(self.parametros_labelframe, textvariable=index_var, values=index, width=3)
            V15.grid(row=2, column=11, sticky=tk.W, pady=2, padx=(5, 0))
            B15.grid(row=2, column=10, sticky=tk.W, pady=2, padx=0)
            C15.grid(row=2, column=9, padx=(20, 0))

        def qualificar():
            glo_check = glo_check1.get()
            dni_check = dni_check1.get()
            dif_check = dif_check1.get()
            lw_check = lw_check1.get()
            par_check = par_check1.get()
            lux_check = lux_check1.get()
            tp_check = tp_check1.get()
            umi_check = umi_check1.get()
            press_check = press_check1.get()
            rain_check = rain_check1.get()
            wspe_check = wspe_check1.get()
            wdr_check = wdr_check1.get()



        def botoes_parametros():
            self.butao_para = tk.Button(self.parametros_labelframe, text="Gerar Qualificação",
                                        bg="#66cccc", width=20, command=qualificar)
            self.butao_para.grid(row=4, column=10,columnspan=2, ipady=5, pady=(0,5))
        def botoes_parametro1():
            self.butao_para_2 = tk.Button(self.parametros_labelframe, text="Voltar", command=voltar2, bg="#66cccc",
                                          width=20)
            self.butao_para_2.grid(row=4, column=12, columnspan=2,ipady=5, pady=(0,5))
        def botoes_parametro2():
            self.butao_para_2 = tk.Button(self.parametros_labelframe, text="Voltar", command=voltar3, bg="#66cccc",
                                          width=20)
            self.butao_para_2.grid(row=4, column=12, ipady=5, pady=(0, 5))




if __name__=='__main__':
    root = tk.Tk()
    app = LaicaApp(root)
    app.mainloop()