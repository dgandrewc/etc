from tkinter import *
from tkinter import ttk
import pymysql

conn=pymysql.connect(host='219.249.195.19', port=3306, db='STUDY', user='kim', password='kim123', charset='utf8')
DATABASE=conn.cursor()

window=Tk()
window.title('STUDY RESERVATION SYSTEM')

id=StringVar()
password=StringVar()
Nid=StringVar()
Npassword=StringVar()
Nname=StringVar()
Nphone=StringVar()
Naddress=StringVar()
Nemail=StringVar()
Rdate=StringVar()
Rtime=StringVar()
Rterm=StringVar()
Rper=StringVar()
Rroom=StringVar()
Rbran=StringVar()
Rwho=StringVar()
Aname=StringVar()
Anum=StringVar()
Dname=StringVar()
str1=StringVar()
notmember=1

def UIinit():
    global label1, button1, button2, button3, Ulabel3, Ulabel4, Mlabel5, Mbutton6
    global Mlabel1, Mbutton1, Mbutton2, Mbutton3, Mbutton4, Mbutton5, Mlabel2, Mlabel3, listbox, MCombo1, Mlabel4
    global Ulabel1, Ulabel2, Utxt1, Utxt2, Ubutton1, Ubutton2, Ubutton3, Ubutton4, Ubutton5, Ubutton6, Ubutton7
    global Jlabel1, Jlabel2, Jlabel3, Jlabel4, Jlabel5, Jlabel6, Jtxt1, Jtxt2, Jtxt3, Jtxt4, Jtxt5, Jtxt6, Jbutton
    global Rlabel1, Rlabel2, Rlabel3, Rlabel4, Rlabel5, Rlabel6, Rtxt1, Rtxt2, Rtxt3, Rtxt4, Rtxt5, Rtxt6, Rbutton, Rbutton2
    global Alabel1, Alabel2, Atxt1, Atxt2, Abutton, Dlabel1, Dtxt1, Dbutton1, Dbutton2, Mbutton7

    label1=Label(window, text='Select Mode')
    button1=Button(window, text='Manager Mode', command=ManagerFunc)
    button2=Button(window, text='User Mode', command=UserFunc)
    button3=Button(window, text='Return', command=ResetHome)

    Mlabel1=Label(window, text='Select Job')
    Mlabel2=Label(window, text="User Management")
    Mlabel3=Label(window, text='Branch Management')
    Mlabel4=Label(window, text='Branch Room                                                                       ')
    Mlabel5=Label(window, text='UserNo ID Name Phone addr mail')
    Mbutton1=Button(window, text='Study Room Management', command=StudyRoomManagement)
    Mbutton2=Button(window, text='User Management', command=UserManagement)
    Mbutton3=Button(window, text='Branch Management', command=BranchManagement)
    Mbutton4=Button(window, text='Add Branch', command=AddBranch)
    Mbutton5=Button(window, text='Delete Branch', command=DelBranch)
    Mbutton6=Button(window, text='Search', command=BranchReserve)
    Mbutton7=Button(window, text='Delete', command=MReserveDelete)
    MCombo1=ttk.Combobox(window, textvariable=str1)
    listbox=Listbox(window, width=50, height=20)

    Ulabel1=Label(window, text='      id : ')
    Ulabel2=Label(window, text='password : ')
    Ulabel3=Label(window, text='Choose Room')
    Ulabel4=Label(window, text='ReserveID RoomNo Date Time Term People Branch UserID')
    Utxt1=Entry(window, textvariable=id)
    Utxt2=Entry(window, textvariable=password)
    Ubutton1=Button(window, text='Login', command=Login)
    Ubutton2=Button(window, text='Join', command=join)
    Ubutton3=Button(window, text='Reservation', command=Reserve)
    Ubutton4=Button(window, text='My Reservation', command=MyReserve)
    Ubutton5=Button(window, text='No User', command=NotUserMain)
    Ubutton6=Button(window, text='Reservation Cancel', command=UReserveDelete)
    Ubutton7=Button(window, text='Find Room', command=Reserve)

    Jlabel1=Label(window, text='      id : ')
    Jtxt1=Entry(window, textvariable=Nid)
    Jlabel2=Label(window, text='password : ')
    Jtxt2=Entry(window, textvariable=Npassword)
    Jlabel3=Label(window, text='    name : ')
    Jtxt3=Entry(window, textvariable=Nname)
    Jlabel4=Label(window, text='   phone : ')
    Jtxt4=Entry(window, textvariable=Nphone)
    Jlabel5=Label(window, text=' address : ')
    Jtxt5=Entry(window, textvariable=Naddress)
    Jlabel6=Label(window, text='   email : ')
    Jtxt6=Entry(window, textvariable=Nemail)
    Jbutton=Button(window, text='Join', command=excuteJoin)

    Rlabel1=Label(window, text='   Date : ')
    Rtxt1=Entry(window, textvariable=Rdate)
    Rlabel2=Label(window, text='   Time : ')
    Rtxt2=Entry(window, textvariable=Rtime)
    Rlabel3=Label(window, text='   Term : ')
    Rtxt3=Entry(window, textvariable=Rterm)
    Rlabel4=Label(window, text=' People : ')
    Rtxt4=Entry(window, textvariable=Rper)
    Rlabel5=Label(window, text=' RoomNo : ')
    Rtxt5=Entry(window, textvariable=Rroom)
    Rlabel6=Label(window, text=' Branch : ')
    Rtxt6=Entry(window, textvariable=Rbran)
    Rbutton=Button(window, text='Reservation', command=FindAvailableTime)
    Rbutton2=Button(window, text='Reservation', command=reservating)

    label1.grid(row=0, column=0)
    button1.grid(row=1, column=0)
    button2.grid(row=2, column=0)

    Alabel1=Label(window, text='BranchName : ')
    Alabel2=Label(window, text='NumOfRoom : ')
    Atxt1=Entry(window, textvariable=Aname)
    Atxt2=Entry(window, textvariable=Anum)
    Abutton=Button(window, text='Add', command=Adding)

    Dlabel1=Label(window, text='BranchName : ')
    Dtxt1=Entry(window, textvariable=Dname)
    Dbutton1=Button(window, text='DeleteBranch', command=Deleting)
    Dbutton2=Button(window, text='DeleteUser', command=UserDelete)

