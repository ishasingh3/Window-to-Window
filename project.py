
import mysql.connector as sql 
from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
mainbg = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebBackground.gif' mainbg_heading = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebBackgroundHeading.gif' icon = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebIcon.ico' bg_reg = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebBackgroundReg.gif' bg_signup = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebBackgroundSignUp.gif' bg_dept = 'C:\\Users\\acer\\Desktop\\Project\\CS Project\\CS Images\\WebBackgroundDept.gif' mycon=sql.connect( 
 host='localhost', 
 user='root', 
 passwd='password', 
 database='WindowToWindow') 
cursor=mycon.cursor(buffered=True) 
cursor.execute('CREATE DATABASE IF NOT EXISTS WindowToWindow') 
cursor.execute('''CREATE TABLE IF NOT EXISTS BUSINESS (Shop_Code INT(5) ZEROFILL AUTO_INCREMENT  PRIMARY KEY, 
 fname varchar(20), 
 lname varchar(20), 
 Shop_Name varchar(30), 
 Deptartment varchar(13), 
 City varchar(20), 
 Pincode int(7), 
 Phone_number int(12), 
 Email_ID varchar(40),
 Password varchar(30))''') 
cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER (fname varchar(20), 
 lname varchar(20), 
 City varchar(15), 
 Pincode int(7), 
 Phone_number int(12), 
 Email_ID varchar(40), 
 Password varchar(30))''') 
'***************************************DATA DISPLAY***************************************' def display(lst): 
 root = Tk() 
 root.title('WINDOW TO WINDOW') 
 root.iconbitmap(icon) 
 frametop = LabelFrame(root,text="Here are the details of the stores nearest to you!")#,padx=50,pady=50)  frametop.pack(side= TOP) 
 framebottom = LabelFrame(root) 
 framebottom.pack(side= BOTTOM) 
 msg = Label(frametop, text="Here are the details of the stores nearest to you!",font="Times 20 ",  bg='#f7aca8',fg="#21626e") 
 msg.grid_columnconfigure(0,weight=6) 
 msg2= Label(frametop, text="Happy Shopping!",font="Times 20 ", bg='#f7aca8',fg="#21626e")  msg2.grid_columnconfigure(1,weight=6) 
 fname_labelD = Label(framebottom,width=18, text="First Name", font="Times 16 ",  bg='#f7aca8',fg="#21626e") 
 fname_labelD.grid(row=2, column=0) 
 lname_labelD = Label(framebottom,width=18, text="Last Name", font="Times 16 ",  bg='#f7aca8',fg="#21626e") 
 lname_labelD.grid(row=2, column=1) 
 shname_labelD = Label(framebottom,width=18, text="Shop Name", font="Times 16 ",  bg='#f7aca8',fg="#21626e") 
 shname_labelD.grid(row=2, column=2) 
 city_labelD = Label(framebottom,width=18, text="City", font="Times 16 ", bg='#f7aca8',fg="#21626e")  city_labelD.grid(row=2, column=3)
 phno_labelD = Label(framebottom,width=18, text="Phone Number", font="Times 16 ",  bg='#f7aca8',fg="#21626e") 
 phno_labelD.grid(row=2, column=4) 
 email_labelD = Label(framebottom,width=18, text="E-mail ID", font="Times 16 ", bg='#f7aca8',fg="#21626e")  email_labelD.grid(row=2, column=5) 
 total_rows = len(lst) #total_columns = 7 #len(data_gD[0]) 
 for i in range(total_rows): 
 for j in range(6): 
 self = Entry(framebottom,width=20,font= "Times 16 ", bg='white',fg="#21626e")  self.grid(row=i+4, column=j) 
 self.insert(END, lst[i][j]) 
'********************************BUTTON FUNCTIONS**************************************'  CLOTHING 
def dept_cloth(): 
 global city_combo2 
 if city_combo2.get()=='Delhi': 
 query_cD='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cD) 
 data_cD = cursor.fetchall() 
 display(data_cD) 
 elif city_combo2.get()=='Noida': 
 query_cN='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cN) 
 data_cN = cursor.fetchall() 
 display(data_cN) 
 elif city_combo2.get()=='Ghaziabad': 
 query_cG='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cG) 
 data_cG = cursor.fetchall() 
 display(data_cG)
 elif city_combo2.get()=='Faridabad': 
 query_cF='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cF) 
 data_cF = cursor.fetchall() 
 display(data_cF) 
 elif city_combo2.get()=='Gurugram': 
 query_cGu='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cGu) 
 data_cGu = cursor.fetchall() 
 display(data_cGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_cGN='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Clothing"' 
 cursor.execute(query_cGN) 
 data_cGN = cursor.fetchall() 
 display(data_cGN) 
FOOTWEAR 
def dept_footwear(): 
 global city_combo2 
 if city_combo2.get()=='Delhi': 
 query_fwD='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwD) 
 data_fwD = cursor.fetchall() 
 display(data_fwD) 
 elif city_combo2.get()=='Noida': 
 query_fwN='SELECT fname,lname,shop_name,phone_number,email_ID,city FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwN) 
 data_fwN = cursor.fetchall() 
 display(data_fwN) 
 elif city_combo2.get()=='Ghaziabad':
 query_fwG='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwG) 
 data_fwG = cursor.fetchall() 
 display(data_fwG) 
 elif city_combo2.get()=='Faridabad': 
 query_fwF='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwF) 
 data_fwF = cursor.fetchall() 
 display(data_fwF) 
 elif city_combo2.get()=='Gurugram': 
 query_fwGu='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwGu) 
 data_fwGu = cursor.fetchall() 
 display(data_fwGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_fwGN='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Footwear"' 
 cursor.execute(query_fwGN) 
 data_fwGN = cursor.fetchall() 
 display(data_fwGN) 
GROCERY 
def dept_grocery(): 
 global city_combo2 
 if city_combo2.get()=='Delhi': 
 query_gD='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gD) 
 data_gD = cursor.fetchall() 
 display(data_gD) 
 elif city_combo2.get()=='Noida':
 query_gN='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gN) 
 data_gN = cursor.fetchall() 
 display(data_gN) 
 elif city_combo2.get()=='Ghaziabad': 
 query_gG='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gG) 
 data_gG = cursor.fetchall() 
 display(data_gG) 
 elif city_combo2.get()=='Faridabad': 
 query_gF='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gF) 
 data_gF = cursor.fetchall() 
 display(data_gF) 
 elif city_combo2.get()=='Gurugram': 
 query_gGu='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gGu) 
 data_gGu = cursor.fetchall() 
 display(data_gGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_gGN='SELECT fname,lname,shop_name,phone_number,email_ID FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Grocery"' 
 cursor.execute(query_gGN) 
 data_gGN = cursor.fetchall() 
 display(data_gGN) 
MEDICINE 
def dept_medicine(): 
 global city_combo2 
 if city_combo2.get()=='Delhi':
 query_gD='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gD) 
 data_gD = cursor.fetchall() 
 display(data_gD) 
 elif city_combo2.get()=='Noida': 
 query_gN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gN) 
 data_gN = cursor.fetchall() 
 display(data_gN) 
 elif city_combo2.get()=='Ghaziabad': 
 query_gG='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gG) 
 data_gG = cursor.fetchall() 
 display(data_gG) 
 elif city_combo2.get()=='Faridabad': 
 query_gF='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gF) 
 data_gF = cursor.fetchall() 
 display(data_gF) 
 elif city_combo2.get()=='Gurugram': 
 query_gGu='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gGu) 
 data_gGu = cursor.fetchall() 
 display(data_gGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_gGN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Medicine"' 
 cursor.execute(query_gGN) 
 data_gGN = cursor.fetchall()
 display(data_gGN) 
FOOD 
def dept_food(): 
 global city_combo2 
 if city_combo2.get()=='Delhi': 
 query_gD='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Food"' 
 cursor.execute(query_gD) 
 data_gD = cursor.fetchall() 
 display(data_gD) 
 elif city_combo2.get()=='Noida': 
 query_gN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Food"' 
 cursor.execute(query_gN) 
 data_gN = cursor.fetchall() 
 display(data_gN) 
 elif city_combo2.get()=='Ghaziabad': 
 query_gG='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Food"' 
 cursor.execute(query_gG) 
 data_gG = cursor.fetchall() 
 display(data_gG) 
 elif city_combo2.get()=='Faridabad': 
 query_gF='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Food"' 
 cursor.execute(query_gF) 
 data_gF = cursor.fetchall() 
 display(data_gF) 
 elif city_combo2.get()=='Gurugram': 
 query_gGu='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Food"' 
 cursor.execute(query_gGu) 
 data_gGu = cursor.fetchall()
 display(data_gGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_fGN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Food"' 
 cursor.execute(query_fGN) 
 data_fGN = cursor.fetchall() 
 display(data_fGN)  
ELETRONICS 
def dept_elect(): 
 global city_combo2 
 if city_combo2.get()=='Delhi': 
 query_eD='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Delhi" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eD) 
 data_eD = cursor.fetchall() 
 display(data_eD) 
 elif city_combo2.get()=='Noida': 
 query_eN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Noida" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eN) 
 data_eN = cursor.fetchall() 
 display(data_eN) 
 elif city_combo2.get()=='Ghaziabad': 
 query_eG='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Ghaziabad" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eG) 
 data_eG = cursor.fetchall() 
 display(data_eG) 
 elif city_combo2.get()=='Faridabad': 
 query_eF='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Faridabad" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eF) 
 data_eF = cursor.fetchall() 
 display(data_eF)
 elif city_combo2.get()=='Gurugram': 
 query_eGu='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Gurugram" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eGu) 
 data_eGu = cursor.fetchall() 
 display(data_eGu) 
 elif city_combo2.get()=='Greater Noida': 
 query_eGN='SELECT fname,lname,shop_name,city,phone_number,email_ID FROM BUSINESS WHERE  CITY="Greater Noida" AND DEPARTMENT="Electronics"' 
 cursor.execute(query_eGN) 
 data_eGN = cursor.fetchall() 
 display(data_eGN) 
'*******************************DEPARTMENT WINDOW*******************************' def Department(): 
 global bgimage_dept 
 global img_cloth 
 global img_fw 
 global img_food 
 global img_med 
 global img_elec 
 global img_groc 
 top_dept = Toplevel() 
 top_dept.title("WINDOW TO WINDOW") 
 top_dept.iconbitmap('#WebIcon.ico') 
 canvas_dept = Canvas(top_dept, width=1350, height=600) 
 canvas_dept.pack() 
 bgimage_dept = PhotoImage(file=bg_dept) 
 bgimage_label = Label(top_dept, image=bgimage_dept) 
 bgimage_label.place(relwidth=1, relheight=1) 
 img_cloth = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-clothing.png')  img_fw = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-footwear.png')  img_food = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-food.png')
 img_elec = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-electronics.png')  img_med = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-medicine.png')  img_groc = PhotoImage(file='C:/Users/acer/Desktop/Project/CS Project/CS Images/button-grocery.png')  button_cloth = Button(top_dept ,bg='#f7aca8', image=img_cloth, command=dept_cloth)  button_cloth.place(relx=0.10, rely=0.20) 
 button_fw = Button(top_dept, bg='#f7aca8', image=img_fw, command=dept_footwear)  button_fw.place(relx=0.50, rely=0.20) 
 button_groc = Button(top_dept, bg='#f7aca8', image=img_groc, command=dept_grocery)  button_groc.place(relx=0.10, rely=0.45) 
 button_med = Button(top_dept, bg='#f7aca8', image=img_med, command=dept_medicine)  button_med.place(relx=0.50, rely=0.45) 
 button_food = Button(top_dept, bg='#f7aca8', image=img_food, command=dept_food)  button_food.place(relx=0.10, rely=0.70) 
 button_elec = Button(top_dept, bg='#f7aca8', image=img_elec, command=dept_elect)  button_elec.place(relx=0.50, rely=0.70) 
"********************************* REGISTRATION *********************************" def Register(): 
 global bgimage_reg  
 top_reg = Toplevel() 
 top_reg.title("WINDOW TO WINDOW") 
 top_reg.iconbitmap(icon) 
 canvas_reg = Canvas(top_reg, width=1350, height=600) 
 canvas_reg.pack() 
 bgimage_reg = PhotoImage(file=bg_reg) 
 bgimage_label = Label (top_reg, image = bgimage_reg) 
 bgimage_label.place(relwidth =1 ,relheight =1) 
 fname_label1 = Label(top_reg, text="First Name", font="Times 16 ", bg="white",fg="#21626e")   fname_label1.place(relx=0.175, rely=0.17) 
 lname_label1 = Label(top_reg, text="Last Name", font="Times 16 ", bg="white",fg="#21626e")   lname_label1.place(relx=0.50, rely=0.17)
 shname_label1 = Label(top_reg, text="Shop Name", font="Times 16 ", bg="white",fg="#21626e")   shname_label1.place(relx=0.175, rely=0.26) 
 dept_label1 = Label(top_reg, text="Department", font="Times 16 ", bg="white",fg="#21626e")   dept_label1.place(relx=0.175, rely=0.35) 
 city_label1 = Label(top_reg, text="City", font="Times 16", bg='white',fg='#21626e')  city_label1.place(relx=0.175, rely=0.44) 
 pin_label1 = Label(top_reg, text="Pin Code", font="Times 16",bg='white',fg='#21626e')  pin_label1.place(relx=0.175, rely=0.53) 
 num_label1 = Label(top_reg, text="Contact Number", font="Times 16 ", bg="white",fg="#21626e")   num_label1.place(relx=0.175, rely=0.62) 
 email_label1 = Label(top_reg, text="E-mail Address", font="Times 16 ", bg="white",fg="#21626e")   email_label1.place(relx=0.175, rely=0.71) 
 pass_label1 = Label(top_reg, text="Password", font="Times 16 ", bg="white",fg="#21626e")  pass_label1.place(relx=0.175, rely=0.80) 
 fname_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 fname_frame1.place(relx=0.175, rely=0.21, relwidth=0.30, relheight=0.045)  lname_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 lname_frame1.place(relx=0.50, rely=0.21, relwidth=0.30, relheight=0.045) 
 shname_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 shname_frame1.place(relx=0.175, rely=0.30, relwidth=0.625, relheight=0.045)  dept_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 dept_frame1.place(relx=0.175, rely=0.39, relwidth=0.625, relheight=0.045)  city_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 city_frame1.place(relx=0.175, rely=0.48, relwidth=0.625, relheight=0.045) 
 pin_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 pin_frame1.place(relx=0.175, rely=0.57, relwidth=0.625, relheight=0.045) 
 num_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 num_frame1.place(relx=0.175, rely=0.66, relwidth=0.625, relheight=0.045) 
 email_frame1 = Frame(top_reg, bg='#2a7785', bd=4) 
 email_frame1.place(relx=0.175, rely=0.75, relwidth=0.625, relheight=0.045)  pass_frame1 = Frame(top_reg, bg='#2a7785', bd=4)
 pass_frame1.place(relx=0.175, rely=0.84, relwidth=0.625, relheight=0.045)  dept_v = ["Clothing","Footwear","Grocery","Medicine","Food","Electronics"]  dept_combo = ttk.Combobox(top_reg, values=dept_v) 
 dept_combo.place(relx=0.177, rely=0.395, relwidth=0.620) 
 dept_combo.current(0) 
 city_v = ["Delhi","Noida","Ghaziabad","Faridabad","Gurugram","Greater Noida"]  city_combo = ttk.Combobox(top_reg, values=city_v) 
 city_combo.place(relx=0.177, rely=0.485, relwidth=0.620) 
 city_combo.current(0) 
 fname_entry1 = Entry(fname_frame1) 
 fname_entry1.place(relwidth = 1 , relheight = 1) 
 lname_entry1 = Entry(lname_frame1) 
 lname_entry1.place(relwidth = 1 , relheight = 1) 
 shname_entry1 = Entry(shname_frame1) 
 shname_entry1.place(relwidth = 1 , relheight = 1) 
 pin_entry1 = Entry(pin_frame1) 
 pin_entry1.place(relwidth = 1 , relheight = 1) 
 num_entry1 = Entry(num_frame1) 
 num_entry1.place(relwidth = 1 , relheight = 1) 
 email_entry1 = Entry(email_frame1) 
 email_entry1.place(relwidth = 1 , relheight = 1) 
 pass_entry1 = Entry(pass_frame1) 
 pass_entry1.place(relwidth = 1 , relheight = 1) 
 def New_register(): 
 fname1 = fname_entry1.get() 
 lname1 = lname_entry1.get() 
 shop_name = shname_entry1.get() 
 department = dept_combo.get() 
 city1 = city_combo.get() 
 pincode1 = pin_entry1.get() 
 phone_number1 = num_entry1.get()
 email_ID1 = email_entry1.get() 
 password1 = pass_entry1.get() 
 reg_query ="insert into business  
(fname,lname,shop_name,department,city,pincode,phone_number,email_ID,password)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
 value=(fname1,lname1,shop_name,department,city1,pincode1,phone_number1,email_ID1,password1)  try: 
 cursor.execute(reg_query,value) 
 mycon.commit() 
 messagebox.showinfo("Success!","Your shop is registered now! \n Welcome to Window to Window  family!") 
 except: 
 messagebox.showinfo("Error","Your account could not be created.") 
 submit = Button(top_reg, text='Submit',font='verdana',fg='white',bg='#2a7785',command= New_register)  submit.place(relx=0.47, rely=0.92) 
"************************************* SIGN UP*************************************" def SignUp():  
 global bgimage_sign 
 top_sign = Toplevel() 
 top_sign.title("WINDOW TO WINDOW") 
 top_sign.iconbitmap('#WebIcon.ico') 
 canvas_sign = Canvas(top_sign, width=1350, height=600) 
 canvas_sign.pack() 
 bgimage_sign = PhotoImage(file=bg_signup) 
 bgimage_label = Label (top_sign, image = bgimage_sign) 
 bgimage_label.place(relwidth =1 ,relheight =1) 
 fname_label2 = Label(top_sign, text="First Name", font="Times 16 ", bg="white",fg="#21626e")   fname_label2.place(relx=0.175, rely=0.17) 
 lname_label2 = Label(top_sign, text="Last Name", font="Times 16 ", bg="white",fg="#21626e")   lname_label2.place(relx=0.50, rely=0.17) 
 city_label2 = Label(top_sign, text="City", font="Times 16", bg='white',fg='#21626e')  city_label2.place(relx=0.175, rely=0.28) 
 pin_label2 = Label(top_sign, text="Pin Code", font="Times 16",bg='white',fg='#21626e')
 pin_label2.place(relx=0.175, rely=0.39) 
 num_label2 = Label(top_sign, text="Contact Number", font="Times 16 ", bg="white",fg="#21626e")   num_label2.place(relx=0.175, rely=0.50) 
 email_label2 = Label(top_sign, text="E-mail Address", font="Times 16 ", bg="white",fg="#21626e")   email_label2.place(relx=0.175, rely=0.61) 
 pass_label2 = Label(top_sign, text="Password", font="Times 16 ", bg="white",fg="#21626e")  pass_label2.place(relx=0.175, rely=0.72) 
 fname_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 fname_frame2.place(relx=0.175, rely=0.21, relwidth=0.30, relheight=0.055)  lname_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 lname_frame2.place(relx=0.50, rely=0.21, relwidth=0.30, relheight=0.055) 
 city_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 city_frame2.place(relx=0.175, rely=0.32, relwidth=0.625, relheight=0.055) 
 pin_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 pin_frame2.place(relx=0.175, rely=0.43, relwidth=0.625, relheight=0.055) 
 num_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 num_frame2.place(relx=0.175, rely=0.54, relwidth=0.625, relheight=0.055)  email_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 email_frame2.place(relx=0.175, rely=0.65, relwidth=0.625, relheight=0.055)  pass_frame2 = Frame(top_sign, bg='#2a7785', bd=4) 
 pass_frame2.place(relx=0.175, rely=0.76, relwidth=0.625, relheight=0.055)  global city_combo2 
 city_v = ["Delhi","Noida","Ghaziabad","Faridabad","Gurugram","Greater Noida"]  city_combo2= ttk.Combobox(top_sign, values=city_v) 
 city_combo2.place(relx=0.177, rely=0.325, relwidth=0.620, relheight=0.045)  city_combo2.current(0) 
 fname_entry2 = Entry(fname_frame2) 
 fname_entry2.place(relwidth = 1 , relheight = 1) 
 lname_entry2 = Entry(lname_frame2) 
 lname_entry2.place(relwidth = 1 , relheight = 1) 
 pin_entry2 = Entry(pin_frame2)
 pin_entry2.place(relwidth = 1 , relheight = 1) 
 num_entry2 = Entry(num_frame2) 
 num_entry2.place(relwidth = 1 , relheight = 1) 
 email_entry2 = Entry(email_frame2) 
 email_entry2.place(relwidth = 1 , relheight = 1) 
 pass_entry2 = Entry(pass_frame2) 
 pass_entry2.place(relwidth = 1 , relheight = 1) 
 def New_signup(): 
 fname2 = fname_entry2.get() 
 lname2 = lname_entry2.get() 
 city2 = city_combo2.get() 
 pincode2 = pin_entry2.get() 
 phone_number2 = num_entry2.get() 
 email_ID2 = email_entry2.get() 
 password2 = pass_entry2.get() 
 sign_query ="insert into customer (fname,lname,city,pincode,phone_num,email_ID,password)  values(%s,%s,%s,%s,%s,%s,%s)" 
 value=(fname2,lname2,city2,pincode2,phone_number2,email_ID2,password2)  try: 
 cursor.execute(sign_query,value) 
 mycon.commit()  
 except:  
 messagebox.showinfo("Error","Your account could not be created.") 
 a=1 
 start = Button(top_sign, text='Start Shopping!',font='verdana',fg='white',bg='#2a7785',  command=lambda:[New_signup(),Department()]) #lambda:[New_signup(), Department(), close(top_sign)]) 
 start.place(relx=0.43, rely=0.87) 
 return city_combo2 
"********************************** MAIN WINDOW **********************************" root=Tk() 
root.title('WINDOW TO WINDOW') 
root.iconbitmap('#WebIcon.ico')
canvas = Canvas(root, width = 1350, height = 600)  
canvas.pack() 
bg_image = PhotoImage(file="#WebBackground.gif")  
canvas.create_image(0,0, anchor=NW, image=bg_image) 
bg_label = Label (root, image = bg_image) 
bg_label.place(width=1, height=1) 
bg_imgheading = PhotoImage(file="#WebBackgroundHeading.gif" ) 
bg_label = Label (root, image = bg_imgheading) 
bg_label.place(relwidth = 1 ,relheight = 0.19) 
register_label = Label (root, text="* Register your BUSINESS today to get the best customers!",font='Times  25',bg='#f7aca8',fg="#21626e") 
register_label.place(relx=0.15, rely=0.19) 
register = Button(root, text='Register Now',font='verdana',fg='white',bg='#2a7785', command=Register) register.place(relx=0.75, rely=0.20) 
msg_label = Label (root, text="FOR CONSUMERS:", font='Times 20',bg='#f7aca8',fg="white") msg_label.place(relx=0.40, rely=0.27) 
fname_label = Label(root, text="First Name", font="Times 16 ", bg='#f7aca8',fg="#21626e")  fname_label.place(relx=0.15, rely=0.34) 
lname_label = Label(root, text="Last Name", font="Times 16 ", bg='#f7aca8',fg="#21626e") lname_label.place(relx=0.15, rely=0.45) 
email_label = Label(root, text="Email Address", font="Times 16", bg="#f7aca8", fg="#21626e") email_label.place(relx=0.15, rely=0.56) 
pass_label = Label(root, text="Password", font="Times 16", bg="#f7aca8", fg="#21626e") pass_label.place(relx=0.15, rely=0.67) 
fname_frame = Frame(root, bg='#2a7785', bd=4) 
fname_frame.place(relx=0.15, rely=0.39, relwidth=0.30, relheight=0.055) 
lname_frame = Frame(root, bg='#2a7785', bd=4) 
lname_frame.place(relx=0.15, rely=0.50, relwidth=0.30, relheight=0.055) 
email_frame = Frame(root, bg='#2a7785', bd=4) 
email_frame.place(relx=0.15, rely=0.61, relwidth=0.70, relheight=0.055) 
pass_frame = Frame(root, bg='#2a7785', bd=4) 
pass_frame.place(relx=0.15, rely=0.72, relwidth=0.70, relheight=0.055)
fname_entry = Entry(fname_frame) 
fname_entry.place(relwidth = 1 , relheight = 1) 
lname_entry = Entry(lname_frame) 
lname_entry.place(relwidth =1, relheight= 1) 
email_entry = Entry(email_frame) 
email_entry.place(relwidth = 1, relheight=1) 
pass_entry = Entry(pass_frame) 
pass_entry.place(relwidth = 1, relheight=1) 
def login(): 
 fname = fname_entry.get() 
 lname = lname_entry.get() 
 Email_ID = email_entry.get() 
 password = pass_entry.get() 
 cursor = mycon.cursor(buffered=True) 
 cursor.execute("SELECT fname,lname,email_ID,password FROM CUSTOMER")  table_data = cursor.fetchall() 
 #print(table_data) 
 for i in range (0,len(table_data)): 
 if table_data[i][0]==fname and table_data[i][1]==lname and table_data[i][2]==Email_ID and  table_data[i][3]==password:  
 val=(fname,lname,email_ID,password) 
 sql="SELECT * FROM customer WHERE fname = %s AND lname= %s AND email_ID= %s AND  password=%s" 
 cursor.execute(sql,val) 
 mycon.commit() 
 messagebox.showinfo("you did it","correct mam.")  
 break  
 else: 
 messagebox.showinfo("Error","Wrong information entered.") 
 break 
login = Button(root, text='Log In',font='verdana',fg='white',bg='#2a7785',command=login)  login.place(relx=0.5, rely=0.79)
sign_label = Label (root, text="Don't have an account? Make one right now!",font='Times 19  ',bg='#f7aca8',fg="#21626e") 
sign_label.place(relx=0.35, rely=0.87) 
signup = Button(root, text='Sign Up',font='verdana',fg='white',bg='#2a7785', command=SignUp) signup.place(relx=0.499, rely=0.93) 
root.mainloop()
