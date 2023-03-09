def coculating_process():
    global x,y,d    
    a = float(cof_a.get())
    b = float(cof_b.get())
    c = float(cof_c.get())
    
    d = float(((b**2)-(4*a*c)))
    x = float((-b/(2*a)))
    y = float((((4*a*c)-(b**2))/(4*a)))
    x1 = ((-b)+d**(1/2))/(2*a)
    x2 = ((-b)-d**(1/2))/(2*a)  
    
    D.set(d) 
    vertex.set("("+ str(x)+ ","+ str(y)+ ")")
    
    if(d < 0):           
        root.set("無實根")        
    
    if(d == 0):        
        root.set("重根")
    
    if(d > 0):
        root.set("有相異兩根")
        ans_x1.set("x1="+ str(x1))
        ans_x2.set("x2="+ str(x2))

import tkinter as tk

win = tk.Tk()
win.geometry("790x370")
win.resizable(0, 0)
win.title("一元二次方程式 計算機")

class GUI_interface():
    reference_point_x1=10
    reference_point_y1=10
    
    label1 = tk.Label(win, text="一元二次方程式 計算機", fg="black", font=("微軟正黑體", 24))
    label1.place(x=reference_point_x1, y=reference_point_y1)
    label2 = tk.Label(win, text="輸入係數", fg="gray", font=("微軟正黑體", 18))
    label2.place(x=reference_point_x1, y=reference_point_y1+60)

    reference_point_x2 = 10
    reference_point_y2 = 110
    x_len = 200
    input_len = 50
    unit1 = input_len+x_len
    
    global cof_a
    cof_a = tk.StringVar()
    input1 = tk.Entry(win, font=("微軟正黑體", 20), bg="white", width="12", textvariable=cof_a)
    input1.place(x=reference_point_x2, y=reference_point_y2)
    x_pow2 = tk.Label(win, text="x²+", fg="gray", font=("微軟正黑體", 20))
    x_pow2.place(x=reference_point_x2+x_len, y=reference_point_y2)  
    
    global cof_b
    cof_b = tk.StringVar()
    input2 = tk.Entry(win, font=("微軟正黑體", 20), bg="white", width="12", textvariable=cof_b)
    input2.place(x=reference_point_x2+unit1, y=reference_point_y2)
    x_pow1 = tk.Label(win, text="x+", fg="gray", font=("微軟正黑體", 20))
    x_pow1.place(x=reference_point_x2+unit1+x_len, y=reference_point_y2)
    
    global cof_c
    cof_c = tk.StringVar()
    input3 = tk.Entry(win, font=("微軟正黑體", 20), bg="white", width="12", textvariable=cof_c)
    input3.place(x=reference_point_x2+2*unit1-10, y=reference_point_y2)
    
    bottom1 = tk.Button(win, text="Enter", bg="gray", fg="white", font=("微軟正黑體", 15), command=coculating_process)
    bottom1.place(x=reference_point_x2+2*unit1+x_len, y=reference_point_y2-5)

    reference_point_x3 = 10
    reference_point_y3 = 165
    y_len = 40

    global D,root,ans_x1,ans_x2,vertex
    D = tk.StringVar() 
    root = tk.StringVar()
    ans_x1 = tk.StringVar()
    ans_x2 = tk.StringVar()     
    vertex = tk.StringVar()

    ans_D_label = tk.Label(win, text=("判別式="), fg="black", font=("微軟正黑體", 20))
    ans_D_label.place(x=reference_point_x3, y=reference_point_y3)
    ans_D = tk.Label(win, fg="black", font=("微軟正黑體", 20), textvariable=D)
    ans_D.place(x=reference_point_x3+105, y=reference_point_y3)
    
    ans_vertex = tk.Label(win, text=("頂點="), fg="black", font=("微軟正黑體", 20))
    ans_vertex.place(x=reference_point_x3, y=reference_point_y3+1*y_len)
    ans_vertex = tk.Label(win, fg="black", font=("微軟正黑體", 20), textvariable=vertex)
    ans_vertex.place(x=reference_point_x3+70, y=reference_point_y3+1*y_len)
    
    root_label = tk.Label(win, fg="black", font=("微軟正黑體", 20), textvariable=root)
    root_label.place(x=reference_point_x3, y=reference_point_y3+2*y_len)
    
    label_ans_x1 = tk.Label(win, fg="black", font=("微軟正黑體", 20), textvariable=ans_x1)
    label_ans_x1.place(x=reference_point_x3, y=reference_point_y3+3*y_len)
    
    label_ans_x2 = tk.Label(win, fg="black", font=("微軟正黑體", 20), textvariable=ans_x2)
    label_ans_x2.place(x=reference_point_x3, y=reference_point_y3+4*y_len)

win.mainloop()