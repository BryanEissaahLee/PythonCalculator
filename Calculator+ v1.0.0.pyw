import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import math
import os

root = tb.Window(themename="cyborg")
root.geometry("300x350")
root.title("")

#creates the results tab where calculations and button inputs go
resultTab = tb.Entry(root, state="readonly", font=("Segoe UI", 16), justify="right", bootstyle=INFO)
resultTab.grid(row=1, column=0, columnspan=4, sticky="ew", padx=5, pady=10)

#command for button inputs
def inputSymbol(num):
    resultTab.config(state="normal")
    resultTab.insert(tb.END, str(num))
    resultTab.config(state="readonly")

#command for button clear results tab field
def clearTab():
    resultTab.config(state="normal")
    resultTab.delete(0, tb.END)
    resultTab.config(state="readonly")

#this is the command for the operator buttons
def operatorInput(symbol, operator):
    resultTab.config(state="normal")
    resultTab.insert(tb.END, symbol)
    expression.append(operator)
    resultTab.config(state="readonly")

#calculate command
def calcul8():
    calculation = resultTab.get()
    resultTab.config(state="normal")
    try:
        result = eval(calculation)
        resultTab.delete(0, tb.END)
        resultTab.insert(0, str(result))
        resultTab.config(state="readonly")
    except Exception:
        resultTab.delete(0, tb.END)
        resultTab.insert(0, "Error")
        resultTab.config(state="readonly")

#backspace command
def backSpace():
    resultTab.config(state="normal")
    resultTab.delete(len(resultTab.get())-1, tb.END)
    resultTab.config(state="readonly")

#inserts peroid for decimal float values
def periDeci():
    resultTab.config(state="normal")
    resultTab.insert(tb.END, ".")
    resultTab.config(state="readonly")

#below are fun features for Windows PCs

#adds funny message to home screen :D
desktopPath = os.path.join(os.path.expanduser("~"), "Desktop") #gets the users home directory, adds Desktop to file path
filePath = os.path.join(desktopPath, "viruspackage.txt")         #creates txt file to send to desktop
txtFileDelivery = f'powershell -Command "Set-Content -Path \'{filePath}\' -Value \'yeah buddy youre done for\'"' #data in file

#these here have the system speech funny lines
speakerOne = f'powershell -Command "Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'I know what you are.\')"'
speakerTwo = f'powershell -Command "Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'Its time to blaze it\')"'

def helloThere():
    messagebox.showinfo("Hello!")

def checkResultTab():
    checkCode = resultTab.get()
    if os.name == "nt" and checkCode == "6969":
        os.system(txtFileDelivery)
    elif os.name == "nt" and checkCode == "80085":
        os.system(speakerOne)
    elif os.name == "nt" and checkCode == "420":
        os.system(speakerTwo)

#sets a field for operators, so teh calculations can be performed
expression = []

#Button setup helper function
def addButton(text, row, col, cmd, bootstyle=SECONDARY, padx=3, pady=3):
    btn = tb.Button(root, text=text, command=cmd, width=6, bootstyle=bootstyle)
    btn.grid(row=row, column=col, padx=padx, pady=pady, sticky="nsew")
    return btn

#adds a custome label
titleLabel = tb.Label(root, text="⚡ CΛLCULΛTOR ⚡",
                      font=("Comic Sans MS", 20, "bold"), foreground="#FF00FF",
                      background="#222222")
titleLabel.grid(row=0, column=0, columnspan=4, pady=(10, 0), sticky="ew")

#adds first row of buttons
addButton("DEL", 2, 0, backSpace, bootstyle=WARNING)
addButton("CLR", 2, 1, clearTab, bootstyle=DANGER)
addButton(":D", 2, 2, helloThere, bootstyle=INFO)
addButton("/", 2, 3, lambda: operatorInput("/", "/"), bootstyle=PRIMARY)

#adds second row of buttons
addButton("7", 3, 0, lambda: inputSymbol(7), bootstyle=LIGHT)
addButton("8", 3, 1, lambda: inputSymbol(8), bootstyle=LIGHT)
addButton("9", 3, 2, lambda: inputSymbol(9), bootstyle=LIGHT)
addButton("*", 3, 3, lambda: operatorInput("*", "*"), bootstyle=PRIMARY)

#adds third row of buttons
addButton("4", 4, 0, lambda: inputSymbol(4), bootstyle=LIGHT)
addButton("5", 4, 1, lambda: inputSymbol(5), bootstyle=LIGHT)
addButton("6", 4, 2, lambda: inputSymbol(6), bootstyle=LIGHT)
addButton("-", 4, 3, lambda: operatorInput("-", "-"), bootstyle=PRIMARY)

#adds fourth row of buttons
addButton("1", 5, 0, lambda: inputSymbol(1), bootstyle=LIGHT)
addButton("2", 5, 1, lambda: inputSymbol(2), bootstyle=LIGHT)
addButton("3", 5, 2, lambda: inputSymbol(3), bootstyle=LIGHT)
addButton("+", 5, 3, lambda: operatorInput("+", "+"), bootstyle=PRIMARY)

#adds fifth row of buttons
addButton("?", 6, 0, checkResultTab, bootstyle=INFO)
addButton("0", 6, 1, lambda: inputSymbol(0), bootstyle=LIGHT)
addButton(".", 6, 2, periDeci, bootstyle=LIGHT)
addButton("=", 6, 3, calcul8, bootstyle=SUCCESS)

#allows grid cells to expand
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
