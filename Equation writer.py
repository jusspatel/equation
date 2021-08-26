from tkinter import*
import tkinter.font as font
import tkinter.scrolledtext as ScrolledText


root = Tk()

root.title("Calculator")
root.configure(bg="black")
MyFont=font.Font(size=15)

sText = ScrolledText.ScrolledText(root, height=7,borderwidth=10,font=MyFont)

sText.grid(row=0,columnspan=12,column=0)

    
 

def button_add(number):

    
    current=sText.get(10.0,END)
    sText.delete(10.0,END)
    sText.insert(10.0,str(current)+str(number),END)

lab=Label(root, text="",width=40,bg="black",fg="black").grid(row=2,columnspan=3,column=0)
lab2=Label(root, text="",width=40,bg="black",fg="black").grid(row=2,columnspan=7,column=3)
frame = Frame()  
frame.grid(row=3,column=2)



MyFont=font.Font(size=13)

button1=Button(root,text="1",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(1)).grid(row=3,column=0)
button2=Button(root,text="2",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(2)).grid(row=3,column=1)
button3=Button(root,text="3",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(3)).grid(row=3,column=2)
button4=Button(root,text="4",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(4)).grid(row=4,column=0)
button5=Button(root,text="5",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(5)).grid(row=4,column=1)
button6=Button(root,text="6",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(6)).grid(row=4,column=2)
button7=Button(root,text="7",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(7)).grid(row=5,column=0)
button8=Button(root,text="8",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(8)).grid(row=5,column=1)
button9=Button(root,text="9",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(9)).grid(row=5,column=2)
button0=Button(root,text="0",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(0)).grid(row=6,column=1)
buttonpi=Button(root,text="π",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add("π")).grid(row=6,column=0)
buttonpi2=Button(root,text=".",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",font=MyFont,command=lambda:button_add(".")).grid(row=6,column=2)


lab02=Label(root,text="",height=40).grid(row=3,column=3,rowspan=9)


buttonroot=Button(root,text="√x",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("√")).grid(row=3,column=4)
buttonroot1=Button(root,text="∛x",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("∛")).grid(row=3,column=5)
buttonroot2=Button(root,text="∜x",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("∜")).grid(row=3,column=6)
buttonroot3=Button(root,text="+",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("+")).grid(row=4,column=4)
buttonroot4=Button(root,text="÷",borderwidth=5,padx=55,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("÷")).grid(row=4,column=5)
buttonroot5=Button(root,text="-",borderwidth=5,padx=55,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("-")).grid(row=4,column=6)
buttonroot6=Button(root,text="x",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("x")).grid(row=6,column=4)
buttonroot7=Button(root,text="y",borderwidth=5,padx=53,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("y")).grid(row=6,column=5)
buttonroot8=Button(root,text="z",borderwidth=5,padx=53,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("z")).grid(row=6,column=6)
buttonroot9=Button(root,text="×",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("×")).grid(row=5,column=4)
buttonroot10=Button(root,text="press this as many times to create \n a line for fraction",borderwidth=5,padx=30,pady=17,bg="red",fg="White",command=lambda:button_add("⎼")).grid(row=5,column=5,columnspan=2)
buttonroot11=Button(root,text="x²",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("²")).grid(row=4,column=7)
buttonroot12=Button(root,text="x³",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("³")).grid(row=5,column=7)
buttonroot13=Button(root,text="x⁴",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("⁴")).grid(row=6,column=7)
buttonroot14=Button(root,text="x⁰",borderwidth=5,padx=50,pady=20,bg="red",fg="White",font=MyFont,command=lambda:button_add("⁰")).grid(row=3,column=7)
buttonroot15=Button(root,text="=",borderwidth=5,padx=40,pady=20,bg="black",fg="White",font=MyFont,command=lambda:button_add("=")).grid(row=7,column=1)
buttonroot16=Button(root,text="( ",borderwidth=5,padx=45,pady=20,bg="blue",fg="White",font=MyFont,command=lambda:button_add("(")).grid(row=9,column=0)
buttonroot17=Button(root,text=") ",borderwidth=5,padx=45,pady=20,bg="blue",fg="White",font=MyFont,command=lambda:button_add(")")).grid(row=9,column=1)

buttonroot18=Button(root,text="Spacebar ",borderwidth=5,padx=180,pady=20,bg="Red",fg="White",font=MyFont,command=lambda:button_add(" ")).grid(row=7,column=4,columnspan=4)
buttonroot19=Button(root,text="∫",borderwidth=5,padx=40,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("∫")).grid(row=3,column=9)
lab22=Label(root,text="",height=40).grid(row=3,column=8,rowspan=9)

buttonroot20=Button(root,text="d/dx",borderwidth=5,padx=40,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("d/dx")).grid(row=3,column=10)
buttonroot21=Button(root,text="∑",borderwidth=5,padx=40,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("∑")).grid(row=3,column=11)
buttonroot22=Button(root,text="∞",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("∞")).grid(row=4,column=9)
buttonroot23=Button(root,text="-∞",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("-∞")).grid(row=4,column=10)
buttonroot24=Button(root,text="∈",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("∈")).grid(row=4,column=11)
buttonroot25=Button(root,text="⋃",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("⋃")).grid(row=5,column=9)
buttonroot26=Button(root,text="⋂",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("⋂")).grid(row=5,column=10)
buttonroot27=Button(root,text="f(x)",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("f()")).grid(row=5,column=11)
buttonroot28=Button(root,text=">",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add(">")).grid(row=6,column=9)
buttonroot29=Button(root,text="<",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("<")).grid(row=6,column=10)
buttonroot30=Button(root,text="≤",borderwidth=5,padx=48,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("≤")).grid(row=6,column=11)
buttonroot31=Button(root,text="≥",borderwidth=5,padx=48,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("≥")).grid(row=7,column=9)
buttonroot32=Button(root,text="≠",borderwidth=5,padx=48,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("≠")).grid(row=7,column=10)
buttonroot32=Button(root,text="≈",borderwidth=5,padx=45,pady=20,bg="green",fg="White",font=MyFont,command=lambda:button_add("≈")).grid(row=7,column=11)

lab23=Label(root,text=" ",width=150).grid(row=8,column=0,columnspan=12)

buttonroot33=Button(root,text="{ ",borderwidth=5,padx=45,pady=20,bg="blue",fg="White",font=MyFont,command=lambda:button_add("{")).grid(row=9,column=2)
buttonroot34=Button(root,text="} ",borderwidth=5,padx=45,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("}")).grid(row=10,column=0)
buttonroot35=Button(root,text="[ ",borderwidth=5,padx=45,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("[")).grid(row=10,column=1)
buttonroot36=Button(root,text="] ",borderwidth=5,padx=45,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("]")).grid(row=10,column=2)
buttonroot37=Button(root,text="∴",borderwidth=5,padx=45,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("∴")).grid(row=11,column=0)
buttonroot38=Button(root,text="|x|",borderwidth=5,padx=40,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("|x|")).grid(row=11,column=1)
buttonroot39=Button(root,text="∵",borderwidth=5,padx=40,pady=20,bg="Blue",fg="White",font=MyFont,command=lambda:button_add("∵")).grid(row=11,column=2)

buttonroot40=Button(root,text="sin",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("sin")).grid(row=9,column=9)
buttonroot41=Button(root,text="cos",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("cos")).grid(row=9,column=10)
buttonroot42=Button(root,text="tan",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("tan")).grid(row=9,column=11)
buttonroot43=Button(root,text="csc",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("cosec")).grid(row=10,column=9)
buttonroot44=Button(root,text="sec",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("sec")).grid(row=10,column=10)
buttonroot45=Button(root,text="cot",borderwidth=5,padx=40,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("cot")).grid(row=10,column=11)
buttonroot46=Button(root,text="θ",borderwidth=5,padx=45,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("θ")).grid(row=11,column=9)
buttonroot47=Button(root,text="β",borderwidth=5,padx=45,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("β")).grid(row=11,column=10)
buttonroot48=Button(root,text="α",borderwidth=5,padx=45,pady=20,bg="Orange",fg="White",font=MyFont,command=lambda:button_add("α")).grid(row=11,column=11)







root.mainloop()