def Reset():
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    label1.grid_forget()
    Mbutton1.grid_forget()
    Mbutton2.grid_forget()
    Mbutton3.grid_forget()
    Mbutton4.grid_forget()
    Mbutton5.grid_forget()
    Mbutton6.grid_forget()
    Mbutton7.grid_forget()
    MCombo1.grid_forget()
    Mlabel1.grid_forget()
    Mlabel2.grid_forget()
    Mlabel3.grid_forget()
    Mlabel4.grid_forget()
    Mlabel5.grid_forget()
    listbox.grid_forget()
    listbox.delete(0, 99)
    Ulabel1.grid_forget()
    Ulabel2.grid_forget()
    Ulabel3.grid_forget()
    Ulabel4.grid_forget()
    Utxt1.grid_forget()
    Utxt2.grid_forget()
    Ubutton1.grid_forget()
    Ubutton2.grid_forget()
    Ubutton3.grid_forget()
    Ubutton4.grid_forget()
    Ubutton5.grid_forget()
    Ubutton6.grid_forget()
    Ubutton7.grid_forget()
    Jlabel1.grid_forget()
    Jlabel2.grid_forget()
    Jlabel3.grid_forget()
    Jlabel4.grid_forget()
    Jlabel5.grid_forget()
    Jlabel6.grid_forget()
    Jtxt1.grid_forget()
    Jtxt2.grid_forget()
    Jtxt3.grid_forget()
    Jtxt4.grid_forget()
    Jtxt5.grid_forget()
    Jtxt6.grid_forget()
    Jbutton.grid_forget()
    Rlabel1.grid_forget()
    Rlabel2.grid_forget()
    Rlabel3.grid_forget()
    Rlabel4.grid_forget()
    Rlabel5.grid_forget()
    Rlabel6.grid_forget()
    Rtxt1.grid_forget()
    Rtxt2.grid_forget()
    Rtxt3.grid_forget()
    Rtxt4.grid_forget()
    Rtxt5.grid_forget()
    Rtxt6.grid_forget()
    Rbutton.grid_forget()
    Rbutton2.grid_forget()
    Alabel1.grid_forget()
    Alabel2.grid_forget()
    Atxt1.grid_forget()
    Atxt2.grid_forget()
    Abutton.grid_forget()
    Dlabel1.grid_forget()
    Dtxt1.grid_forget()
    Dbutton1.grid_forget()
    Dbutton2.grid_forget()

