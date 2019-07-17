'''
TRUTH TABLE 02/22/19
Project made by our group BSCS 1-3

Contributors
Lead and backend design by Vince
Co-designer Earl and Jermaine
UI made by Arnin
Papers lead by Reeya and company

The lines were almost 1400+
This is our first attempt of making a stacks without a knowledge of it.

Table of contents  {}[]()
{0} IMPORTS
{1} GUI function
    [1] OPERATION BUTTON
    [2] VARIABLE BUTTON
    [3] DELETION
    [4] MENU DROP
        (1) HELP
        (2) ABOUT
    [5] SUB MAIN
{2} main Function
    [1] Power
    [2] RemoveDup
    [3] Operate
    [4] Inverse
    [5] Modify
    [6] Error
    [7] Syntax
    [8] SynError
    [9] Elements
    [10] Bits
    [11] Process
    [12] WFF
{3} main
{4} MAIN GUI
'''

# IMPORTS {0}
import re
from tkinter import * 
from tkinter import font

#---- GUI function {1}

# operation button  {1}[1]  Inserts operations at the end 
def operationAND() :

    inpexpr_txtbox.insert( END, "∧")

def operationOR() :

    inpexpr_txtbox.insert( END, "∨")

def operationIMP() :

    inpexpr_txtbox.insert( END, "⇒")

def operationBI() :

    inpexpr_txtbox.insert( END, "⇔")

def operationXOR() :

    inpexpr_txtbox.insert( END, "⊕")

def operationNEG() :

    inpexpr_txtbox.insert( END, "¬")
    
def operationPAR() :

    inpexpr_txtbox.insert( END, "(")

def operationbPAR() :

    inpexpr_txtbox.insert( END, ")")

def operationTAU() :

    inpexpr_txtbox.insert( END, "⊤")

def operationCON() :

    inpexpr_txtbox.insert( END, "⊥")
# -----[]

# variable option {1}[2] Inserts variable at the end

def but_p() :

    inpexpr_txtbox.insert( END, "p")

def but_q() :

    inpexpr_txtbox.insert( END, "q")

def but_r() :

    inpexpr_txtbox.insert( END, "r")

def but_s() :

    inpexpr_txtbox.insert( END, "s")

def but_t() :

    inpexpr_txtbox.insert( END, "t")

def but_u() :

    inpexpr_txtbox.insert( END, "u")

# ---[]

# ---- deletion {1}[3]

def clear() : # deletes all
    
    inpexpr_txtbox.delete( 0, END)

def del_(): # delete last

    exp = expr.get()
    inpexpr_txtbox.delete( len(exp) -1  )

# --- []
# subs ---
# ---- menu drop {1}[4]

def help_() :  #{1}[4](1) shows help 

    root_help = Tk()
    root_help.title(" Truth Help")
    root_help.config( bg = '#FFFFFF')
    help_text = "TRUTH Calculator Help \n\nEnter expression : Input of valid variables and operators given in the operators buttons and in Special Feature \nCAL/Calculate : Initialize the entered input from the textbox\nINITIALIZER: A listbox printing error(s) if there is, else print synchronization and producing truth table\nVARIABLE BUTTONS: Availabled variables in standard ranging from p to u in total of 6 variables. \nOPERATOR BUTTONS: Available operators in standard\n\nAND : ∧ : If p and q are true, then it is true otherwise false \nOR  : ∨ : If one or both are true, then it is true otherwise false\nIMP : ⇒ : If p then q, q is true , then it is true, if both false then true, otherwise false\nBI  : ⇔ : If p == q then it is true, otherwise false.\nXOR : ⊕  : If p is not equal to q then it is ture, otherwise false\nInV : ¬ : If p = true then it is false.\nPar : ( : Provides open parenthesis \nbPar: ) : Provides close parenthesis\nTAU : ⊤ : Special element that only contains true\nCON : ⊥ : Special element that only contains false\nCLR :   : Clear all in the textbox\nDEL :   : Deletes the last element\n\nOptions:\nNatural Option: sort the elements, check then yes \nT/F Option: Display T or F instead of 1 or 0\n\nSpecial Feature:\nVariables: Can input as many variables[letters or words] as the memory can take\nOperations: Can input variation of signs to form an operation symbols\n\nAND &&  ∧ /\ · & and ^\nOR   \/ ∨ ||  + | or\nIMPLIES -> => →  ⊃  ⇒\nBICON   < - >  < = > ⇔ ↔ ≡\nXOR  ( + ) ⊕  ⊻ \nNEGATION - ! ~ not ¬\nTAU 1  T  ⊤\nCON 0  F ⊥\n"
    help_label1 = Label( root_help, text = help_text, justify = 'left', bg = '#d3d3d3').grid( row = 0)

