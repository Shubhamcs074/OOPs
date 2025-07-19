from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import mysql.connector

class create_acc:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("1295x550+230+220")

        # =================variable ======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        

        # Just a label to show it's working
        # ===================== Title ====================
        title = Label(self.root, text="Create Account", font=("Arial", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=70)

        # =====================logo ======================
        img2=Image.open("C:\\Users\\HP\\Desktop\\python\\LOGO1.png")
        img2=img2.resize((100,70),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=100,height=70)

        #======================= label Frame ==============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=80,width=425,height=490)

        # ===================== label and entry ===========
        #custRef
        label_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)

        # cust name
        cname=Label(labelframeleft,text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)

        # cust mname
        cmname=Label(labelframeleft,text="Mother Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        cmname.grid(row=2,column=0,sticky=W)
        txtcmname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtcmname.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # Postcode 
        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        # mobile Number
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile No.:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        # email
        lblemail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)

        # nationality
        lblnationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
        combo_nationality["value"]=("Indian","Foreign")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        

        # id proof type combobox
        lblId_proof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblId_proof.grid(row=8,column=0,sticky=W)
        combo_idtype=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
        combo_idtype["value"]=("Aadhar","PAN","Voter ID")
        combo_idtype.current(0)
        combo_idtype.grid(row=8,column=1)
        
        # id Number 
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # Address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        # ====================== btns ================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnAdd=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=1,padx=1)

        btnAdd=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=2,padx=1)

        btnAdd=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=3,padx=1)

        # =====================Table frame==============
        Table_frame = LabelFrame(self.root, bd=2, text="View and Search Customer Details", font=("arial", 12, "bold"), relief=RIDGE)
        Table_frame.place(x=435,y=0,width=860,height=490)

        lblSearchBy=Label(Table_frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnAdd=Button(Table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=4,padx=1)

        # =============== Show Data table ===============

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)    


        
if __name__ == "__main__":
    root = Tk()
    obj = create_acc(root)
    root.mainloop()
