from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from windows.window import Window

class Help():
  def displayHelp(self, window):
    windowAppearance = Window()

    popUp = Toplevel(window)
    windowAppearance.centerWindow(popUp, 250, 250)
    popUp.title("Help")
    infoLabel = ttk.Label(popUp, text="When adding a person: ", font='bold').pack(anchor=CENTER, pady=15)
    cityInfoLabel = ttk.Label(popUp, text="  • City must be in database:").pack(anchor="nw")
    cityInfoLabel2 = ttk.Label(popUp, text="      • Jonesboro").pack(anchor="nw")
    cityInfoLabel2 = ttk.Label(popUp, text="      • Seattle").pack(anchor="nw")
    cityInfoLabel2 = ttk.Label(popUp, text="      • Providence").pack(anchor="nw")
    cityInfoLabel2 = ttk.Label(popUp, text="      • Canton").pack(anchor="nw")
    cityInfoLabel2 = ttk.Label(popUp, text="      • Wellesley").pack(anchor="nw")
    idInfoLabel = ttk.Label(popUp, text="  • ID must be unique").pack(anchor="nw", pady=10)
  
  def displayHelpSQL(self, window):
    windowAppearance = Window()

    popUp = Toplevel(window)
    for widget in popUp.winfo_children():
          widget.destroy()
    windowAppearance.centerWindow(popUp, 600, 300)
    popUp.title("Help")
    infoLabel = ttk.Label(popUp, text="Operating the SQL Injection window: ", font='bold').pack(anchor=CENTER, pady=15)
    infoLabel1 = ttk.Label(popUp, text="  • Search bar is used to find a nickname of a user in sqlinjectiontable1").pack(anchor="nw")
    infoLabel2 = ttk.Label(popUp, text="  • Try searching 'Robert'").pack(anchor="nw")
    infoLabel3 = ttk.Label(popUp, text="  • Press 'Search' button to try the preloaded SQL Injection").pack(anchor="nw")
    infoLabel4 = ttk.Label(popUp, text="  • Try searching 'Robert' again").pack(anchor="nw")
    infoLabel5 = ttk.Label(popUp, text="  • If you wish to repeat the process, press 'Create sqlinjectiontable1' to create the table again").pack(anchor="nw")
    infoLabel6 = ttk.Label(popUp, text="  • You can verify the deletion by checking pgAdmin 4").pack(anchor="nw")
    infoLabel7 = ttk.Label(popUp, text="';DROP TABLE public.sqlinjectiontable1;--").pack(anchor=CENTER, pady=20)

    nextButton = ttk.Button(popUp, text="Next", style='danger.TButton', command=lambda:Help.displayHelpSQLUnion(Help, window), cursor="hand2").pack(pady=10)

  def displayHelpSQLUnion(self, window):
    windowAppearance = Window()

    popUp = Toplevel(window)
    for widget in popUp.winfo_children():
          widget.destroy()
    windowAppearance.centerWindow(popUp, 600, 250)
    popUp.title("Help")
    infoLabel = ttk.Label(popUp, text="Union Attack: ", font='bold').pack(anchor=CENTER, pady=15)
    infoLabel1 = ttk.Label(popUp, text="  • This search bar again uses a select query").pack(anchor="nw")
    infoLabel2 = ttk.Label(popUp, text="  • First, we test how many columns there are by typing 'ORDER BY 1', then 2 and so on").pack(anchor="nw")
    infoLabel3 = ttk.Label(popUp, text="  • Then we have to use 'UNION' accordingly, because it depends on the number of columns").pack(anchor="nw")
    infoLabel4 = ttk.Label(popUp, text="  • We can guess column names password or username or both, from a table called user").pack(anchor="nw")
    infoLabel5 = ttk.Label(popUp, text="  • We have successfuly retrieved username and password from a database").pack(anchor="nw")
    infoLabel6 = ttk.Label(popUp, text="  • If the website is prone to be injected, then there is a good chance that passwords are not hashed").pack(anchor="nw")
    infoLabel7 = ttk.Label(popUp, text="';DROP TABLE public.sqlinjectiontable1;--").pack(anchor=CENTER, pady=20)

