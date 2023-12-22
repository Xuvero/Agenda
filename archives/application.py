from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import sqlite3


class window:

    def database(self):
        ###############Creating the database###############
        self.connect = sqlite3.connect('contactsInfo')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            '''
            create table if not exists info (
                nome varchar(50) not null, 
                sex varchar(15) not null, 
                number int primary key not null, 
                email varchar(50) not null
                );
            '''
        )
        self.connect.commit()
        print('The database works')

    def showInTreeview(self):
        ###############Show the new number in treeview###############
        self.tree.delete(*self.tree.get_children())

        self.data = self.cursor.execute('select * from info order by nome asc')

        for i in self.data:
            self.tree.insert('', END, values=i)

    def entrysGet(self):
        self.name = self.inpName.get()
        self.sex = self.inpSex.get()
        self.number = self.inpNum.get()
        self.email = self.inpMail.get()

    def addTable(self):
        ###############Add a number###############
        self.entrysGet()

        self.cursor.execute(
            '''
            insert into info (nome, sex, number, email) values (?, ?, ?, ?)
            ''', 
                (
                self.name, 
                self.sex, 
                self.number, 
                self.email
                )
            )

        self.showInTreeview()

        self.connect.commit()

    def modifyTable(self):
        ###############Modify something on a existent number###############
        self.entrysGet()

        self.cursor.execute(
            '''
            update info set nome=?, sex=?, email=? where number=?
            ''', 
                (
                self.name, 
                self.sex, 
                self.email,
                self.number 
                )
            )

        self.showInTreeview()
        self.connect.commit()

    def deleteButton(self):
        ###############Delete the user by number###############
        self.entrysGet()
        self.cursor.execute(
            """
            delete from info where number = ?
            """,
            [self.number]
        )

        self.tree.delete(*self.tree.get_children())

        self.data = self.cursor.execute('select * from info order by nome asc')

        for i in self.data:
            self.tree.insert('', END, values=i)

        self.connect.commit()

    def secondDeleteButton(self):
        ###############Delete the user by name###############
        self.entrysGet()
        self.cursor.execute(
            """
            delete from info where nome = ?
            """,
            [self.name]
        )

        self.tree.delete(*self.tree.get_children())

        self.data = self.cursor.execute('select * from info order by nome asc')

        for i in self.data:
            self.tree.insert('', END, values=i)

        self.connect.commit()

    def thirdDeleteButton(self):
        ###############Delete the user by E-mail###############
        self.entrysGet()
        self.cursor.execute(
            """
            delete from info where email = ?
            """,
            [self.email]
        )

        self.tree.delete(*self.tree.get_children())

        self.data = self.cursor.execute('select * from info order by nome asc')

        for i in self.data:
            self.tree.insert('', END, values=i)

        self.connect.commit()

    def treeview(self):
        ###############Treeview###############
        self.tree = ttk.Treeview(self.thirdFrame)

        ###############Columns###############
        self.tree['column'] = ('Nome', 'Sexo', 'Número', 'E-mail')

        ###############Adding Columns###############
        self.tree.column('#0', width=0, minwidth=0, stretch=NO)
        self.tree.column('Nome', anchor=W, width=137, minwidth=137)
        self.tree.column('Sexo', anchor=W, width=137, minwidth=137)
        self.tree.column('Número', anchor=W, width=137, minwidth=137)
        self.tree.column('E-mail', anchor=W, width=137, minwidth=137)

        ###############Adding Headings###############
        self.tree.heading('Nome', text='Nome', anchor=W)
        self.tree.heading('Sexo', text='Sexo', anchor=W)
        self.tree.heading('Número', text='Número', anchor=W)
        self.tree.heading('E-mail', text='E-mail', anchor=W)

        ###############Show treeview###############
        self.tree.place(x=250, y=60, relwidth=0.69, relheight=0.88)

    def searchButton(self):
        ###############Search contacts button###############
        self.treeview()
        self.tree.delete(*self.tree.get_children())

        self.inpSearch.insert(END, '%')
        
        self.search = self.inpSearch.get()
        
        self.cursor.execute(
            """
            select nome, sex, number, email from info where nome like '%s' order by nome asc
            """ 
            % self.search
            )

        self.searchNumber = self.cursor.fetchall()

        for i in self.searchNumber:
            self.tree.insert("", END, values=i)

        self.inpSearch.delete(0, END)

    def seeEveryThing(self):
        ###############Return to the main part###############
        self.inpSearch.delete(0, END)

        self.treeview()
        self.tree.delete(*self.tree.get_children())

        self.inpSearch.insert(END, '%')
        
        self.search = self.inpSearch.get()
        
        self.cursor.execute(
            """
            select nome, sex, number, email from info where nome like '%s' order by nome asc
            """ 
            % self.search
            )

        self.searchNumber = self.cursor.fetchall()

        for i in self.searchNumber:
            self.tree.insert("", END, values=i)

        self.inpSearch.delete(0, END)


    def __init__(self):

        ###############Calling the database###############
        self.database()
        self.connect

        ###############Window configurations###############
        self.win = Tk()
        self.win.title('Agenda')
        self.win.geometry('800x500+250+60')
        self.win.resizable(False, False)

        ###############window icon###############
        self.img = PhotoImage(file='../images/icon.png')
        self.win.iconphoto(False, self.img)

        ###############Colors Palete###############
        self.num1 = '#f0f3f5'  # Darker White
        self.num2 = '#f0f3f5'  # Blue Grey
        self.num3 = '#feffff'  # White
        self.num4 = '#38576b'  # Dark Blue
        self.num5 = '#403d3d'  # Brown
        self.num6 = '#6f9fbd'  # Light Blue
        self.num7 = '#ef5350'  # Red
        self.num8 = '#93cd95'  # Green
        self.num9 = '#a0c8e1'  # Whiter Light Blue
        self.numf = '#ffa6a5'  # Whiter Red
        self.numg = '#b5dfb6'  # Whiter Green

        ###############Frames###############
        self.firstFrame = Frame(self.win, width=800, height=60, relief=FLAT, bg=self.num4).place(x=0, y=0)

        self.secondFrame = Frame(self.win, width=250, height=440, relief=FLAT, bg=self.num2).place(x=0, y=60)

        self.secondInfoFrame = Frame(self.secondFrame, width=250, height=40, relief=FLAT, bg=self.num4).place(x=0, y=340)

        self.thirdFrame = Frame(self.win, width=550, height=440, relief=FLAT, bg=self.num3).place(x=250, y=60)

        ###############Main Mensage of the Frame###############
        self.labTitle = Label(
            self.firstFrame, 
            text='Sua Agenda', 
            font='magion 20 bold', 
            fg=self.num3, 
            bg=self.num4
            ).place(x=300, y=10)

        ###############Secondary Mensage of the Frame###############
        self.labSecTitle = Label(
            self.secondInfoFrame, 
            text='Encontre um Número Mais Rápido', 
            bg=self.num4, 
            fg=self.num3,
            font='gothan 9 bold'
            ).place(x=5, y=350)

        ###############Nome:###############
        self.labName = Label(
        self.secondFrame, text='Nome:', font='magion 10', bg=self.num2).place(x=10, y=95)
        self.inpName = Entry(width=15, font='magion 12', relief=FLAT)
        self.inpName.place(x=80, y=95)
        
        ###############Sex:###############
        self.labSex = Label(self.secondFrame, text='Sexo:', font='magion 10', bg=self.num2).place(x=10, y=145)
        self.inpSex = Combobox(self.secondFrame, width=17, font='magion 10')
        self.inpSex['value'] = ('', 'Masculino', 'Feminino')
        self.inpSex.place(x=80, y=145)

        ###############Number:###############
        self.labNum = Label(self.secondFrame, text='Número:', font='magion 10', bg=self.num2).place(x=10, y=195)
        self.inpNum = Entry(self.secondFrame, width=15, font='magion 12', relief=FLAT)
        self.inpNum.place(x=80, y=195)

        ###############E-mail:###############
        self.labMail = Label(self.secondFrame, text='E-mail:', font='magion 10', bg=self.num2).place(x=10, y=245)
        self.inpMail = Entry(self.secondFrame, width=15, font='magion 12', relief=FLAT)
        self.inpMail.place(x=80, y=245)

        ###############Search:###############
        self.labSearch = Label(self.secondFrame, text='Pesquise:', font='magion 10', bg=self.num2).place(x=10, y=395)
        self.inpSearch = Entry(self.secondFrame, width=15, font='magion 12', relief=FLAT)
        self.inpSearch.place(x=80, y=395)

        ###############Button Search###############
        self.butSearch = Button(
            self.secondFrame, 
            text="Pesquisar", 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num6, 
            activebackground=self.num9, 
            activeforeground=self.num3,
            command=self.searchButton
            ).place(x=10, y=445)

        ###############Button see Everything###############
        self.butShow = Button(
            self.secondFrame, 
            text='Ver todos', 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num6, 
            activebackground=self.num9, 
            activeforeground=self.num3,
            command=self.seeEveryThing
            ).place(x=90, y=445)

        ###############Button Exit###############
        self.butExit = Button(
            self.secondFrame, 
            text='Sair', 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num7, 
            activebackground=self.numf, 
            activeforeground=self.num3, 
            command=quit
            ).place(x=170, y=445)

        ###############Button Update###############
        self.butUpdate = Button(
            self.secondFrame, 
            text='Atualizar', 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num6, 
            activebackground=self.num9, 
            activeforeground=self.num3,
            command=self.modifyTable
            ).place(x=90, y=295)

        ###############Button Add###############
        self.butAdd = Button(
            self.secondFrame, 
            text='Adicionar', 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num8, 
            activebackground=self.numg, 
            activeforeground=self.num3,
            command=self.addTable
            ).place(x=10, y=295)

        ###############Button Delete###############
        self.butDel = Button(
            self.secondFrame, 
            text='Remover', 
            width=5, 
            height=1, 
            relief=FLAT, 
            highlightthickness=0, 
            fg=self.num3, 
            bg=self.num7, 
            activebackground=self.numf, 
            activeforeground=self.num3,
            command=lambda: (self.deleteButton(), self.secondDeleteButton(), self.thirdDeleteButton())
            ).place(x=170, y=295)

        self.treeview()

        #Show treeview info
        self.tree.delete(*self.tree.get_children())

        self.data = self.cursor.execute('select * from info order by nome asc')

        for i in self.data:
            self.tree.insert('', END, values=i)

        self.win.mainloop()


load = window()
