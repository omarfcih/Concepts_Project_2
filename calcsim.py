
#*****************************************#
# Project number from sheet: 2                            #
# Project idae is to create a                                   #
# simple GUI calculator that does multiple 	    #
# operations and print result on screen             #
#       --calculator using Tkinter--        	    #
#*****************************************# 



# import everything from tkinter module 
from tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string
        # using the line >>
        # >> expression = ""
        # or set it to the total to continue
        # calculating
        expression = total
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    calc = Tk() 
  
    # set the background colour of GUI window 
    calc.configure(background="black") 
  
    # set the title of GUI window 
    calc.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    calc.geometry("580x360") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(calc, textvariable=equation,
                             font=('arial',20,'normal'), bd=10) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=3, column=0, row=0,
                          ipadx=55, ipady=8) 
  
    equation.set('Enter the full equation') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(calc, text=' 1 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(1), height=1, width=7, 
                     font=('arial',20,'bold')) 
    button1.grid(row=4, column=0) 
  
    button2 = Button(calc, text=' 2 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(2), height=1, width=7,
                     font=('arial',20,'bold')) 
    button2.grid(row=4, column=1) 
  
    button3 = Button(calc, text=' 3 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(3), height=1, width=7,
                     font=('arial',20,'bold')) 
    button3.grid(row=4, column=2) 
  
    button4 = Button(calc, text=' 4 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(4), height=1, width=7,
                     font=('arial',20,'bold')) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(calc, text=' 5 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(5), height=1, width=7,
                     font=('arial',20,'bold')) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(calc, text=' 6 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(6), height=1, width=7,
                     font=('arial',20,'bold')) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(calc, text=' 7 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(7), height=1, width=7,
                     font=('arial',20,'bold')) 
    button7.grid(row=2, column=0) 
  
    button8 = Button(calc, text=' 8 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(8), height=1, width=7,
                     font=('arial',20,'bold')) 
    button8.grid(row=2, column=1) 
  
    button9 = Button(calc, text=' 9 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(9), height=1, width=7,
                     font=('arial',20,'bold')) 
    button9.grid(row=2, column=2) 
  
    button0 = Button(calc, text=' 0 ', fg='black', bg='gray',
                     bd=10, 
                     command=lambda: press(0), height=1, width=7,
                     font=('arial',20,'bold')) 
    button0.grid(row=5, column=0) 
  
    plus = Button(calc, text=' + ', fg='black', bg='blue',
                     bd=10, 
                     command=lambda: press("+"), height=1, width=7,
                     font=('arial',20,'bold')) 
    plus.grid(row=2, column=3) 
  
    minus = Button(calc, text=' - ', fg='black', bg='blue',
                     bd=10, 
                     command=lambda: press("-"), height=1, width=7,
                     font=('arial',20,'bold')) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(calc, text=' * ', fg='black', bg='blue',
                     bd=10, 
                     command=lambda: press("*"), height=1, width=7,
                     font=('arial',20,'bold')) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(calc, text=' / ', fg='black', bg='blue',
                     bd=10, 
                     command=lambda: press("/"), height=1, width=7,
                     font=('arial',20,'bold')) 
    divide.grid(row=5, column=3)
  
    equal = Button(calc, text=' = ', fg='black', bg='blue',
                     bd=10, 
                     command=equalpress, height=1, width=7,
                     font=('arial',20,'bold')) 
    equal.grid(row=5, column=2) 
  
    clear = Button(calc, text='Clear', fg='black', bg='blue',
                     bd=10, 
                     command=clear, height=1, width=7, 
                     font=('arial',20,'bold')) 
    clear.grid(row=0, column=3)
  
    Decimal= Button(calc, text='.', fg='black', bg='gray',
                    bd=10, 
                    command=lambda: press('.'), height=1, width=7,
                    font=('arial',20,'bold')) 
    Decimal.grid(row=5, column=1)
    
    # start the GUI 
    calc.mainloop() 


#---------------------------------------Directed_By-------------------------------------#
#*****************************************************************************************#
# 1- Idea title: Simple Calculator.		                              			#
#                    --------------------------------------						#
# 2- Team mempers:-								#
#                               1st								#
#  -> Name: Omar Hussein Abdallah Ali. عمر حسين عبدالله علي 				#
#  --> ID: 20160257								#
#                               2nd							#
#  -> Name: Ahmad Ali Mohammed. أحمد علي محمد 					#
#  --> ID: 20170051								#
#                               3rd								#
#  -> Name: Amr Mohammed Hasanin Abdo. عمرو محمد حسنين عبده				#
#  --> ID: 20160288								#
#                               4th								#
#  -> Name: Mosaad Mohammed Mosaad Hammodah. مسعد محمد مسعد حموده			#
#  --> ID: 20170527								#
#                               5th								#
#  -> Name: Mohammed Yousif Bendary. محمد يوسف بنداري				#
#  --> ID: 20172481								#
#                               6th								#
#  -> Name: Sameh Refaat Hashim Ali. سامح رفعت هاشم علي                           			#
#  --> ID: 20160178                                                                   				#
#                    --------------------------------------                          					#
# 3- Registration sheet row number: 66                                              				#
#*****************************************************************************************#
