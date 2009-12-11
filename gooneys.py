import os

def level2():
    print "Chunck is at the gate, he needs to somethin to get in what is it.\n"
    print "1) Cries and says let me in."
    print "2) Breacks down the fence."
    print "3) Does the Truffle Shuffle."
    
    option = input() 
    
    if option == 1:
        print "Mouth says Shut up fat ass. This is the wrong answer."
        level2()
     
    elif option == 2:
        print "WTF Chunk your out of the Goonies. This is the wront anwer."
        level2()

    elif option == 3:
        print "HAHAHA. Mouth pulls the trigger, a bowling ball rolls"           
        print "down a track... and all this other stuff that"
        print "opens the gate and lets Chunk in."
        
        
        
        
        
def level1():
    print "Tall guy at the start escapes from prison and meets up"      
    print "with his mom how does he do it.\n"
    
    print "1) He kills off all the gaurds."
        
    print "2) He eats some bad food and pretend to be really sick, the"
    print "	ambulance has to come, but he jumps out of thee"             
    print "	ambulance before it gets to the hospital."
        
    print "3) He pretend to hang himself, when the gaurd comes"
    print "	in he knocks him out and runs out."
    
    option = input()
    
    if option == 1:
        os.system("clear")
        print " Wrong"
        level1()
    elif option == 2:
        os.system("clear")
        print "wrong but close"
        level1()
    elif option == 3:
        print "right"
        level2()
    
        

print "DuDe DO YoU KnoW WhAt the GOONIES is, NO well LETS play!" # start

print "1) Start Game"
print "2) Quit"

option = input()

if option == 1:
    option = 0
    os.system('clear')
    level1()
    
    
    
elif option == 2:
    print "WTF"
    quit()
    
    
    
    
    
