#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgb

import os
import sys
import subprocess

from tkinter import *
from tkinter.ttk import *




def script(ap="wifidude",paspharse="12345678",iprange="192.168.1.1",nbusers=16):
    cmd1_output = subprocess.check_output("netsh wlan show drivers", shell=True)
    if "Hosted network supported  : Yes" in str(cmd1_output):
        print("[+] Driver supported")
    hot_name = ap if len(ap)>3 else "wifidu0de"
    password = paspharse if len(paspharse)>8 else "12345678"
    while(len(password)<8):
        print("\n[-] Insufficient password strength. Try again ")
        password = input("Enter your password (include alphanumeric): ")
    cmd2 = "netsh wlan set hostednetwork mode=allow ssid="+hot_name+" key="+password
    cmd2_output = subprocess.check_output(cmd2, shell=True)
    if "successfully changed" in str(cmd2_output):
        print("[+] Hotspot created")
        cmd3_output = subprocess.check_output("netsh wlan start hostednetwork", shell=True)
        if "started" in str(cmd3_output):
            print("[+] The hotspot is up and running")
        else:
            print("[-] Oops, Something went wrong")
            exitting()
#       stat = "a"
#       while (stat != "q"):
        stat = input("\nPress any key to stop hotspot ")
        cmd4_output = subprocess.check_output("netsh wlan stop hostednetwork", shell=True)
        print("\n[+] Hotspot has been stopped")
        print("[+] Thanks for using")
        print("[+] For details contact @bnchandrapal")




































































class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Access Point Wifi")
        self.pack()

        self.create_widgets()

    def create_widgets(self):

        self.fontMsg = ttk.Label(text ='GeeksForGeeks', font = "50")
        self.fontMsg.pack(side="top")

        self.start = ttk.Button(self, text="startAP",command=self.createAP)
        self.stop = ttk.Button(self, text="StopAP",command=self.stopAP)

        # self.start["text"] = "startAP"
        # self.start["command"] = self.createAP
        self.start.pack(side="top")

        # self.stop["text"] = "StopAP"
        # self.stop["command"] = self.stopAP
        self.stop.pack(side="top")

        self.quit = ttk.Button(self, text="QUIT",command=self.leave)

        self.quit.pack(side="bottom")

        self.AP = ttk.Entry(self, width=25)
        # self.AP.insert(0, "APwifi")
        self.AP.pack()
        self.PassPhrase=ttk.Entry(self, width=25)
        self.PassPhrase.pack()
        # self.PassPhrase.insert(1, "12345678")

        self.button = ttk.Button(self, text="Visit Page 1")
        self.button.pack()


        self.dns=ttk.Entry(self, width=25)
        self.dns.pack()
        self.dhcp=ttk.Entry(self, width=25)
        self.dhcp.pack()

        self.lenpass = IntVar()
        self.userNbr=ttk.Combobox(self, width=2, textvariable = self.lenpass)
        self.userNbr.set('8')
        self.userNbr.configure(values = ('8','12','14','20','40'))
        self.userNbr.pack()






    def createAP(self):
        msgb.showinfo("nothing yet","starting ...")
        script(self.AP.get(),self.PassPhrase.get())
        print("hi there, everyone!")

    def stopAP(self):
        msgb.showinfo("nothing yet","deleting ... ")
        f=os.system("ping 127.0.0.1")
        print(f)


    def leave(self):
        msgb.showinfo("bye","quittig ...")
        sys.exit()





def exitting():
    msgb.showinfo("bye","you dont have admin privileges\nquittig ...")
    sys.exit()


# window = tk.Tk()
# window.title("Simple Text Editor")


def main():
    print ("[+] Checking for admin status")
    root = tk.Tk()
    root.geometry("400x450")
    app = Application(master=root)

    try:
        output = subprocess.check_output("whoami /groups | find \"S-1-16-12288\"", shell=True)
    except:
        print("[-] You are not admin :( ")
        exitting()

    if('S-1-16-12288' in str(output)):
        print("[+] The program is running with Admin priv :)")
        print("[+] Initiating the script")
        app.mainloop()
        # script()




if __name__ == '__main__':
    main()
