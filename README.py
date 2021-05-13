from tkinter import  *
from tkinter import ttk
import mysql.connector
class oder:
    def __init__(self,root):
        self.root=root
        self.root.title("oder book")
        self.root.geometry("1370x700+0+0")
        title = Label(self.root,text="ODER BOOK",bd=9,relief=GROOVE,font=("times new roman",50,"bold"))
        title.pack(side=TOP,fill=X)
        #  all variable
        self.part_no_var = StringVar()
        self.parts_name_var = StringVar()
        self.qty_var = StringVar()
        self.parts_group_var = StringVar()
        self.parts_company_var = StringVar()
        self.ws_name_var = StringVar()
        self.search_var = StringVar()
        self.search1_var = StringVar()

        #  manage fram
        manage_fram = Frame(self.root,bd=4,relief=RIDGE)
        manage_fram.place(x=20,y=100,width=450,height=585)

        m_title = Label(manage_fram,text="ENTER ODER",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_part_no = Label(manage_fram,text="PART NUMBER",font=("times new roman",15,"bold"))
        lbl_part_no.grid(row=1,column=0,pady=10,padx=0,sticky="w")
        txt_part_no = Entry(manage_fram,textvariable=self.part_no_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_part_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_part_name = Label(manage_fram, text="PART NAME", font=("times new roman", 15, "bold"))
        lbl_part_name.grid(row=2, column=0, pady=10, padx=0,sticky="w")
        txt_part_name = Entry(manage_fram,textvariable=self.parts_name_var, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_part_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_qty = Label(manage_fram, text="QTY", font=("times new roman", 15, "bold"))
        lbl_qty.grid(row=3, column=0, pady=10, padx=0,sticky="w")
        txt_qty = Entry(manage_fram,textvariable=self.qty_var ,font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_qty.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_pg = Label(manage_fram, text="PARTS GROUP", font=("times new roman", 15, "bold"))
        lbl_pg.grid(row=4, column=0, pady=10, padx=0, sticky="w")
        combo_pg = ttk.Combobox(manage_fram ,textvariable=self.parts_group_var, font=("times new roman",13,"bold"))
        combo_pg['values']=("oil","filter","brake","wtr body","glass","hose","RDTR")
        combo_pg.grid(row=4,column=1,padx=10,pady=0)

        lbl_pc = Label(manage_fram, text="PARTS COMPANY", font=("times new roman", 15, "bold"))
        lbl_pc.grid(row=5, column=0, pady=10, padx=0, sticky="w")
        combo_pc = ttk.Combobox(manage_fram,textvariable=self.parts_company_var, font=("times new roman", 13, "bold"))
        combo_pc['values'] = ("MGP", "TVS", "BANCO","MAHLA","AIS","MOBIL",)
        combo_pc.grid(row=5, column=1, padx=10, pady=0)

        lbl_wn = Label(manage_fram, text="W/S NAME", font=("times new roman", 15, "bold"))
        lbl_wn.grid(row=6, column=0, pady=10, padx=0, sticky="w")
        combo_wn = ttk.Combobox(manage_fram,textvariable=self.ws_name_var, font=("times new roman", 13, "bold"))
        combo_wn['values'] = ("RS MOTORS", "FTC", "AIS DIST","JMA","PAWAN AUTO","DTC")
        combo_wn.grid(row=6, column=1, padx=10, pady=0)

        # BUTTON FRAM
        btn_fram = Frame(manage_fram, bd=3, relief=RIDGE)
        btn_fram.place(x=12, y=525, width=420 )

        addbtn = Button(btn_fram,text="ADD",width=10,command=self.add_oder).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_fram, text="UPDATE", width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_fram, text="DELETE", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_fram, text="CLEAR", width=10).grid(row=0, column=3, padx=10, pady=10)

        #  details fram
        details_fram = Frame(self.root, bd=4, relief=RIDGE)
        details_fram.place(x=500, y=100, width=1000, height=585)

        lbl_search = Label(details_fram, text="SEARCH", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(details_fram,textvariable=self.search_var, font=("times new roman", 13, "bold"), width=10 )
        combo_search['values'] = ("PARTS GROUP", "PARTS COMPANY", "W/S NAME")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        lbl_search1 = Label(details_fram, text="SEARCH BY LIST", font=("times new roman", 20, "bold"))
        lbl_search1.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        combo_serch1 = ttk.Combobox(details_fram,textvariable=self.search1_var, font=("times new roman", 13, "bold"), width=10)
        combo_serch1['values'] = ("")
        combo_serch1.grid(row=0, column=3, padx=20, pady=10)

        serchbtn = Button(details_fram, text="SERCH", width=10,pady=5).grid(row=0, column=4, padx=10, pady=10)
        showbtn = Button(details_fram, text="SHOW ALL", width=10,pady=5).grid(row=0, column=5, padx=10, pady=10)

        #  table fram
        table_fram = Frame(details_fram, bd=4 , relief=RIDGE)
        table_fram.place(x=10, y=70, width=970, height=500)

        scroll_x = Scrollbar(table_fram,orient =HORIZONTAL)
        scroll_y = Scrollbar(table_fram, orient=VERTICAL)


        self.oder_table = ttk.Treeview(table_fram,
                                       column=("part no","parts name","qty","parts group","parts company","w/s name" )
                                       ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.oder_table.xview)
        scroll_y.config(command=self.oder_table.yview)

        self.oder_table.heading("part no",text ="PART NUMBER")
        self.oder_table.heading("parts name", text="PART NAME")
        self.oder_table.heading("qty", text="QTY")
        self.oder_table.heading("parts group", text="PARTS GROUP")
        self.oder_table.heading("parts company", text="PARTS COMPANY")
        self.oder_table.heading("w/s name", text="W/S NAME")

        self.oder_table['show']='headings'

        self.oder_table.column("part no" , width=100)
        self.oder_table.column("parts name", width=100)
        self.oder_table.column("qty", width=100)
        self.oder_table.column("parts group", width=100)
        self.oder_table.column("parts company", width=100)
        self.oder_table.column("w/s name", width=100)
        self.oder_table.pack(fill=BOTH,expand=1)

    def add_oder(sefl):
        mydb=mysql.connector.connect(host="localhost",user="root",password="")




class oder():
    pass
    root=Tk()
    obj=oder(root)
    root.mainloop()