def Home():
    label1.grid(row=0, column=0)
    button1.grid(row=1, column=0)
    button2.grid(row=2, column=0)

def ResetHome():
    Reset()
    Home()

def ManagerFunc():
    Reset()
    Mlabel1.grid(row=0, column=0)
    Mbutton1.grid(row=1, column=0)
    Mbutton2.grid(row=2, column=0)
    Mbutton3.grid(row=3, column=0)
    button3.grid(row=4, column=0)

def StudyRoomManagement():
    Reset()
    bbranch=[]
    MCombo1.grid(row=0, column=0)
    DATABASE.execute('SELECT BRANCHNAME FROM BRANCH')
    branchn=DATABASE.fetchall()
    for branch in branchn:
        bbranch.append(branch[0])
    MCombo1['values']=bbranch
    button3.grid(row=2, column=0)
    Mbutton6.grid(row=1, column=0)

def BranchReserve():
    Reset()
    Ulabel4.grid(row=0, column=0)
    DATABASE.execute("SELECT * FROM RESERVATION WHERE BRANCH='"+MCombo1.get()+"'")
    datas=DATABASE.fetchall()
    for data in datas:
        DATE=str(data[2])
        DATE=DATE[0:10]
        DInfo=str(str(data[0])+' '+str(data[1]))+' '+DATE+' '+(str(data[3]))+' '+(str(data[4]))+' '+(str(data[5]))+' '+(data[6]).strip()+' '+(data[7])
        listbox.insert(100, DInfo)
    listbox.grid(row=1, column=0)
    button3.grid(row=3, column=0)
    Mbutton7.grid(row=2, column=0)

def MReserveDelete():
    seltext=listbox.get(listbox.curselection()[0])
    DATABASE.execute('DELETE FROM RESERVATION WHERE RESERVENUM='+seltext[0])
    conn.commit()
    BranchReserve()

def BranchManagement():
    Reset()
    DATABASE.execute('SELECT * FROM BRANCH')
    branches=DATABASE.fetchall()

    Mlabel3.grid(row=0, column=0)
    Mlabel4.grid(row=1, column=0)
    Mbutton4.grid(row=1, column=1)
    Mbutton5.grid(row=2, column=1)
    button3.grid(row=0, column=1)
    
    for branch in branches:
        BInfo=(str(branch[0])).strip()+' '+str(branch[1])
        listbox.insert(100, BInfo)
    listbox.grid(row=2, column=0)

def AddBranch():
    Reset()
    Alabel1.grid(row=0, column=0)
    Atxt1.grid(row=0, column=1)
    Alabel2.grid(row=1, column=0)
    Atxt2.grid(row=1, column=1)
    Abutton.grid(row=2, column=0)

def DelBranch():
    Reset()
    Dlabel1.grid(row=0, column=0)
    Dtxt1.grid(row=0, column=1)
    Dbutton1.grid(row=1, column=1)

def Adding():
    DATABASE.execute("INSERT INTO BRANCH VALUES('"+Aname.get()+"','"+Anum.get()+"')")
    conn.commit()
    BranchManagement()

def Deleting():
    DATABASE.execute("DELETE FROM BRANCH WHERE BRANCHNAME='"+Dname.get()+"'")
    conn.commit()
    BranchManagement()