def abt() :  #{1}[4](2) shows about

    root_abt = Tk()
    root_abt.title(" Truth About")

    abt_text = "TRUTH Calculator About\n\nTruth table generator was an application to test given expression in logical statement. Provided the expression was correct, it will generate a table showing the process and corresponding answers\nAside from that it can determine the well formed formula of the process : Tautology / Contradiction / Contigency/\n\nMembers:\nABAD, Miguel\nANETIN,Jasmine\nCANLAS, Jermaine\nCUNTAPAY,Earl\nGLORIANI, Reeya\nISIP,Vince Andrei\nMANDARIO,Lloyd\nMENDOZA, Arnin\n\nSPECIAL THANKS:\nGOD\nCarl Isip\nSir.Martin Figuracion\nBSCS 1-3\n\nTruth table Generator 2018-2019"
    abt_label1 = Label( root_abt, text = abt_text, justify = 'center', bg = '#d3d3d3').grid( row = 0)



def Sub( expr, num_bitraise, process, eval_, wff_ ) : #{1}[5] shows truth table
                
    root_sub = Tk()              
    root_sub.title( "Truth Table")
    root_sub.config( bg = 'white')

    courier = font.Font( family = 'Courier' )
    
    msgsplitexpr = expr.copy()
    msgsplitexpr.remove('#')

    total_len = 0
    
    for i in range( len( process)) :
        total_len += len( process[i])
        
    frame_sub = Frame( root_sub, bg = 'white')
    frame_sub.pack( fill = 'both', expand = True)

    canvas_sub = Canvas( frame_sub, bg = 'white')
 
    xscrollbar = Scrollbar( frame_sub, orient = HORIZONTAL, command = canvas_sub.xview)
    yscrollbar = Scrollbar( frame_sub, orient = VERTICAL, command = canvas_sub.yview)
   
    frame_msub = Frame( canvas_sub)
    
    print_inpexpr_label = Label( frame_msub, font = courier, text = msgsplitexpr, justify = 'center', bg = "#D3D3D3", relief = "ridge",height=2,width = ( 20*len(process) + total_len + len( process) - 1) ).grid( row = 0, columnspan = 1 + len( process))


    for j in range( len ( process) ) :

        if process[j] == process[-1] :
            process_txtbox = Label( frame_msub, font = courier, text = process[j], bg ='#FA8072' , relief = "ridge" )
        else :
            process_txtbox = Label( frame_msub, font = courier, text = process[j], bg = "#03DAC6", relief = "ridge" )
        process_txtbox.grid( row = 1, column = j)
        #process_txtbox.insert( 0, process[j] )
        process_txtbox.config( justify = 'center', width = 20 + len( process[j] ) )

    for k in range( num_bitraise ) :

        for l in range ( len( process) ) :

            if process[l] == process[-1]:
                eval_txtbox = Label( frame_msub, font = courier, text = eval_[k][l], bg = '#fdd8d4', relief = "ridge")
            else:
                eval_txtbox = Label( frame_msub, font = courier, text = eval_[k][l], bg = "white", relief = "ridge")
                
            eval_txtbox.grid( row = 2 + k, column =l )
            eval_txtbox.config( justify = 'center', width = 20 + len( process[l] ) )
    
    wff_msg = WFF( wff_ , num_bitraise, process)

    wff_label = Label( frame_msub, font = courier, text = wff_msg, justify = 'center', bg = "white", width = ( 20*len(process) + total_len + len( process ) - 1) ).grid( row = 2 + num_bitraise, columnspan = 1 + len( process))  

    frame_msub.pack( fill = 'both', expand = True)

    xscrollbar.pack( side = BOTTOM, fill = X)
    yscrollbar.pack( side = RIGHT, fill = Y)
    
    canvas_sub.create_window( (0,0), window = frame_msub, anchor = 'nw')
    canvas_sub.update_idletasks()
  
    canvas_sub.config( yscrollcommand = yscrollbar.set, xscrollcommand = xscrollbar.set, scrollregion = canvas_sub.bbox('all'))

    #canvas_sub.bind("<1>", lambda event: canvas_sub.focus())  
    #canvas_sub.bind("<Left>",  lambda event: canvas_sub.xview_scroll(-1, "units"))
    #canvas_sub.bind("<Right>",  lambda event: canvas_sub.xview_scroll( 1, "units"))
    #canvas_sub.bind("<Down>",  lambda event: canvas_sub.yview_scroll( -1, "units"))
    #canvas_sub.bind("<Up>",  lambda event: canvas_sub.yview_scroll( 1, "units"))

    canvas_sub.pack( fill = 'both', expand = True )

    root_sub.mainloop()

        
        
# ----[][]

# ---- main Function

def Power(base_num ,power_num): # [0](0) exponent # {2}[1] raise number
        
        result = 1
        
        for index in range(power_num):
                
                result = result * base_num
                
        return result

def RemoveDup(oldlist):       # {2}[2] remove duplicates in finprocesslist check ....
        
    sublist = []

    for items in oldlist:

        if items not in sublist:

            sublist.append(items)

    return sublist

