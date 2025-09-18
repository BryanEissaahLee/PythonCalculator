import tkinter as tk
from tkinter import messagebox
import math
import os

root = tk.Tk()
root.geometry("250x250")
root.title("CALCULATOR")

#creates the results tab where calculations and button inputs go
resultTab = tk.Entry(root, state="readonly")
resultTab.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

#command for button inputs
def inputSymbol(num):
    resultTab.config(state="normal")
    resultTab.insert(tk.END, str(num))
    resultTab.config(state="readonly")

#command for button clear results tab field
def clearTab():
    resultTab.config(state="normal")
    resultTab.delete(0, tk.END)
    resultTab.config(state="readonly")

#this is the command for the operator buttons
def operatorInput(symbol, operator):
    resultTab.config(state="normal")
    resultTab.insert(tk.END, symbol)
    expression.append(operator)
    resultTab.config(state="readonly")

#calculate command
def calcul8():
    calculation = resultTab.get()
    resultTab.config(state="normal")
    try:
        result = eval(calculation)
        resultTab.delete(0, tk.END)
        resultTab.insert(0, str(result))
        resultTab.config(state="readonly")
    except Exception:
        resultTab.delete(0, tk.END)
        resultTab.insert(0, "Error")
        resultTab.config(state="readonly")

#backspace command
def backSpace():
    resultTab.config(state="normal")
    resultTab.delete(len(resultTab.get())-1, tk.END)
    resultTab.config(state="readonly")

#inserts peroid for decimal float values
def periDeci():
    resultTab.config(state="normal")
    resultTab.insert(tk.END, ".")
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


#these are bits specific to the basic calcul8tr
#first row of buttons
buttonDel = tk.Button(root, text = "DEL", width=3, height=1, fg="white", bg="black",
                      command=lambda: backSpace())
buttonDel.grid(row=1, column=0, padx=1, pady=0)
buttonClr = tk.Button(root, text = "CLR", width=3, height=1, fg="white", bg="black",
                      command=clearTab)
buttonClr.grid(row=1, column=1, padx=1, pady=1)
buttonSmile = tk.Button(root, text = ":D", width=3, height=1, fg="white", bg="black",
                        command=lambda: helloThere())
buttonSmile.grid(row=1, column=2, padx=1, pady=1)
buttonDiv = tk.Button(root, text = "/", width=3, height=1, fg="white", bg="black",
                      command=lambda: operatorInput("/", "/"))
buttonDiv.grid(row=1, column=3, padx=1, pady=1)

#second row of buttons
button7 = tk.Button(root, text="7", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(7))
button7.grid(row=2, column=0, padx=1, pady=5)
button8 = tk.Button(root, text="8", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(8))
button8.grid(row=2, column=1, padx=1, pady=1)
button9 = tk.Button(root, text="9", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(9))
button9.grid(row=2, column=2, padx=1, pady=1)
buttonX = tk.Button(root, text="*", width=3, height=1, fg="white", bg="black",
                    command=lambda: operatorInput("*", "*"))
buttonX.grid(row=2, column=3, padx=1, pady=1)

#third row of buttons
button4 = tk.Button(root, text="4", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(4))
button4.grid(row=3, column=0, padx=1, pady=1)
button5 = tk.Button(root, text="5", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(5))
button5.grid(row=3, column=1, padx=1, pady=1)
button6 = tk.Button(root, text="6", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(6))
button6.grid(row=3, column=2, padx=1, pady=1)
buttonMin = tk.Button(root, text="-", width=3, height=1, fg="white", bg="black",
                      command=lambda: operatorInput("-", "-"))
buttonMin.grid(row=3, column=3, padx=1, pady=1)

#fourth row of buttons
button1 = tk.Button(root, text="1", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(1))
button1.grid(row=4, column=0, padx=1, pady=5)
button2 = tk.Button(root, text="2", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(2))
button2.grid(row=4, column=1, padx=1, pady=1)
button3 = tk.Button(root, text="3", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(3))
button3.grid(row=4, column=2, padx=1, pady=1)
buttonPlu = tk.Button(root, text="+", width=3, height=1, fg="white", bg="black",
                      command=lambda: operatorInput("+", "+"))
buttonPlu.grid(row=4, column=3, padx=1, pady=1)

#fifth row of buttons
buttonQue = tk.Button(root, text="?", width=3, height=1, fg="white", bg="black",
                      command=lambda: checkResultTab())
buttonQue.grid(row=5, column=0, padx=1, pady=1)
button0 = tk.Button(root, text="0", width=3, height=1, fg="white", bg="black",
                    command=lambda: inputSymbol(0))
button0.grid(row=5, column=1, padx=1, pady=1)
buttonPeri = tk.Button(root, text=".", width=3, height=1, fg="white", bg="black",
                       command=lambda: periDeci())
buttonPeri.grid(row=5, column=2, padx=1, pady=1)
buttonEqu = tk.Button(root, text="=", width=3, height=1, fg="white", bg="black",
                      command=lambda: calcul8())
buttonEqu.grid(row=5, column=3, padx=1, pady=1)

#sets a field for operators, so it can do the math
expression = []

#keeps the calc window open
root.mainloop()
