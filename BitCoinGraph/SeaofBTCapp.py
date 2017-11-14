#!


import tkinter as tk        #
from tkinter import ttk     # ttk is the css of python

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation    # it for the animation
from matplotlib import style                # style for the graph
from matplotlib import pyplot as plt

import urllib
import json

import pandas as pd         # this is for data maanipulation

import numpy as np

matplotlib.use("TKAgg")     # it's the back-end

# font
LARGE_FONT = ("VERDANA", 12)
NORM_FONT = ("VERDANA", 10)
SMALL = ("VERDANA", 8)


style.use("ggplot")             # it is the style for the graph

# f = Figure(figsize=(7, 6), dpi=100) # it determine the size of the fraph

f = Figure()
a = f.add_subplot(111)

exchange = "BTC-e"
DatCounter = 9000
programName = "btce"


def popupmsg(msg):
    popup = tk.Tk()

    popup.wm_title("!")
    label= ttk.Label(popup, text=msg, font = NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 =  ttk.Button(popup, text="Okay", command = popup.destroy())
    B1.pack()
    popup.mainloop()


def changeExchange(toWhat, pn):
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName = pn
    DatCounter = 9000



def animate (i):
    dataLink = "https://api.bitfinex.com/v1/trades/BTCUSD?limit_trades=2000"
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode("utf-8")
    data = json.loads(data)   # data = data["btc_usd"] is useless for us

    data = pd.DataFrame(data)

    buys = data[(data["type"] == "buy")]  # changed to match the api response bid is now buy

    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
    buyDates = (buys["datestamp"]).tolist()

    sells = data[(data["type"] == "sell")]  # changed to match the api response ask is now sell

    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    sellDates = (sells["datestamp"]).tolist()

    a.clear()

    a.plot_date(buyDates, buys["price"], "#00A3E0", label="buys") # for color you can use r for red g for green or xadecimal
    a.plot_date(sellDates, sells["price"], "#183A54", label="sells")

    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    title = "BTC-e BTCUSD Prices\nLast Price:" + str(data["price"][99])
    a.set_title(title)



    '''pullDate = open("sampleData.txt", "r").read()
    dataList = pullDate.split()
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            try:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))
            except ValueError:
                print('Ignoring: malformed line: "{}"'.format(x,y))
    a.clear()

    a.plot(xList, yList)
'''




class SeaofBTCapp(tk.Tk):

    # constructor
    # args pass number
    # kwargs passes words (dictionary)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Right upper corner icon
        tk.Tk.iconbitmap(self, default="Untitled.ico")
        tk.Tk.wm_title(self,"Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # menu bar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label = "Save Settings", command = lambda: popupmsg("Not set up yet"))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)

        # add exchange to the menue bar
        exchangeChoice.add_command(label="BTC-e", command=lambda: changeExchange("BTC-e","btce"))
        exchangeChoice.add_command(label="BItfinex", command=lambda: changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="Bitstamp", command=lambda: changeExchange("Bitstamp","bitstamp"))
        exchangeChoice.add_command(label="Houbi", command=lambda: changeExchange("Houbi","houbi"))

        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick", command = lambda: changeTimeFrame("tick"))
        dataTF.add_command(label="1 Day", command = lambda: changeTimeFrame("1d"))
        dataTF.add_command(label="3 Day", command = lambda: changeTimeFrame("3d"))
        dataTF.add_command(label="1 Week", command = lambda: changeTimeFrame("7d"))


        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        # if you want to add more pages
        for F in (StartPage, PageOne, PTCe_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""ALPHA Bitcoin trading Application use
            use at your own risk. There is no promise
            of warranty."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                           command=lambda: controller.show_frame(PTCe_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Dessagree",
                             command=quit)
        button2.pack()
        '''
        button2 = ttk.Button(self, text="Visit page 2",
                          command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                          command=lambda: controller.show_frame(PageThree))
        button3.pack()
        '''

class PageOne(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

'''
class PageTwo(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page onw",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
'''


class PTCe_Page(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        # bring the canvas
        canvas =FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # navigation bar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
app.geometry("1280x720")    # resolution of the graph
ani = animation.FuncAnimation(f, animate, interval=2000)
app.mainloop()