def Operate(operation ,var1 ,var2 ,true):  # {2}[3] list of operators functions

        #print(var1,var2)

        if operation == '∨':   #OR

                if var1 == 1 and var2 == 1 or var1 == 'T' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y' :
                                return 'T'
                        else:
                                return 1

                elif var1 == 1 and var2 == 0 or var1 == 'T' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                elif var1 == 0 and var2 == 1 or var1 == 'F' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                        
                elif var1 == 0 and var2 == 0 or var1 == 'F' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
        elif operation == '∧': #AND

                if var1 == 1 and var2 == 1 or var1 == 'T' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y' :
                                return 'T'
                        else:
                                return 1

                elif var1 == 1 and var2 == 0  or var1 == 'T' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y' :
                                return 'F'
                        else:
                                return 0
                elif var1 == 0 and var2 == 1 or var1 == 'F' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
                        
                elif var1 == 0 and var2 == 0 or var1 == 'F' and var2 == 'F':

                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
        elif operation == '⇒': #IMPLICATION

                if var1 == 1 and var2 == 1 or var1 == 'T' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1

                elif var1 == 1 and var2 == 0 or var1 == 'T' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
                elif var1 == 0 and var2 == 1 or var1 == 'F' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                        
                elif var1 == 0 and var2 == 0 or var1 == 'F' and var2 == 'F' :

                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                            
        elif operation == '⇔': #BICON

                if var1 == 1 and var2 == 1 or var1 == 'T' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1

                elif var1 == 1 and var2 == 0 or var1 == 'T' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
                elif var1 == 0 and var2 == 1 or var1 == 'F' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
                        
                elif var1 == 0 and var2 == 0 or var1 == 'F' and var2 == 'F':

                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
        elif operation == '⊕': #XOR

                if var1 == 1 and var2 == 1 or var1 == 'T' and var2 == 'T' :
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0

                elif var1 == 1 and var2 == 0 or var1 == 'T' and var2 == 'F' :
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                elif var1 == 0 and var2 == 1 or var1 == 'F' and var2 == 'T':
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1
                        
                elif var1 == 0 and var2 == 0 or var1 == 'F' and var2 == 'F':

                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0

def Inv(var1,true): # {2}[4] special function for negation
        
        if var1 == 1 or var1 == 'T':
                        
                        if true == 'y' or true == 'Y':
                                return 'F'
                        else:
                                return 0
        else:
                        
                        if true == 'y' or true == 'Y':
                                return 'T'
                        else:
                                return 1

def Modify(exp,expr):  # {2}[5] modify operation into single character

        expr = re.split(r'(\W)', exp)

        while '' in expr:    #remove all character = '' in expr 
            expr.remove('')

        while ' ' in expr:   #remove all character = ' ' in expr
            expr.remove(' ')

        expr.append('#')     #add # in end expr

        for x in range(len(expr)):  #this is for two or more elements special case the -/! = NOT

            if ( expr[x] == '<' and (expr[x+1] == '-' or expr[x+1] == '=') and expr[x+2] == '>'):  #BICon
                    expr[x] = '⇔'
                    expr[x+1] = ''
                    expr[x+2] = ''
                 
            elif ( expr[x] == '-' and expr[x+1] != '>' ): #NOT
                    expr[x] = '¬'
                    
            elif ( expr[x] == '-' or expr[x] == '=' and expr[x+1] == '>' ):  #THEN
                    expr[x] = '⇒'
                    expr[x+1] = ''

            elif ( expr[x] == '\\' and expr[x+1] == '/'): #OR1
                    expr[x] = '∨'
                    expr[x+1] = ''

            elif ( expr[x] == '|' and expr[x+1] == '|'): #OR2
                    expr[x] = '∨'
                    expr[x+1] = ''

            elif ( expr[x] == '&' and expr[x+1] == '&'): #AND1
                    expr[x] = '∧'
                    expr[x+1] = ''

            elif ( expr[x] == '/' and expr[x+1] == '\\'): #AND2
                    expr[x] = '∧'
                    expr[x+1] = ''

            elif ( expr[x] == '(' and expr[x+1] == '+' and expr[x+2] == ')'): #XOR
                    expr[x] = '⊕'
                    expr[x+1] = ''
                    expr[x+2] = ''

    #this is for one element e.g AND = /\ OR = \\/ THEN = -> BICON = <-> XOR/+ = ⊕

            elif ( expr[x] == '→' or expr[x] == '⊃' ):  # THEN2
                    expr[x] = '⇒'

            elif ( expr[x] == '↔' or expr[x] == '≡'): #BICON2
                    expr[x] = '⇔'

            elif ( expr[x] == '~' or expr[x] == '!' or expr[x] == 'not'): #NOT
                    expr[x] = '¬'

            elif ( expr[x] == '·' or expr[x] == '&' or expr[x] == 'and' or expr[x] == '^'): #AND
                     expr[x] = '∧'

            elif ( expr[x] == '+' or expr[x] == '|' or expr[x] == 'or'): #OR
                    expr[x] = '∨'

            elif ( expr[x] == '⊻'): #XOR
                    expr[x] = '⊕'

            elif ( expr[x] == 'T' or expr[x] == '1'): #TAUTOLOGY
                    expr[x] = '⊤'

            elif ( expr[x] == 'F' or expr[x] == '0'): #CONTRADICTION
                    expr[x] = '⊥'

        while '' in expr:   # remove all character '' in expr
            expr.remove('')
            
        return expr

def Error( expr ):  # {2}[6] checking for errors

    errors = 0   # error counter

