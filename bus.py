from tkinter import *
from tkinter import ttk,messagebox
import random
import webbrowser as wb
from gtts import gTTS
import playsound

def gs():
    f=gTTS(text="You booked the ticket Successfully",lang='en')
    f.save("book.mp3")
    playsound.playsound("book.mp3")



def root_func():
    wb.open("https://www.google.co.in/maps/dir/Gushkara+Bus+Terminal,+Guskara+-+Dignagar+Rd,+Guskhara,+West+Bengal+713128/Asansol+Bus+Stand,+Bus+Stand,+Asansol+-+Chittaranjan+Road,+Munshi+Bazar,+Asansol,+West+Bengal/@23.584373,87.0750837,10z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x39f9cef3b689f1c5:0x7735f8090db1092d!2m2!1d87.7439611!2d23.489362!1m5!1m1!1s0x39f71fa9837a0b73:0xec05534d4daa9c74!2m2!1d86.9698595!2d23.6877957!3e0")
    messagebox.showinfo("Root","The Bus root is Guskara To Asansol Via Durapur ")
def ticket_function():
    name=name_entry.get()
    c1=com1.get()
    c2=com2.get()
    m=meal.get()
    t=time.get()
    print(name,c1,c2,t,m)
    a=tuple(range(1,9))

    b=tuple(range(10,34))

    c=tuple(range(35,70))
    d=tuple(range(10,90))

    p=random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)

    root1=['Guskara','dharapara','deripur','gonna','keutola','anadabazar']
    root2=['abhirampur','valki','jamtara',]
    root3=['panaghar','rajbandh','muchipara']
    s=seat.get()
    se=int(s)

    final="ticket number"+str(p)
    if c1 in root1 and c2 in 'Durgapur':
        news=se*70
        prc.set(news)

        messagebox.showinfo("Amount",f"You Have To Pay{news}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
    elif c1==c2:
        messagebox.showerror("Error","Please select The Right Place")
        
    elif c1 in root2 and c2 in 'Durgapur':
        news1=se*50
        prc.set(news1)
        messagebox.showinfo("Amount",f"You Have To Pay{news1}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        

    elif c1 in 'mankar' and c2 in 'Durgapur':
        news2=se*35
        prc.set(news2)
        messagebox.showinfo("Amount",f"You Have To Pay{news2}")
       
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
    elif c1 in root3 and c2 in 'Durgapur':
        news3=se*37
        prc.set(news3)
        messagebox.showinfo("Amount",f"You Have To Pay{news3}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in 'budbud' and c2 in 'Durgapur':
        news4=se*40
        prc.set(news4)
        messagebox.showinfo("Amount",f"You Have To Pay{news4}")
        
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
    elif c1 in root1 and c2 in 'Asansol':
        news5=se*170
        prc.set(news5)
        messagebox.showinfo("Amount",f"You Have To Pay{news5}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
    elif c1 in root2 and c2 in 'Asansol':
        news6=se*150
        prc.set(news6)
        messagebox.showinfo("Amount",f"You Have To Pay{news6}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
       
    elif c1 in root3 and c2 in 'Asansol':
        news7=se*130
        prc.set(news7)
        messagebox.showinfo("Amount",f"You Have To Pay{news7}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        

        
    elif c1 in 'mankar' and c2 in 'Asansol':
        news8=se*140
        prc.set(news8)
        messagebox.showinfo("Amount",f"You Have To Pay{news8}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in 'mankar' and c2 in 'budbud':
        news9=se*10
        prc.set(news9)
        messagebox.showinfo("Amount",f"You Have To Pay{news9}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in root1 and c2 in root1:
        news11=se*10
        prc.set(news11)
        messagebox.showinfo("Amount",f"You Have To Pay{news11}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
       
    elif c1 in root1 and c2 in root2:
        news12=se*20
        prc.set(news12)
        messagebox.showinfo("Amount",f"You Have To Pay{news12}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
       
    elif c1 in root1 and c2 in root3:
        news13=se*30
        prc.set(news13)
        messagebox.showinfo("Amount",f"You Have To Pay{news13}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in root2 and c2 in root3:
        news14=se*20
        prc.set(news14)
        messagebox.showinfo("Amount",f"You Have To Pay{news14}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in root1 and c2 in 'mankar':
        news15=se*30
        prc.set(news15)
        messagebox.showinfo("Amount",f"You Have To Pay{news15}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
       
    elif c1 in root2 and c2 in 'mankar':
        news16=se*15
        prc.set(news16)
        messagebox.showinfo("Amount",f"You Have To Pay{news16}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        
    elif c1 in root1 and c2 in 'budbud':
        news17=se*25
        prc.set(news17)
        messagebox.showinfo("Amount",f"You Have To Pay{news17}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
       

    elif c1 in root2 and c2 in 'budbud':
        news18=se*15
        prc.set(news18)
        messagebox.showinfo("Amount",f"You Have To Pay{news18}")
        messagebox.showinfo("Booked",f"Your ticket number is:{p}")
        n.set("")
        
        

    elif c1 in "Durgapur" and c2 in "Asansol":
        news19=se*100
        prc.set(news19)
        messagebox.showinfo("Amount",f"You Have To Pay{news19}")
        messagebox.showinfo("Booked",f"Your ticket numberis:{p}") 
        n.set("")

    
    else:
        news191=se*10
        prc.set(news191)

        prc.set(news191)
        messagebox.shoinfo("Amount",f"You Have To Pay{10}")
        n.set("")
        
    
    
    with open('booked.txt','a') as bk:
        bk.write(f"Name:{name}\n")
        bk.write(f'destination is from {c1} to {c2}\n')
        bk.write(f'time is:{t}\n')
        bk.write(f'meal Prefarence:{m}\n')
        bk.write(f"Ticket number is:{final}\n")
        bk.write("___________________________________\n")


    
   

    






root=Tk()
root.geometry("333x433")
root.config(bg="whitesmoke")
root.title("Suraj Travels")
root.iconbitmap("Fasticon-Happy-Bus-Bus-red.ico")

heading=Label(root,text="Welcome To Suraj Travels",bg="green",font=('arial',19))
heading.pack(fill=BOTH)

bus_image=PhotoImage(file="bus.png")
bus_label=Label(root,image=bus_image)
bus_label.pack()
frm=Label(root,text="From:")
frm.place(x=20,y=160)
com1=ttk.Combobox(state='readonly',width=12)
com1['values']=('Guskara','dharapara','deripur','gonna','keutola','anadabazar','abhirampur','valki','jamtara','mankar','budbud','panaghar','rajbandh','muchipara','Durgapur','Asansol',)
com1.current(0)
com1.place(x=20,y=180)

to=Label(root,text="To:")
to.place(x=220,y=160)
com2=ttk.Combobox(state='readonly',width=12)
com2['values']=('Guskara','dharapara','deripur','gonna','keutola','anadabazar','abhirampur','valki','jamtara','mankar','budbud','panaghar','rajbandh','muchipara','Durgapur','Asansol',)
com2.current(14)
com2.place(x=220,y=180)
book=ttk.Button(root,text=" Check The Root",command=root_func)
book.place(x=120,y=180)

form=Label(root,text=" Please Fill The Form CareFully",font=("lucida",15,'bold'),bg='blue')
form.place(x=10,y=210,)
n=StringVar()
name_lable=Label(text='Enter The Collecter Name:-',font=("lucida",10,'bold','underline'),)
name_lable.place(x=10,y=250)
name_entry=Entry(width=27,font=("lucida",10,'bold'),textvariable=n)
name_entry.focus()
name_entry.place(x=190,y=250)

name_lable=Label(text='Select The Seat Number :-',font=("lucida",10,'bold','underline'))
name_lable.place(x=10,y=280)
seat=ttk.Combobox(state='readonly')
seat['values']=tuple(range(1,15))
seat.current(0)
seat.place(x=190,y=280)
time=ttk.Combobox(state="readonly")
time_lable=Label(text="Select Your Time:-",font=("lucida",10,'bold','underline'))
time_lable.place(x=10,y=310)
time['values']=(5.41,6.01,6.15,6.35,6.50,7.15,7.31,7.51,8.01,8.15,8.45,9.11,9.35,10.01,11.01,11.30,12.11,13.31,14.01,14.31,15.01,15.15,15.41,16.01,16.34,17.01,18.01,19.31,19.01,20.01,21.01,22.01)
time.current(9)
time.place(x=190,y=310)
meal=StringVar()
meal_lable=Label(text="Do You Want A Meal:-",font=("lucida",10,'bold','underline'))
meal_lable.place(x=10,y=340)

meal_t=ttk.Radiobutton(root,text='Yes',value='Yes',variable=meal,)
meal_t.place(x=190,y=340)

meal_t1=ttk.Radiobutton(root,text='No',value='No',variable=meal,)
meal_t1.place(x=250,y=340)
prc=StringVar()
price=Entry(root,font=("lucida",15,'bold'),textvariable=prc,state ='readonly')
price.place(x=50,y=370)

book_ticket=ttk.Button(text='Book the Ticket',width=45,command=ticket_function)
book_ticket.place(x=30,y=410)


root.mainloop()


