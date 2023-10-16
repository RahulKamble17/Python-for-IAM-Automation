#from curses import wrapper
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *


#GUI Window
root= tk.Tk()
root.geometry("800x500")
root.resizable(True,True)
root.title('Query Generator')

cog_img=tk.PhotoImage(file="")
ImgLabel= ttk.Label(root,text=" " ,image=cog_img)
ImgLabel.pack(side=TOP)



#Entry Frame
entries= ttk.Frame(root)
entries.pack(padx=10,pady=10,fill="both",expand="yes")

#Button Frame
wrapper=LabelFrame(root)
wrapper.pack(padx=10,pady=10,fill="both",expand="yes")

#Query Generator
def generator():
    file=open('output.txt','a')
    user_id=id_entry.get()
    #fname=fname_entry.get()
    #lname=lname_entry.get()
    name=Name_entry.get() #fname+" "+lname
    ritm=ritm_entry.get()
    role=role_combo.get()
    module=module_combo.get()

    name_split=name.split()
    print(name_split)
    fname=name_split[0]

    lname=""
    for i in range(len(name_split)-1):
        lname+=name_split[i+1]

    file.write("INSERT INTO WC_SEC_USER_GROUP_MAP(ebs_user_id,obiee_group_name,ad_user_id,lst_name,fst_name,full_name,Active_flg,Comments,Module,CREATED_BY,UPDATED_BY,EFF_ST_DATE,CREATED_DT,LAST_UPD_DT,LICENSE_GROUP) VALUES( '"+user_id+"','"+role+"','"+user_id+"','"+lname+"','"+fname+"','"+name+"','Y','"+ritm+"','"+module+"','aggarwa4','aggarwa4',SYSDATE,SYSDATE,SYSDATE,'');")
    file.write("\n\n")

#Opening File
def openFile():
    fileName="output.txt"
    os.system("start " + fileName)

#Clearing File
def clearFile():
    file=open('output.txt','w')

#Lists of Modules & Roles 
modules=["Manufacturing","SCOM","Finance"]
Manufacturing=["Celgene - Manufacturing Global Planning User","Celgene - Manufacturing User","Celgene - Manufacturing Costing Super User","Celgene - Manufacturing Global Planning Super User","Celgene Manufacturing CTDP User","RegCMC User","MRP Manufacturing User","ICP Super User","Celgene - Manufacturing Super User","Celgene Manufacturing CTDP Super User","Celgene - Manufacturing Phx Fin User","Oracle Bill of Material Corporate User","Celgene - Manufacturing Costing User","Oracle Bill of Material Corporate Super User","Cost Acct Super User"]
SCOM=["Celgene - USLSP User","SCOM Inv User","Oracle Inventory User Corporate","Oracle Order Management Interface Corporate Super User","Oracle Work in Process Corporate User","Oracle Order Management Interface Corporate User","Inventory Movements Super User","Oracle Supply Chain Planning User Corporate","Oracle Supply Chain Planning Super User Corporate","Inventory Balances Super User","Supply chain Americas","Inventory Movements User","Oracle Advanced Supply Chain Planning User Corporate","SCOM OM User","Oracle Inventory Super User Corporate","Oracle Work in Process Corporate Super User","SCOM OM Super User","Oracle Advanced Supply Chain Planning Super User Corporate","Inventory Balances User","SCOM Inv Super User"]
Finance=["Secondary Ledger Super User","Financial Revenue Super User","FIN_UK-Ireland","Celgene Japan User Build Owner","Global Analytics User Build Owner","FIN_Global UK","FIN_1048","Financial Revenue User","Financial AP User","Financial Owners Hierarchy Super User","FIN_BRAZIL","FIN_CC1113","FPA User Build Owner","FIN_Spain","FIN_Mexico","FIN_Taiwan","Finance FA Super User","Intercompany User","Financial Budget Admin User","Tax User Build Owner","FIN_Australia","Celgene Audit User","FIN_JUNO_Germany","Fixed Assets User Build Owner","FIN_SEA","FIN_Korea","Financial Owners Hierarchy User","Concur User Build Owner","Tax Admin User","FIN_1101","Financial TnE User","FIN_Canada","Couvet Financial User","FIN_Germany","FIN_US AT1-2-6","Financial User Build Owner","FIN_Italy","Financials P2P Super User","FIN_Russia","FIN_1059","Financial GL User","Secondary Ledger User","AP PO User Build Owner","Financial FA_Project User","FIN_Corporate","Financial FA_Project Super User","AR User Build Owner","Financial TnE Super User","FIN_US AT1-6","FIN_Global","FIN_International","FIN_1099","FIN_1149","Financial AP Super User","Financial GL Super User","FIN_US_Canada","FIN_Japan","Revenue User Build Owner","Financial Global Analytics Super User","FIN_US","FIN_France","General Ledger User Build Owner","OM Financial User Build Owner","Financial AR User","Financial AR Super User","Financial Reporting User Build Owner","Treasury User Build Owner","FIN_Spain Portugal","FIN_CNE","FIN_MEX","FIN_EMEA Emerging","FIN_Global Clinical","Financials P2P User","ITFM Build User"]

#Pick Module
def pick_module(e):
    if module_combo.get()=="Manufacturing":
        role_combo.config(value=Manufacturing)
    elif module_combo.get()=="SCOM":
        role_combo.config(value=SCOM)
    elif module_combo.get()=="Finance":
        role_combo.config(value=Finance)


#All Entries
module_label=ttk.Label(entries,text="Select Module:",font=("Calibri Light",12))
module_label.pack(fill='x',expand=True)
module_combo=ttk.Combobox(entries,value=modules)
module_combo.bind("<<ComboboxSelected>>",pick_module)
module_combo.pack(fill='x')

role_label=ttk.Label(entries,text="Select Role:",font=("Calibri Light",12))
role_label.pack(fill='x',expand=True)
role_combo=ttk.Combobox(entries,value=" ")
role_combo.pack(fill='x')

id_label=ttk.Label(entries,text="Enter User ID:",font=("Calibri Light",12))
id_label.pack(fill='x',expand=True)
id_entry=ttk.Entry(entries)
id_entry.pack(fill='x',expand=True)

Name_label=ttk.Label(entries,text="Enter Full Name:",font=("Calibri Light",12))
Name_label.pack(fill='x',expand=True)
Name_entry=ttk.Entry(entries)
Name_entry.pack(fill='x',expand=True)

ritm_label=ttk.Label(entries,text="Enter RITM:",font=("Calibri Light",12))
ritm_label.pack(fill='x',expand=True)
ritm_entry=ttk.Entry(entries)
ritm_entry.pack(fill='x',expand=True)

#All Buttons
add_button=ttk.Button(wrapper,text="Add",command=generator)
add_button.pack(fill='x',expand=True,pady=10)

openfile_button=ttk.Button(wrapper,text="Open File",command=openFile)
openfile_button.pack(fill='x',expand=True,pady=10)

clearfile_button=ttk.Button(wrapper,text="Clear File",command=clearFile)
clearfile_button.pack(fill='x',expand=True,pady=10)

credit_label=ttk.Label(root,text="Created by Rahul Kamble",font=("Calibri",8))
credit_label.pack()

root.mainloop()