# [ Check the usage of other special characters = illegal characters   specialchar = ['(',')','⊤','⊥','⊕','∨','∧','¬','⇔','⇒']

    for check in range(len( expr )-1):

            if expr[check] == '(' or expr[check] == ')' or expr[check] == '⊤' or expr[check] == '⊥' or expr[check] == '⊕' or expr[check] == '∨' or expr[check] == '∧' or expr[check] == '¬' or expr[check] == '⇔' or expr[check] == '⇒' :

                    happy = 0 

            elif ( re.match(r'[a-zA-Z0-9]',expr[check]) ): # check if the words in with the range 

                    happy = 0
            else:
                    errors +=1
                            
                    msg = "Error: Illegal use of character in line " + str(check) + ": " + str( expr[check])

                    listbox1.insert( errors, msg)

    # [4](1) Check the correct number of parenthesis

    fbraces = 0  # 1... front parenthesis == (

    bbraces = 0  # 2... end parenthesis == )

    for parent in range(len(expr)-1):

            if expr[parent] == '(':   # 1
                    fbraces+=1

            elif expr[parent] == ')': # 2
                    bbraces+=1

    #print(fbraces,bbraces)

    if fbraces != bbraces:
            
            errors +=1
            listbox1.insert ( errors, "Error: Unequal number of parenthesis. Expected parenthesis in pair ( )" )
    else:
            
            expr.insert(0,'(')
            expr.insert(len(expr)-1,')')


    return errors

def Syntax ( expr ) : #{2}[7] changing expression in synxtaxes words PAR VAR bPAR #

    subexpr = expr.copy()   
        
    for sub in range(len(subexpr)-1):

            if subexpr[sub] == '(':  # ( = PAR  

                    rep = subexpr.index('(')

                    subexpr.remove('(')

                    subexpr.insert(rep, 'PAR')

            elif subexpr[sub] == ')': # ) = bPAR

                    rep = subexpr.index(')')

                    subexpr.remove(')')

                    subexpr.insert(rep, 'bPAR')

            elif ( subexpr[sub] == '⊕' or subexpr[sub] == '∨' or subexpr[sub] == '∧' or subexpr[sub] == '⇔' or subexpr[sub] == '⇒'  ):  

                    rep = subexpr.index(subexpr[sub])

                    subexpr.remove(subexpr[sub])

                    subexpr.insert(rep, 'OP')

            elif subexpr[sub] == '¬':  # - = NEG

                    rep = subexpr.index('¬')

                    subexpr.remove('¬')

                    subexpr.insert(rep, 'NEG')

            elif subexpr[sub] == '#':

                    happy = 0

            elif ( subexpr[sub] == '⊤' or subexpr[sub] == '⊥'): # tau or con = VAR

                    rep = subexpr.index(subexpr[sub])

                    subexpr.remove(subexpr[sub])

                    subexpr.insert(rep, 'VAR')

            else: # rest = VAR
                    rep = subexpr.index(subexpr[sub])

                    subexpr.remove(subexpr[sub])

                    subexpr.insert(rep, 'VAR')

    return subexpr

def SynError ( subexpr, expr , error ): # {2}[8] checking for syntax error

    synerror = error

    for synx in range(len( subexpr)-1): # checks the formation of subexpr

                

                if ( subexpr[synx] == 'VAR' and subexpr[synx+1] == 'VAR'): # ( a b )
                        
                        msg = "Error in char " + str(synx) + " No operator detected between var: " + expr[synx] + " and var: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'OP' and subexpr[synx+1] == 'OP'): # ( -> ->)
                        
                        msg = "Error in char " + str(synx) + " No variables detected between op: " + expr[synx] + " and op: " + expr[synx+1]

                        synerror +=1
                        
                        listbox1.insert( synerror , msg )
                        

                elif ( subexpr[synx] == 'OP' and subexpr[synx+1] == 'bPAR'): #( -> )
                        
                        msg = "Error in char " + str(synx) + " Operator end without a variable op: " + expr[synx] + " and end: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'NEG' and subexpr[synx+1] == 'bPAR'): # ( - )
                        
                        msg = "Error in char " + str(synx) + " Negation end without a variable op: " + expr[synx] + " and end: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )
                        
                elif ( subexpr[synx] == 'NEG' and subexpr[synx+1] == 'OP'): #  ( - -> )
                        
                        msg = "Error in char " + str(synx) + " Negation cannot operate within operator neg: " + expr[synx] + " and op: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )
                        
                elif ( subexpr[synx] == 'PAR' and subexpr[synx+1] == 'bPAR' ): # ( )

                        msg = "Error in char " + str(synx) + " No input given "

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'SP' and subexpr[synx+1] == 'SP'): # ( 1 1 )
                        
                        msg = "Error in char " + str(synx) + " No operator detected between con: " + expr[synx] + " and con: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'SP' and subexpr[synx+1] == 'VAR'): # ( 1 a )
                        
                        msg = "Error in char " + str(synx) + " No operator detected between con: " + expr[synx] + " and var: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'VAR' and subexpr[synx+1] == 'SP'): # ( a 1 )
                        
                        msg = "Error in char " + str(synx) + " No operator detected between var: " + expr[synx] + " and con: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'SP' and subexpr[synx+1] == 'PAR'): # a ( ) 
                        
                        msg = "Error in char " + str(synx) + " Connectives end without operator con: " + expr[synx] + " and end: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'VAR' and subexpr[synx+1] == 'PAR'): # 1 ( )
                        
                        msg = "Error in char " + str(synx) + " Variables end without operator var: " + expr[synx] + " and end: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'VAR' and subexpr[synx+1] == 'NEG'): #  ( a - )
                        
                        msg = "Error in char " + str(synx) + " Variables cannot operate with negation var: " + expr[synx] + " and neg: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )

                elif ( subexpr[synx] == 'SP' and subexpr[synx+1] == 'PAR'): #  ( 1 - )
                        
                        msg = "Error in char " + str(synx) + " Connectives cannot operate with negation con: " + expr[synx] + " and neg: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )
                        
                elif ( subexpr[synx] == 'bPAR' and subexpr[synx+1] == 'PAR'): #  ) (
                        
                        msg = "Error in char " + str(synx) + " No Operands between paren: " + expr[synx] + " and paren: " + expr[synx+1]

                        synerror +=1

                        listbox1.insert( synerror , msg )
                        
    return synerror

