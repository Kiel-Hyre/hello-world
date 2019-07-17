'''
    Tic Tac Toe dynamic v1 @ Kiel Hyre
    ------------------
    Basic Tic Tac Toe with a twist
    ------------------
    Goal
    ------------------
        Input dynamic size 3 and greater odd numbers
        If 3 :
            Check 3 x or 3 o
        else :
            Check 4 x or 4 o
        Print winner
    ------------------
    Future updates
    ------------------
    fixing + AI
    ------------------
    Imports
    ------------------
        os - for 'cls'
    
'''

import os 

def Mode() :
    
    while True :
        os.system( 'cls' )

        print( '\t\t\t\tWelcome to Tic Tac Toe ')
        print( '''\n\nInstructions :
        Sizes only accepts greater than 1
        If choose 3 goal is to make 3 X's or 3 O's
        More than 3 goal is to make 4 X's or 4 O's
    Checking will done horizontal, vertical or diagonals and print the winner
        \n\n
        ''')
        
        try :
            mode = int( input ( " Size >> " ) )

            if mode < 2 :
                raise ValueError

            else :

                print( f'Your mode size is {mode} \n Preparing...')
                input( "Enter lmao")

                return mode
            
        except ValueError :

            continue

def Setup( mode ) :

    board_main = []

    for i in range( mode ) :
        board_sub = []

        for j in range( mode ) :

            board_sub.append( '-' )

        board_main.append( board_sub )

    return board_main
    
def Board( board_main ) :

    print( '\t' , end = '')
    for i in range( len( board_main ) ) :
        print( i , end = '\t' )
    print( '\n' )
    for i in range( len( board_main ) ) :
        print( i , end = '\t' )
        
        for j in range( len( board_main ) ) :
            print( board_main[i][j] , end = '\t')

        print( '\n' )
    

def Game( board_main , game_state , mode  ) :

    board_dict = {}
    
    while game_state == True :

        os.system( 'cls' )
         
        board_dict = Players( True , mode , board_main )        
        game_state = Check( board_dict['board'] , board_dict['play'] , mode  )

        if game_state == False :
            os.system( 'cls' )
            Board( board_dict['board'] )
            print( "P1 Win" )
            break
        elif game_state == 'Draw' :
            break
        else :
            board_dict = Players( False , mode , board_main )
            game_state = Check( board_dict['board'] , board_dict['play'] , mode )

    if game_state == 'Draw' :
        os.system( 'cls' )
        Board( board_dict['board'])
        print( 'Draw' )
    elif board_dict['play'] == False and game_state == False :
        os.system( 'cls' )
        Board( board_dict['board'])
        print( "P2 Win" )

    input()
    

def Players( player , mode , board_main ) :

    while True :

        os.system( 'cls' )
        Board( board_main )

        if player == True :
            print( '''Player 1's Turn''')
        else :
            print( '''Player 2's Turn''')
            
        try :
            px = int ( input ( " Enter Row >> "))
            py = int ( input( " Enter Column >> "))

            if ( 0 <= px < mode  ) and ( 0 <= py < mode )  :

                if board_main[px][py] != '-' :
                    print( "There was already a piece")
                else :
                    if player == True :
                        board_main[px][py] = 'X'
                    else :
                        board_main[px][py] = 'O'

                    return { 'board' : board_main , 'play' : player }
                
                    break
              
            else :
                raise ValueError

        except ValueError :
            continue

def Check( board_main , player , mode  ) :
    
    # horizontal and vertical
    for i in range( mode ) :
        ctrh = 0
        ctrv = 0 
        for j in range( mode ) :
            if board_main[i][j] == 'X' and player == True :
                ctrh += 1
            elif board_main[i][j] == 'O' and player == False :
                ctrh += 1
            else :
                ctrh = 0
                
            if mode > 3 and  ( ctrh > 3 ):
                return False
            elif mode <= 3 and ( ctrh == mode ) :
                return False
            else :
                state = True
            
        for j in range( mode ) :
            if board_main[j][i] == 'X' and player == True :
                ctrv += 1
            elif board_main[j][i] == 'O' and player == False :
                ctrv += 1
            else :
                ctrv = 0

            if mode > 3 and  ( ctrv > 3 ):
                return False
            elif mode <= 3 and ( ctrv == mode ) :
                return False
            else :
                state = True

    
        
    # diagonal LR RL
    for i in range( mode ) :

        if i == 0 :
            for j in range( mode ) :
                ctrd = 0
                for k in range( mode - j ) :

                    if board_main[k][k + j ] == 'X' and player == True :
                        ctrd += 1
                    elif board_main[k][k + j ] == 'O' and player == False :
                        ctrd += 1
                    else :
                        ctrd = 0

                    if mode > 3 and  ctrd > 3 :
                        return False
                    elif mode <= 3 and ( ctrd == mode ) :
                        return False
                    else :
                        state = True

            for j in range( mode , 0 , -1 ) :
                ctrd1 = 0
                for k in range( j ) :
                    if  board_main[ i + k ][ j - 1 - k ] == 'X' and player == True :
                        ctrd1 += 1
                    elif board_main[ i + k ][ j - 1 - k ] == 'O' and player == False :
                        ctrd1 += 1
                    else :
                        ctrd1 = 0
                    if mode > 3 and ctrd1 > 3 :
                            return False
                    elif mode <= 3 and ctrd1 == mode  :
                            return False
                    else :
                            state = True


        else :

            ctr = mode - i    
            for j in range( ctr ) :
                ctrd = 0
                for k in range( ctr - j ) :
                    if board_main[k+i][k] == 'X' and player == True :
                        ctrd += 1
                    elif board_main[k+i][k] == 'O' and player == False :
                        ctrd +=1
                    else :
                        ctrd = 0
                     
                    if mode > 3 and ctrd > 3 :
                        return False
                    elif mode == 3 and ctrd == 3  :
                        return False
                    else :
                        state = True
                ctr -= 1

            ctr = i - 1
            for j in range( mode - 1 , ctr , -1  ) :
                ctrd1 = 0
                
                for k in range( j - ctr ) :
                    if board_main[ i + k ][ j - k ] == 'X' and player == True :
                        ctrd1 += 1
                    elif board_main[ i + k ][ j - k ] == 'O' and player == False :
                        ctrd1 += 1
                    else :
                        ctrd1 = 0
                    if mode > 3 and ctrd1 > 3 :
                            return False
                    elif mode == 3 and ctrd1 == 3  :
                            return False
                    else :
                            state = True    
                        
                break

    # check if draw

    check_draw = 0
    for i in range( mode ) :
        for j in range( mode ) :
            if board_main[i][j] != '-' :
                check_draw += 1
    if check_draw == mode**2 :
        state = 'Draw'
        
    return state

def main() :

    while True  :        
        board_mode = Mode()
        board_list = Setup( board_mode )
        Game( board_list , True , board_mode )
        
main()
