import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import messagebox as msgb



def startAp(ap="wifidude",paspharse="12345678",ipaddress="192.168.1.1",nbusers=16):
    # testing the values
    defaultConfig=["wifidude","12345678","192.168.1.1",16]
    return "wifiAP"

class FirstprojectApp:
    def __init__(self, master=None):
        # build ui
        master=tk.Tk()
        master.title('wifiHotSpot')
        master.resizable(0, 0)
        # toplevel_6 = tk.Toplevel(master)
        frame_4 = ttk.Frame(master)

        createAP = ttk.Button(frame_4)
        createAP.config(default='normal', state='normal', takefocus=True, text='createAP',command=self.__createAccessPoint__)
        createAP.place(relx='0.86', rely='0.6', x='0', y='0')

        killAP = ttk.Button(frame_4)
        killAP.config(compound='top', cursor='arrow', text='killAP',command=self.__killAP__)
        killAP.place(relx='0.86', rely='0.79', x='0', y='0')

        config = ttk.Labelframe(frame_4)
        hotspotname = ttk.Label(config)
        hotspotname.config(anchor='w', cursor='arrow', takefocus=False, text='AP_Name:')
        hotspotname.place(anchor='nw', relx='0.0', rely='0.05', x='0', y='0')
        hotspotpassword = ttk.Label(config)
        hotspotpassword.config(text='Password:')
        hotspotpassword.place(anchor='nw', relx='0.0', rely='0.20', x='0', y='0')
        hotspot_ress = ttk.Label(config)
        hotspot_ress.config(text='Ip@:')
        hotspot_ress.place(anchor='nw', relx='0.0', rely='0.35', x='0', y='0')
        NumberUsers = ttk.Label(config)
        NumberUsers.config(text='Num°Users:')
        NumberUsers.place(anchor='nw', relx='0.', rely='0.50', x='0', y='0')

        self.AP = ttk.Entry(config)
        _text_ = '''AP_Name'''
        self.AP.delete('0', 'end')
        self.AP.insert('0', _text_)
        self.AP.place(anchor='nw', relx='0.5', rely='0.05', x='0', y='0')

        self.Pass = ttk.Entry(config)
        _text_ = '''Password'''
        self.Pass.delete('0', 'end')
        self.Pass.insert('0', _text_)
        self.Pass.place(anchor='nw', relx='0.5', rely='0.20', x='0', y='0')

        self.IpRange = ttk.Entry(config)
        _text_ = '''Ip address'''
        self.IpRange.delete('0', 'end')
        self.IpRange.insert('0', _text_)
        self.IpRange.place(anchor='nw', relx='0.5', rely='0.35', x='0', y='0')

        self.NbrUsers = ttk.Entry(config)
        _text_ = '''Num users'''
        self.NbrUsers.delete('0', 'end')
        self.NbrUsers.insert('0', _text_)
        self.NbrUsers.place(anchor='nw', relx='0.5', rely='0.50', x='0', y='0')

        config.config(cursor='arrow', height='200', text='Config', width='200')
        config.place(relheight='0.4', relwidth='0.50', relx='0.0', rely='0.14', x='0', y='0')

        QrCode = ttk.Labelframe(frame_4)
        # qrBtnimg = ttk.Button(QrCode)


        # width = 100
        # height = 550
        lImag = Image.open("qr.png")
        w,h = lImag.size
        lImag = lImag.resize((w//2,h), Image.ANTIALIAS)
        self.img_qr =  ImageTk.PhotoImage(lImag)

        # self.img_qr = tk.PhotoImage(file='qr.png')





        # canvas = Canvas(QrCode, width = 300, height = 100)
        # canvas.pack()
        # canvas.create_image(80, 80, anchor='nw', image=self.img_qr)

        # qrBtnimg.config(compound='top', default='disabled', image=self.img_qr, takefocus=True)
        # qrBtnimg.place(anchor='nw', relheight='1.0', relwidth='1.0', relx='0.0', x='0', y='0')


        # canvas.config(height='200', width='200')
        # canvas.place(anchor='nw', relheight='0.4', relwidth='0.0', relx='0.0', rely='0.0', x='0', y='0')
        # canvas.place(bordermode='inside',relx='0.1', rely='0.2', x='0', y='0')


        canvas = Canvas(QrCode,bg="red")
        canvas.create_image(0, 0, image=self.img_qr)
        canvas.config(relief='ridge')
        canvas.place(anchor='nw',bordermode='inside', height='0', relheight='1.0', relwidth='1.0', relx='0.0', rely='0.0', width='0', x='0', y='0')




        QrCode.config(height='200', text='QrCode', width='200')
        QrCode.place(anchor='nw', relheight='0.4', relwidth='0.49', relx='0.5', rely='0.14', x='0', y='0')

        LogDisplay = ttk.Labelframe(frame_4)
        treeview_2 = ttk.Treeview(LogDisplay)
        treeview_2.place(bordermode='inside', relheight='0.91', relwidth='0.9', rely='0.0', x='0', y='0')
        scrollbar_2 = ttk.Scrollbar(LogDisplay)
        scrollbar_2.config(orient='vertical')
        scrollbar_2.place(anchor='nw', relheight='1.0', relwidth='0.07', relx='0.83', rely='0.0', x='0', y='0')
        LogDisplay.config(height='200', relief='sunken', text='LogDisplay', width='200')
        LogDisplay.place(anchor='nw', relwidth='0.56', relx='0.0', rely='0.54', x='0', y='0')
        # image = ttk.Button(frame_4)


        imglogo = Image.open("logo.png")
        # w,h = imglogo.size
        # imglogo = imglogo.resize((w,h), Image.ANTIALIAS)
        self.img_logo =  ImageTk.PhotoImage(imglogo)


        canvasTwo = Canvas(frame_4,bg="green")
        canvasTwo.create_image(0, 0,image=self.img_logo)
        # canvasTwo.config(relief='ridge')
        canvasTwo.place(anchor=NW,bordermode='inside', height='0', relheight='0.12', relwidth='0.5', relx='0.0', rely='0.0', width='0', x='0', y='0')

        # self.img_logo = tk.PhotoImage(file='logo.png')

        # image.config(image=self.img_logo, state='normal', takefocus=False)
        # image.place(anchor='nw', bordermode='inside', height='80', relheight='0.0', relwidth='0.33', relx='0.0', rely='0.0', width='100', x='0', y='0')

        frame_4.config(borderwidth='1', height='600', padding='0', relief='flat',takefocus=True, width='600')
        frame_4.pack(side='top')

        # frame_4.config()
        # toplevel_6.config(height='500', relief='flat', width='500')
        # toplevel_6.resizable(True, True)
        # toplevel_6.title('wifiHotSpot')


        # Main widget
        self.mainwindow = frame_4




    # stating the APP GUI
    def run(self):
        self.mainwindow.mainloop()
        msgb.showinfo("WELCOME","greeting ...")

    # CREATING THE ACCESSPOINT
    def  __createAccessPoint__(self):
        msgb.showinfo("nothing yet","starting ...")
        self.wifiAP=startAp(self.AP.get(),self.Pass.get(),self.IpRange.get(),self.NbrUsers.get())

    # STOPPING THE AP
    def  __killAP__(self):
        msgb.showinfo("nothing yet","deleting ... ")
        self.wifiAP.destroy()


    def leave(self):
        msgb.showinfo("bye","quittig ...")
        self.exit()


if __name__ == '__main__':
    app = FirstprojectApp()
    app.run()