def Elements( subexpr, expr , option): # {2}[9] getting the elements in an expression

    processlist = [] # container to collect all elements with syn word of VAR or SP
                
    for bits in range( len( subexpr ) ) : 

            if ( subexpr[bits] == 'VAR' or subexpr[bits] == 'SP') :
                    
                    processlist.append( expr[bits] ) # through subexpr checking VAR, if detected add the element equal to expr to list processlist

            finprolist = RemoveDup( processlist ) # remove duplicated elements and stored to finprolist

    while '⊤' in finprolist : # removes tau from container finprolist
            finprolist.remove('⊤')

    while '⊥' in finprolist : # remove con from container finprolist
            finprolist.remove('⊥') 
            

    if option == 'y' or option == 'Y' : # natural option or not

            happy = 0 

    else:
            
            finprolist = sorted(finprolist,key=str.lower) # sorted

    return finprolist

def Bits( num_elements, num_bitraise ,option ) : #{2}[9] getting bits of each element p q = [[1 1 0 0],[1 0 1 0 ]] 
    
    bitlist_ = []  # container for the corresponding bits for each element
    
    inbitlist_ = [] # container for each bit , resets  to be like a 2d array  bitlist_[inbitlist_]

    process = num_bitraise // 2  # for printing T or F
    
    countprocess = 2         # for how many repetitions err

    for count in range(len(num_elements)):

            for count1 in range(countprocess // 2):

                    for true in range(process):

                            if option == 'y' or option == 'Y':

                                    inbitlist_.append('T')

                            else:
                                    inbitlist_.append(1)

                    for false in range(process):

                            if option == 'y' or option == 'Y':

                                    inbitlist_.append('F')

                            else:

                                    inbitlist_.append(0)
                                    

            bitlist_.append(inbitlist_)
            inbitlist_ = []
            countprocess *= 2
            process = process // 2

    return bitlist_

def Process(subexpr, expr) : #{2}[10] for process label p->q   p q p->q
    
    reexpr = expr.copy() # copy of expr

    resubexpr = subexpr.copy()  # copy of subexpr

    spaces = 1
    disp = 0

    reserved = []
    
    while spaces > 0:  # go to infinite loop until syntax VAR # is satisfied

            for disp in range(len(resubexpr)-1) :
                                                       
                    if not disp:  # so that it will not check PAR in 1st position
                            
                            continue
                    
                    elif (  resubexpr[disp] == 'VAR' and resubexpr[disp-1] == 'PAR' and resubexpr[disp+1] == 'bPAR'): # ( VAR )

                            #e.g ( p ) -> PAR VAR bPAR - > VAR pop pop -> VAR -> print p

                            resubexpr[disp-1] = 'VAR'   

                            resubexpr.pop(disp)
                            resubexpr.pop(disp)

                            reexpr[disp-1] = reexpr[disp] 

                            reexpr.pop(disp)
                            reexpr.pop(disp)

                            break
                    
                    elif ( resubexpr[disp] == 'OP' and resubexpr[disp-1] == 'VAR' and resubexpr[disp+1] == 'VAR' ): # ( P -> Q)

                            #e.g (P->q) -> PAR VAR OP VAR bPAR # -> print (p -> q) -> PAR VAR pop pop bPar #-> PAR VAR bPar -> VAR pop pop -> VAR # -> print (p->q) 

                            #print( "(" , reexpr[disp-1] , reexpr[disp] , reexpr[disp+1] , end = ")<--->")
                            
                            resubexpr[disp-1] = 'VAR'   

                            resubexpr.pop(disp)
                            resubexpr.pop(disp)

                            reexpr[disp-1] = '(' + reexpr[disp-1] + reexpr[disp] + reexpr[disp+1] + ')' 

                            reserved.append(reexpr[disp-1])
                            
                            reexpr.pop(disp)
                            reexpr.pop(disp)

                            break

                    elif ( resubexpr[disp] == 'VAR' and resubexpr[disp-1] == 'NEG'):

                            #e.g -A -> par neg var bpar # -> print -A -> par var pop bpar # -> par var bpar # -> var pop pop -> print (-A)

                            #print( "(" , reexpr[disp-1] , reexpr[disp] , end = ")<--->" )

                            resubexpr[disp-1] = 'VAR'
                            resubexpr.pop(disp)

                            reexpr[disp-1] = '(' + reexpr[disp-1] + reexpr[disp] + ')'

                            reserved.append(reexpr[disp-1])
                            
                            reexpr.pop(disp)
                            
                            break

            if resubexpr[0] == 'VAR' and resubexpr[1] == '#':
                    
                    return reserved
                    
                    break

def WFF( wffcheck , num_bitraise, process ) : # {2}[11] message for wff check
        
    truecount = 0
    
    falsecount = 0

    
    for index in range( len( wffcheck)) :

            if wffcheck[index] == 'T' or wffcheck[index] == 1:
                    truecount += 1

            elif wffcheck[index] == 'F' or wffcheck[index] == 0:
                    falsecount += 1
    
    if truecount == num_bitraise:
            wff = "TAUTOLOGY"

    elif falsecount == num_bitraise:
            wff = "CONTRADICTION"

    else:
            wff = "CONTINGENCY" 

    return wff

# -------

#--- main    
def main( event = None) : #{3} int main()

    expression = expr.get()

    NatuOption = checkvar1.get()

    TFOption = checkvar2.get()

    splitexpr = []

    splitexpr = Modify( expression, splitexpr)

    error = 0

    synerror_ = 0

    listbox1.delete(0, END)

    error = Error ( splitexpr )

    subsplitexpr = Syntax (  splitexpr )

    synerror_ = SynError( subsplitexpr , splitexpr, error )
    
    if ( synerror_ <= 0 ) :

        listbox1.insert( 0, "No error found ")

        listbox1.insert( 1, "Initializing truth table...")

        finprocesslist = []
    
        finprocesslist = Elements( subsplitexpr, splitexpr, NatuOption )

        bitraise = Power( 2 , len( finprocesslist) )

        bitlist= Bits( finprocesslist , bitraise ,TFOption)

        reserved_processlist = []

        reserved_processlist = Process( subsplitexpr, splitexpr)

#--- evaluate -----
        reserved_evallist = []

        reserved_inevallist = []

        disp = 0

        spaces = 1


        wffcheck = [] #container for final answers

        evsplitexpr = splitexpr.copy()  # another copy of splitexpr for evaluation

        evsubsplitexpr = subsplitexpr.copy() # another copy of subsplitexpr for evaluation


        for j in  range( bitraise) :

            for i in range( len( finprocesslist ) ) :

                while finprocesslist[i] in evsplitexpr: # replace correspoding elements with respective bits e.g ( p -> q )  ->  ( 1 -> 0)

                        rem = evsplitexpr.index( finprocesslist[i] )
                        evsplitexpr.remove( finprocesslist[i] )
                        evsplitexpr.insert( rem, bitlist[i][j] )

            while '⊤' in evsplitexpr: # tau to all 1

                    rem = evsplitexpr.index('⊤')
                    evsplitexpr.remove('⊤')
                    if TFOption == 'y' or TFOption == 'Y':
                            evsplitexpr.insert(rem,'T')
                    else:
                            evsplitexpr.insert(rem,1)

            while '⊥' in evsplitexpr: # con to all 0

                    rem = evsplitexpr.index('⊥')
                    evsplitexpr.remove('⊥')
                    if TFOption == 'y' or TFOption == 'Y':
                            evsplitexpr.insert(rem,'F')
                    else:
                            evsplitexpr.insert(rem,0)
            
            while spaces > 0:  #same idea in splitting process but rather evsplit will undergo operations  

                    for disp in range( len(evsubsplitexpr) - 1) :

                            if not disp :

                                    continue

                            elif ( evsubsplitexpr[disp] == 'VAR' and evsubsplitexpr[disp-1] == 'PAR' and evsubsplitexpr[disp+1] == 'bPAR' ):

                                    evsubsplitexpr[disp-1] = 'VAR'

                                    evsubsplitexpr.pop(disp)
                                    evsubsplitexpr.pop(disp)

                                    evsplitexpr[disp-1] = evsplitexpr[disp]
                                    evsplitexpr.pop(disp)
                                    evsplitexpr.pop(disp)

                                    break

                            elif ( evsubsplitexpr[disp] == 'OP' and evsubsplitexpr[disp-1] == 'VAR' and evsubsplitexpr[disp+1] == 'VAR' ) :

                                    evsubsplitexpr[disp-1] = 'VAR'

                                    evsubsplitexpr.pop(disp)
                                    evsubsplitexpr.pop(disp)


                                    evsplitexpr[disp-1] = Operate( evsplitexpr[disp], evsplitexpr[disp-1], evsplitexpr[disp+1], TFOption)

                                    reserved_inevallist.append( evsplitexpr[disp-1])

                                    #print("    ",evsplitexpr[disp-1],end = "     ")

                                    evsplitexpr.pop(disp)
                                    evsplitexpr.pop(disp)

                                    #print("case2",evsplitexpr)

                                    break

                            elif ( evsubsplitexpr[disp] == 'VAR' and evsubsplitexpr[disp-1] == 'NEG') :

                                    evsubsplitexpr[disp-1] = 'VAR'

                                    evsubsplitexpr.pop(disp)

                                    evsplitexpr[disp-1] = Inv(evsplitexpr[disp], TFOption)

                                    evsplitexpr.pop(disp)

                                    reserved_inevallist.append( evsplitexpr[disp-1] )
                    
                                    break


                    if evsubsplitexpr[0] == 'VAR' and evsubsplitexpr[1] == '#':

                            wffcheck.append(evsplitexpr[0]) #collects all final answer
                            
                            break

            reserved_evallist.append( reserved_inevallist)

            reserved_inevallist = []

            evsplitexpr = splitexpr.copy()
            
            evsubsplitexpr = subsplitexpr.copy()
#---- []
            
#---- extend 
            
        finprocesslist.extend( reserved_processlist)
     
        finevallist__ = []
        
        for i in  range(bitraise) :

                finevallist = []

                for j in range( len( bitlist ) ) :

                        finevallist.append( bitlist[j][i] )

                finevallist.extend( reserved_evallist[i] )
 
                finevallist__.append(finevallist)
                        
        Sub( splitexpr, bitraise, finprocesslist, finevallist__, wffcheck)
        
#---- subwindow truth table


#---- []            

    
# ---- MAIN GUI {4}

root = Tk()
root.title( "Truth Calculator")
root.config( bg = '#EEEEEE')
root.resizable(0,0)


#courier = Font( root, family = 'Courier')
#--- menu drop

button_help = Button( root, text = "?", bg = '#1DE9B6' , fg = '#0EA17C', command = help_ , width = 9, height = 3, borderwidth = 0)
button_help.grid( row = 9, column = 7, sticky = W )

button_abt = Button( root, text = "i",  bg = '#1DE9B6' , fg = '#0EA17C', width = 9, height = 3, command = abt, borderwidth = 0 )
button_abt.grid( row = 9, column = 8, sticky = W)


# --- []

# --- textbox ---

#button_spc = Button( root, text = "?", command = spec )
#button_spc.grid( row = 1, sticky = W )

expr = StringVar()
#inpexpr_label = Label( root, text = "Enter expression: ").grid( row = 2, column = 1 )
inpexpr_txtbox = Entry(
    root,
    bg = "#EEEEEE",
    textvariable = expr,
    justify = RIGHT,
    width = 81,
    borderwidth = 0)
inpexpr_txtbox.grid(
    row = 2,
    column = 1,
    columnspan = 9,
    sticky = W)
inpexpr_txtbox.focus()
button_F6= Button(
    root,
    bg = '#EEEEEE',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F6.grid(
    row = 2,
    column = 0,
    sticky = W)

# --- []

# Operation Buttons ---

#oper_label = Label( root, bg = '#FFFFFF', text = "Operations:", width = 29, height = 3, borderwidth = 0).grid( row = 4, column = 5, columnspan = 3)


button_AND = Button(
    root,
    text = "∧",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationAND,
    width = 9,
    height = 3,
    borderwidth = 0)
button_AND.grid(
    row = 6 ,
    column = 3 ,
    sticky = W )

button_OR = Button(
    root,
    text = "∨",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationOR,
    width = 9,
    height = 3,
    borderwidth = 0 )
button_OR.grid(
    row = 6,
    column = 4,
    sticky = W )

button_IMP = Button(
    root,
    text = "⇒",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationIMP,
    width = 9,
    height = 3,
    borderwidth = 0 )
button_IMP.grid(
    row = 6,
    column = 5,
    sticky = W)

button_BI = Button(
    root,
    text = "⇔",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationBI,
    width = 9,
    height = 3,
    borderwidth = 0 )
button_BI.grid(
    row = 7 ,
    column = 3,
    sticky = W)

button_XOR = Button(
    root,
    text = "⊕",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationXOR,
    width = 9,
    height = 3,
    borderwidth = 0)
button_XOR.grid(
    row = 7,
    column = 4,
    sticky = W)

button_NEG = Button(
    root,
    text = "¬",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationNEG,
    width = 9,
    height = 3,
    borderwidth = 0 )
button_NEG.grid(
    row = 7 ,
    column = 5,
    sticky = W)

button_PAR = Button(
    root, text = " ( ",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationPAR,
    width = 9,
    height = 3,
    borderwidth = 0)
button_PAR.grid(
    row = 8 ,
    column = 3,
    sticky = W)

button_bPAR = Button(
    root,
    text = " ) ",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationbPAR,
    width = 9,
    height = 3,
    borderwidth = 0)
button_bPAR.grid(
    row = 8 ,
    column = 4,
    sticky = W)

button_TAU = Button(
    root,
    text = "⊤",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationTAU,
    width = 9,
    height = 3,
    borderwidth = 0)
button_TAU.grid(
    row = 9,
    column = 3,
    sticky = W)

button_CON = Button(
    root,
    text = "⊥",
    bg = '#434343',
    fg = '#FFFFFF',
    command = operationCON,
    width = 9,
    height = 3,
    borderwidth = 0)
button_CON.grid(
    row = 9,
    column = 4,
    sticky = W)
button_F1= Button(
    root,
    bg = '#434343',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F1.grid(
    row = 9,
    column = 5,
    sticky = W)
button_F2= Button(
    root,
    bg = '#434343',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F2.grid(
    row = 8,
    column = 5,
    sticky = W)

#--------[]-----

#------- Printing Options -----------

#option_label = Label( root, bg = '#FFFFFF', text = "Options:" ).grid( row = 9, columnspan = 8, sticky = W )

checkvar1 = StringVar()
checkvar1.set(0)
checkbutton1 = Checkbutton(root,
                           bg = '#121212',
                           fg = '#999999',
                           text = "ORD",
                           variable = checkvar1,
                           width = 9,
                           height = 3,
                           onvalue ='y',
                           offvalue = 0,
                           borderwidth = 0)
checkbutton1.grid(row = 6, column = 0, columnspan = 2)

checkvar2 = StringVar()
checkvar2.set(0)
checkbutton2 = Checkbutton(root, bg = '#121212', fg = '#999999', text = "T/F", variable = checkvar2, onvalue = 'y', width = 9, height = 3, offvalue = 0,borderwidth = 0)
checkbutton2.grid(row = 6, column = 2, columnspan = 1)

#--------------[]

#------ List of errors ---------

#error_label = Label( root,  bg = '#FFFFFF', text = "Initializer:", width = 9, height = 3, borderwidth = 0).grid(row = 4, columnspan = 2, sticky = W)


frame_list = Frame( root, bg = '#121212')
frame_list.grid( row = 7, columnspan = 3 , rowspan = 4)

xscrollbar = Scrollbar( frame_list, orient = HORIZONTAL)
xscrollbar.pack( side = BOTTOM , fill = X)

yscrollbar = Scrollbar( frame_list, orient = VERTICAL)
yscrollbar.pack( side = RIGHT , fill = Y)

listbox1 = Listbox( frame_list, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set, width = 24, height = 8)
listbox1.pack()

xscrollbar.config( command = listbox1.xview)
yscrollbar.config( command = listbox1.yview)


#------[]


#---- bottom buttons ----------
button_calc = Button(
    root,
    text = "=",
    bg = '#636363', fg = '#FFFFFF',
    width = 9,
    height = 3,
    borderwidth = 0,
    command = main)
button_calc.grid( row = 9, column = 6, sticky = W)
root.bind( '<Return>', main)

button_clr = Button( root, text = "CLR", bg = '#636363', fg = '#FFFFFF',  command = clear, width = 9, height = 3, borderwidth = 0 )
button_clr.grid( row = 6, column = 6, sticky = W)

button_del = Button( root, text = "DEL", bg = '#636363' ,fg = '#FFFFFF', command = del_, width = 9, height = 3, borderwidth = 0)
button_del.grid( row = 7, column = 6, sticky = W)
button_F3= Button(
    root,
    bg = '#636363',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F3.grid(
    row = 8,
    column = 6,
    sticky = W)

#--------[] ------
# ---- variable options ----

#var_label = Label( root, bg = '#FFFFFF', text = "Variable:", width = 29, height = 3, borderwidth = 0).grid( row = 1, column = 5, columnspan = 3)

button_p = Button( root, text = "P", bg = '#1DE9B6' , fg = '#0EA17C', command = but_p, width = 9, height = 3, borderwidth = 0)
button_p.grid( row = 6, column = 7, sticky = W )

button_q = Button( root, text = "Q", bg = '#1DE9B6' , fg = '#0EA17C',command = but_q, width = 9, height = 3, borderwidth = 0)
button_q.grid( row = 6, column = 8, sticky = W )

button_r = Button( root, text = "R", bg = '#1DE9B6' , fg = '#0EA17C',command = but_r, width = 9, height = 3, borderwidth = 0)
button_r.grid( row = 7, column = 7, sticky = W )

button_s = Button( root, text = "S", bg = '#1DE9B6' , fg = '#0EA17C',command = but_s, width = 9, height = 3, borderwidth = 0)
button_s.grid( row = 7, column = 8, sticky = W )

button_t = Button( root, text = "T", bg = '#1DE9B6' , fg = '#0EA17C',command = but_t, width = 9, height = 3, borderwidth = 0)
button_t.grid( row = 8, column = 7, sticky = W )

button_u = Button( root, text = "U", bg = '#1DE9B6' , fg = '#0EA17C',command = but_u, width = 9, height = 3, borderwidth = 0)
button_u.grid( row = 8, column = 8, sticky = W  )
'''button_F4= Button(
    root,
    bg = '#1DE9B6',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F4.grid(
    row = 9,
    column = 7,
    sticky = W)

button_F5= Button(
    root,
    bg = '#1DE9B6',
    width = 9,
    height = 3,
    borderwidth = 0,
    state = DISABLED)
button_F5.grid(
    row = 9,
    column = 8,
    sticky = W)
'''

# --- []

#label1 = Label( root, text = "Enter Expression:", bg = '#FFFFFF' ).grid( row = 1 , columnspan = 8, sticky = W)
#label2 = Label( root, text = "sss").grid( row = 3, columnspan = 5)
#label3 = Label( root, bg = '#FFFFFF' ,text = "?: Can enter any var or ops aside from given above. Check Help").grid( row = 10, column = 2, columnspan = 5)

root.mainloop()