def UserManagement():
    Reset()
    DATABASE.execute('SELECT * FROM MEMBER')
    Users=DATABASE.fetchall()

    Mlabel2.grid(row=0, column=0)
    Mlabel5.grid(row=1, column=0)
    button3.grid(row=0, column=1)
    Dbutton2.grid(row=1, column=1)

    for User in Users:
        UInfo=(str(User[0])).strip()+' '+(User[1]).strip()+' '+(User[3]).strip()+' '+(User[4]).strip()+' '+(User[5]).strip()+' '+(User[6]).strip()
        listbox.insert(100, UInfo)
    listbox.grid(row=2, column=0)

def UserDelete():
    seltext=listbox.get(ACTIVE)
    DATABASE.execute('DELETE FROM MEMBER WHERE MEMNO='+seltext[0])
    conn.commit()
    UserManagement()

def UserFunc():
    Reset()

    Ulabel1.grid(row=0, column=0)
    Utxt1.grid(row=0, column=1)
    Ulabel2.grid(row=1, column=0)
    Utxt2.grid(row=1, column=1)
    Ubutton1.grid(row=2, column=0)
    Ubutton2.grid(row=2, column=1)
    Ubutton5.grid(row=2, column=2)
    button3.grid(row=2, column=3)

def join():
    Reset()
    Jlabel1.grid(row=0, column=0)
    Jtxt1.grid(row=0, column=1)
    Jlabel2.grid(row=1, column=0)
    Jtxt2.grid(row=1, column=1)
    Jlabel3.grid(row=2, column=0)
    Jtxt3.grid(row=2, column=1)
    Jlabel4.grid(row=3, column=0)
    Jtxt4.grid(row=3, column=1)
    Jlabel5.grid(row=4, column=0)
    Jtxt5.grid(row=4, column=1)
    Jlabel6.grid(row=5, column=0)
    Jtxt6.grid(row=5, column=1)
    Jbutton.grid(row=6, column=0)
    button3.grid(row=6, column=1)

def excuteJoin():
    DATABASE.execute("SELECT ID FROM MEMBER WHERE ID='"+Nid.get()+"'")
    IsExist=DATABASE.fetchone()
    if IsExist is not None:
        Error()

    if Nid.get()=='' or Npassword.get()=='' or Nname.get()=='' or Nphone.get()=='' or Naddress.get()=='' or Nemail.get()=='':
        Error()

    DATABASE.execute("SELECT max(MEMNO) FROM MEMBER")
    num=DATABASE.fetchone()
    if num[0]==None:
        token=0
    else:
        token=num[0]+1

    query="INSERT INTO MEMBER VALUES('"+str(token)+"', '"+Nid.get()+"','"+Npassword.get()+"','"+Nname.get()+"','"+Nphone.get()+"','"+Naddress.get()+"','"+Nemail.get()+"')"
    DATABASE.execute(query)
    conn.commit()
    ResetHome()

def Login():
    Uid=id.get()
    global notmember
    notmember=0
    DATABASE.execute("SELECT passwd FROM MEMBER WHERE id='"+Uid+"'")
    pswd=DATABASE.fetchone()
    if pswd==None:
        Error()
    else:
        UserMain()

def UserMain():
    Reset()
    Ubutton3.grid(row=0, column=0)
    Ubutton4.grid(row=1, column=0)
    button3.grid(row=2, column=0)

def NotUserMain():
    global notmember
    notmember=1
    Reset()
    Ubutton7.grid(row=0, column=0)
    button3.grid(row=1, column=0)

