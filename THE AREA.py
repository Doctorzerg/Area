# this app is for calculate the area
import tkinter #TK
from tkinter import *
import math
gif = False
print("Area Application")
print("Welcome To my Application(Warning:[Units are in meters and square meters])")
x = input("please choose a shape(please type square or triangle or rectangle or circle or shpere or cube or oval or cone)\n[the PI number is 3]: ") # PI is 3.0
k = 'square','Square','cube','Cube','rectangle','Rectangle','Triangle','triangle','circle','Circle','oval','Oval','sphere','Sphere','cone','Cone'
while x not in k:
    print("your choose is not correct please try again")
    x = input("please choose a shape(please type square or triangle or rectangle or circle or cube or sphere or oval)\n[the PI number is 3]: ")
if x == "square" or x == "Square":
    y = input("from Side or Diagonal? ")
    k = "side","Side","Diagonal","diagonal"
    while y not in k:
        print("your choose is not correct please try again")
        y = input("from Side or Diagonal? ")
    if y == "Side" or y == "side":
        while not gif:
            try:
                side_square = float(input("please enter the side: "))
                gif = True
            except ValueError:
                print("it is not a number")
            else:
                root=tkinter.Tk()
                root.geometry("400x400")
                root.resizable(False,False)
                def clicked():
                    lbl.configure(text=f"The area is {side_square*side_square}\n(buttom exit to out)", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  side is {side_square}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="yes", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=140)    
                def clicked():
                    lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the side is {side_square}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="no", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=180)
                def Terminate():
                    root.destroy()
                btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                btn_2.place(height=50,width=300,x=50,y=220)
                root.mainloop()
    elif y == "diagonal" or y == "Diagonal":
        while not gif:
            try:
                diagonal_square = float(input("please enter the diagonal: "))
                gif = True
            except ValueError:
                print("it is not a number")
            else:
                root=tkinter.Tk()
                root.geometry("400x400")
                root.resizable(False,False)
                def clicked():
                    lbl.configure(text=f"The area is {0.5*(diagonal_square**2)} (buttom exit)", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  diagonal is {diagonal_square}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="yes", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=140)    
                def clicked():
                    lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  diagonal is {diagonal_square}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="no", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=180)
                def Terminate():
                    root.destroy()
                btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                btn_2.place(height=50,width=300,x=50,y=220)
                root.mainloop()        
elif x == "circle" or x == "Circle":
        c = input("from Diameter or Radius? ")
        k = "diameter","Diameter","radius","Radius"
        while c not in k:
            print("your choose is not correct please try again")
            c = input("from Diameter or Radius? ")
        if c == "Diameter" or c == "diameter":
            while not gif:
                try:
                    diameter = float(input("what is the daimeter: "))   
                    gif = True
                except ValueError:
                    print("it is not a number")
                else:         
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {((diameter/2)**2)*3} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Diameter is {diameter} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Diameter is {diameter} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
        elif c == "Radius" or c == "radius":
            while not gif:
                try:
                    radius = float(input("what is the Radius: "))
                    gif = True
                except ValueError:
                    print("it is not a number")
                else:
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {(radius**2)*3} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Radius is {radius} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Radius is {radius} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
elif x == "rectangle" or x == "Rectangle":
    while not gif:
        try:
            lenght = float(input("please enter the lenght: "))
        except ValueError:
            print("it is not a number")       
        else:
            while not gif:
                try:
                    width = float(input("please enter the width: "))
                except ValueError:
                    print("it is not a number")
                else:
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {width*lenght} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the lenght is {lenght} and width is {width}\nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the lenght is {lenght} and width is {width}\nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
elif x == "Triangle" or x == "triangle":
    while not gif:
        try:
            height = float(input("please enter the height: "))
        except ValueError:
            print("it is not a number")       
        else:
            while not gif:
                try:
                    base = float(input("please enter the base: "))
                except ValueError:
                    print("it is not a number")
                else:
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {(height*base)/2} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the height is {height} and base is {base}\nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the height is {height} and base is {base}\nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
elif x == "cube" or x == "Cube":
    y = input("from Side or Diagonal: ")
    k = "Side","side","diagonal","Diagonal"
    while y not in k:
        print("your choose is not correct please try again")
        y = input("from Side or Diagonal: ")
    if y == "Side" or y == "side":
        while not gif:
            try:
                side_cube = float(input("please enter the side: "))
                gif = True
            except ValueError:
                print("it is not a number")
            else:
                root=tkinter.Tk()
                root.geometry("400x400")
                root.resizable(False,False)
                def clicked():
                    lbl.configure(text=f"The area is {(side_cube*side_cube)*6} (buttom exit)", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  side is {side_cube}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="yes", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=140)    
                def clicked():
                    lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the side is {side_cube}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="no", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=180)
                def Terminate():
                    root.destroy()
                btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                btn_2.place(height=50,width=300,x=50,y=220)
                root.mainloop()
    elif y == "diagonal" or y == "Diagonal":
        while not gif:
            try:
                diagonal_cube = float(input("please enter the diagonal: "))
                gif = True
            except ValueError:
                print("it is not a number")
            else:
                root=tkinter.Tk()
                root.geometry("400x400")
                root.resizable(False,False)
                def clicked():
                    lbl.configure(text=f"The area is {0.5*(diagonal_cube**2)} (buttom exit)", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  diagonal is {diagonal_cube}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="yes", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=140)    
                def clicked():
                    lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                lbl=Label(root, text=f"the  diagonal is {diagonal_cube}\nare you sure?", font=("arial",14), bg="green")
                lbl.place(height=50,width=300,x=50,y=40)
                btn=Button(root, text="no", command=clicked, bd="8")
                btn.place(height=50,width=300,x=50,y=180)
                def Terminate():
                    root.destroy()
                btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                btn_2.place(height=50,width=300,x=50,y=220)
                root.mainloop()
