import tkinter as tk
import tkinter.ttk as ttk


class FirstprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel_6 = tk.Toplevel(master)
        frame_4 = ttk.Frame(toplevel_6)
        createAP = ttk.Button(frame_4)
        createAP.config(default='normal', state='normal', takefocus=True, text='createAP')
        createAP.place(relx='0.86', rely='0.6', x='0', y='0')
        killAP = ttk.Button(frame_4)
        killAP.config(compound='top', cursor='arrow', text='killAP')
        killAP.place(relx='0.86', rely='0.79', x='0', y='0')
        config = ttk.Labelframe(frame_4)
        hotspotname = ttk.Label(config)
        hotspotname.config(anchor='w', cursor='arrow', takefocus=False, text='AP_Name:')
        hotspotname.place(anchor='nw', relx='0.0', rely='0.05', x='0', y='0')
        hotspotpassword = ttk.Label(config)
        hotspotpassword.config(text='Password:')
        hotspotpassword.place(anchor='nw', relx='0.0', rely='0.20', x='0', y='0')
        hotspot@ress = ttk.Label(config)
        hotspot@ress.config(text='Ip@:')
        hotspot@ress.place(anchor='nw', relx='0.0', rely='0.35', x='0', y='0')
        NumberUsers = ttk.Label(config)
        NumberUsers.config(text='Num°Users:')
        NumberUsers.place(anchor='nw', relx='0.', rely='0.50', x='0', y='0')
        entry_1 = ttk.Entry(config)
        _text_ = '''AP_Name'''
        entry_1.delete('0', 'end')
        entry_1.insert('0', _text_)
        entry_1.place(anchor='nw', relx='0.5', rely='0.05', x='0', y='0')
        entry_2 = ttk.Entry(config)
        _text_ = '''Password'''
        entry_2.delete('0', 'end')
        entry_2.insert('0', _text_)
        entry_2.place(anchor='nw', relx='0.5', rely='0.20', x='0', y='0')
        entry_3 = ttk.Entry(config)
        _text_ = '''Ip address'''
        entry_3.delete('0', 'end')
        entry_3.insert('0', _text_)
        entry_3.place(anchor='nw', relx='0.5', rely='0.35', x='0', y='0')
        entry_4 = ttk.Entry(config)
        _text_ = '''Num users'''
        entry_4.delete('0', 'end')
        entry_4.insert('0', _text_)
        entry_4.place(anchor='nw', relx='0.5', rely='0.50', x='0', y='0')
        config.config(cursor='arrow', height='200', text='Config', width='200')
        config.place(relheight='0.4', relwidth='0.50', relx='0.0', rely='0.14', x='0', y='0')
        QrCode = ttk.Labelframe(frame_4)
        qr = ttk.Button(QrCode)
        self.img_qr = tk.PhotoImage(file='qr.png')
        qr.config(compound='top', default='disabled', image=self.img_qr, takefocus=True)
        qr.place(anchor='nw', relheight='1.0', relwidth='1.0', relx='0.0', x='0', y='0')
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
        image = ttk.Button(frame_4)
        self.img_logo = tk.PhotoImage(file='logo.png')
        image.config(image=self.img_logo, state='normal', takefocus=False)
        image.place(anchor='nw', bordermode='inside', height='80', relheight='0.0', relwidth='0.33', relx='0.0', rely='0.0', width='100', x='0', y='0')
        frame_4.config(borderwidth='1', height='600', padding='0', relief='flat')
        frame_4.config(takefocus=True, text='LogDisplay', width='600')
        frame_4.pack(side='top')
        toplevel_6.config(height='500', relief='flat', width='500')
        toplevel_6.resizable(True, True)
        toplevel_6.title('wifiHotSpot')

        # Main widget
        self.mainwindow = toplevel_6


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = FirstprojectApp()
    app.run()