def FindAvailableTime():
    Reset()
    Ulabel3.grid(row=0, column=0)
    UNAVAILROOM=[]
    AVAILROOM=[]

    DATABASE.execute("SELECT ROOMNO, TIM, TERM FROM RESERVATION WHERE DAT='"+Rdate.get()+"' AND BRANCH='"+Rbran.get()+"'")
    TTS=DATABASE.fetchall()

    for i in TTS:
        for j in range(i[1], i[1]+i[2]):
            for k in range(int(Rtime.get()), int(Rtime.get())+int(Rterm.get())):
                if k==j:
                    UNAVAILROOM.append(i[0])
    DATABASE.execute("SELECT NUMOFROOM FROM BRANCH WHERE BRANCHNAME='"+MCombo1.get()+"'")
    NUMOFROOM=DATABASE.fetchall()
    for i in range(1, int(NUMOFROOM[0][0])+1):
        if i not in UNAVAILROOM:
            listbox.insert(100, i)

    listbox.grid(row=1, column=0)
    if notmember==0:
        Rbutton2.grid(row=2, column=1)
    button3.grid(row=1, column=1)


def Reserve():
    Reset()
    bbranch=[]
    Rlabel1.grid(row=0, column=0)
    Rtxt1.grid(row=0, column=1)
    Rlabel2.grid(row=1, column=0)
    Rtxt2.grid(row=1, column=1)
    Rlabel3.grid(row=2, column=0)
    Rtxt3.grid(row=2, column=1)
    Rlabel4.grid(row=3, column=0)
    Rtxt4.grid(row=3, column=1)
    Rlabel6.grid(row=4, column=0)
    MCombo1.grid(row=4, column=1)
    DATABASE.execute('SELECT BRANCHNAME FROM BRANCH')
    branchn=DATABASE.fetchall()
    for branch in branchn:
        bbranch.append(branch[0])
    MCombo1['values']=bbranch
    Rbutton.grid(row=5, column=0)
    button3.grid(row=5, column=1)

def MyReserve():
    Reset()
    Ulabel4.grid(row=0, column=0)
    DATABASE.execute("SELECT * FROM RESERVATION WHERE WHO='"+id.get()+"'")
    datas=DATABASE.fetchall()
    for data in datas:
        DATE=str(data[2])
        DATE=DATE[0:10]
        DInfo=str(str(data[0])+' '+str(data[1]))+' '+DATE+' '+(str(data[3]))+' '+(str(data[4]))+' '+(str(data[5]))+' '+(data[6]).strip()+' '+(data[7]).strip()
        listbox.insert(100, DInfo)
    listbox.grid(row=1, column=0)
    button3.grid(row=0, column=1)
    Ubutton6.grid(row=1, column=1)

def UReserveDelete():
    seltext=listbox.get(listbox.curselection()[0])
    DATABASE.execute('DELETE FROM RESERVATION WHERE RESERVENUM='+seltext[0])
    conn.commit()
    MyReserve()

def reservating():
    Rroom=listbox.get(ACTIVE)
    DATABASE.execute("SELECT max(RESERVENUM) FROM RESERVATION")
    num=DATABASE.fetchone()
    if 8>int(Rtime.get()) or 22<int(Rtime.get())+int(Rterm.get()):
        Error(1)
        UserMain()
    if num[0]==None:
        token=0
    else:
        token=num[0]+1
    query="INSERT INTO RESERVATION VALUES('"+str(token)+"', '"+str(Rroom)+"','"+Rdate.get()+"','"+Rtime.get()+"','"+Rterm.get()+"','"+Rper.get()+"','"+MCombo1.get()+"','"+id.get()+"')"
    DATABASE.execute(query)
    conn.commit()
    UserMain()

def Error(errno=0):
    global Errorwindow
    Errorwindow=Tk()
    Errorwindow.title('STUDY RESERVATION SYSTEM')
    if errno==1:
        Elabe2=Label(Errorwindow, text='Already Exist Time')
        Elabe2.grid(row=0, column=0)
    else:
        Elabel=Label(Errorwindow, text='Wrong password or already Exist')
        Elabel.grid(row=0, column=0)
    Ebutton=Button(Errorwindow, text='Exit', command=Exit)
    Ebutton.grid(row=0, column=1)

def Exit():
    Errorwindow.destroy()
    window.destroy()

def main():
    UIinit()
    Home()

    window.mainloop()

if __name__=='__main__':
    main()