elif x == "oval" or x == "Oval":
        c = input("from Diameter or Radius? ")
        k = "diameter","Diameter","radius","Radius"
        while c not in k:
            print("your choose is not correct please try again")
            c = input("from Diameter or Radius? ")
        if c == "Diameter" or c == "diameter":
            while not gif:
                try:
                    big_diameter = float(input("what is the Big daimeter: "))
                except:
                    print("it is not a number")
                else:
                    while not gif:
                        try:
                            small_diameter = float(input("what is the Samll daimeter: "))
                        except:
                            print("it is not a number mooz")
                        else:
                            root=tkinter.Tk()
                            root.geometry("400x400")
                            root.resizable(False,False)
                            def clicked():
                                lbl.configure(text=f"The area is {((0.5*big_diameter)*(0.5*small_diameter)*3)} (buttom exit)", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Big Diameter is {big_diameter}\nand small diameter is {small_diameter}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=80,width=300,x=50,y=40)
                            btn=Button(root, text="yes", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=140)    
                            def clicked():
                                lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Big Diameter is {big_diameter}\nand small diameter is {small_diameter}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=80,width=300,x=50,y=40)
                            btn=Button(root, text="no", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=180)
                            def Terminate():
                                root.destroy()
                            btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                            btn_2.place(height=50,width=300,x=50,y=220)
                            root.mainloop()
        elif c == "Radius" or c == "radius":
            while not gif:
                try:
                    big_radius = float(input("what is the Big radius: "))
                except:
                    print("it is not a number")
                else:
                    while not gif:
                        try:
                            small_radius = float(input("what is the Samll radius: "))
                        except:
                            print("it is not a number mooz")
                        else:
                            root=tkinter.Tk()
                            root.geometry("400x400")
                            root.resizable(False,False)
                            def clicked():
                                lbl.configure(text=f"The area is {(big_radius*small_radius*3)} (buttom exit)", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Big Radius is {big_radius}\nand Small Radius is {small_radius}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=80,width=300,x=50,y=40)
                            btn=Button(root, text="yes", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=140)    
                            def clicked():
                                lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Big Radius is {big_radius}\nand Small Radius is {small_radius}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=80,width=300,x=50,y=40)
                            btn=Button(root, text="no", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=180)
                            def Terminate():
                                root.destroy()
                            btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                            btn_2.place(height=50,width=300,x=50,y=220)
                            root.mainloop()
elif x == "Sphere" or x == "sphere":
        c = input("from Diameter or Radius? ")
        k = "diameter","Diameter","radius","Radius"
        while c not in k:
            print("your choose is not correct please try again")
            c = input("from Diameter or Radius? ")
        if c == "Diameter" or c == "diameter":
            while not gif:
                try:
                    diameter_sphere = float(input("what is the daimeter: "))   
                    gif = True
                except ValueError:
                    print("it is not a number")
                else:         
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {((diameter_sphere/2)**2)*3*4} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Diameter is {diameter_sphere} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Diameter is {diameter_sphere} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
        elif c == "Radius" or c == "radius":
            while not gif:
                try:
                    radius_sphere = float(input("what is the Radius: "))
                    gif = True
                except ValueError:
                    print("it is not a number")
                else:
                    root=tkinter.Tk()
                    root.geometry("400x400")
                    root.resizable(False,False)
                    def clicked():
                        lbl.configure(text=f"The area is {(radius_sphere**2)*3*4} (buttom exit)", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Radius is {radius_sphere} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="yes", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=140)    
                    def clicked():
                        lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                    lbl=Label(root, text=f"the Radius is {radius_sphere} \nare you sure?", font=("arial",14), bg="green")
                    lbl.place(height=50,width=300,x=50,y=40)
                    btn=Button(root, text="no", command=clicked, bd="8")
                    btn.place(height=50,width=300,x=50,y=180)
                    def Terminate():
                        root.destroy()
                    btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                    btn_2.place(height=50,width=300,x=50,y=220)
                    root.mainloop()
elif x == "cone" or x == "Cone":
        c = input("Side area or total area? ")
        k = "Total area","total area","side area","Side area"
        while c not in k:
            print("please type (total area) or (side area) and try again")
            c = input("Side area or total area? ")
        if c == "side area" or c == "Side area":
            while not gif:
                try:
                    edge = float(input("what is the edge: "))
                except ValueError:
                    print("it is not a number")
                else:
                    while not gif:
                        try:
                            radius_cone = float(input("what is the radius: "))
                        except ValueError:
                            print("it is not a number")
                        else:
                            root=tkinter.Tk()
                            root.geometry("400x400")
                            root.resizable(False,False)
                            def clicked():
                                lbl.configure(text=f"The area is {3*edge*radius_cone} (buttom exit)", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Edge is {edge} and Radius is {radius_cone} \nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=50,width=300,x=50,y=40)
                            btn=Button(root, text="yes", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=140)    
                            def clicked():
                                lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Edge is {edge} and Radius is {radius_cone}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=50,width=300,x=50,y=40)
                            btn=Button(root, text="no", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=180)
                            def Terminate():
                                root.destroy()
                            btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                            btn_2.place(height=50,width=300,x=50,y=220)
                            root.mainloop()
        elif c == "total area" or c == "Total arae":
            while not gif:
                try:
                    radius_cone2 = float(input("what is the Radius: "))
                except ValueError:
                    print("it is not a number")
                else:
                    while not gif:
                        try:
                            height_cone = float(input("what is the height: "))
                        except ValueError:
                            print("it is not a number")
                        else:
                            root=tkinter.Tk()
                            root.geometry("400x400")
                            root.resizable(False,False)
                            def clicked():
                                lbl.configure(text=f"The area is {math.sqrt((radius_cone2**2)+(height_cone**2))}\n(buttom exit)", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Radius is {radius_cone2} and Height is {height_cone}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=50,width=300,x=50,y=40)
                            btn=Button(root, text="yes", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=140)    
                            def clicked():
                                lbl.configure(text=f"please buttom Exit and try again", font=("arial",14), bg="green")
                            lbl=Label(root, text=f"the Radius is {radius_cone2} and Height is {height_cone}\nare you sure?", font=("arial",14), bg="green")
                            lbl.place(height=50,width=300,x=50,y=40)
                            btn=Button(root, text="no", command=clicked, bd="8")
                            btn.place(height=50,width=300,x=50,y=180)
                            def Terminate():
                                root.destroy()
                            btn_2=Button(root, text="Exit", command=Terminate, bd="8")
                            btn_2.place(height=50,width=300,x=50,y=220)
                            root.mainloop()