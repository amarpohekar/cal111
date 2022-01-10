'''
@File  : main.py
@brief : This is application file
'''
import logical
import arithmatic
import bitwise
import comparitive

if __name__=="__main__":
    
    print('''
            Greeting!...
          Calculator switching on....''')
    while True == 1:
        option = int(input('''Select from the below operation
                 1> Arithmatic
                 2> Bitwise
                 3> Logical 
                 4> Comparitive
                 5> Exit
                  : '''))

        if option == 1:
            while True:
                option2 = int(input('''Select the following operation from below
                          1> Addition
                          2> Substraction
                          3> Multiplication
                          4> Division
                          5> Modulus
                          6> Go to upper menu
                          : '''))
                if option2 == 1:
                    a = int(input("Enter a 1st number: "))
                    b = int(input("Enter a 2nd number: "))
                    arithmatic.add(a,b)
                
                if option2 == 2:
                    a = int(input("Enter a 1st number: "))
                    b = int(input("Enter a 2nd number: "))
                    arithmatic.sub(a,b)
                    
                if option2 == 3:
                    a = int(input("Enter a 1st number: "))
                    b = int(input("Enter a 2nd number: "))
                    arithmatic.multiply(a,b)
                    
                if option2 == 4:
                    a = int(input("Enter a 1st number: "))
                    b = int(input("Enter a 2nd number: "))
                    arithmatic.divide(a,b)
                    
                if option2 == 5:
                    a = int(input("Enter a 1st number: "))
                    b = int(input("Enter a 2nd number: "))
                    arithmatic.modulus(a,b)
                    
                if option2 == 6:
                    break
        
        if option == 2:
            while True:
                option3 = int(input('''Select On of the below bitwise Operation
                        1> And
                        2> Or
                        3> Not
                        4> Xor
                        5> Bitwise Right Shift
                        6> Bitwise Left Shift
                        7> Go to upper menu
                        : '''))
                if option3 == 1:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    bitwise.and_bitwise(x,y)
                    
                if option3 == 2:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    bitwise.or_bitwise(x,y)
                    
                if option3 == 3:
                    x = int(input("Enter the 1st number: "))                               
                    bitwise.not_bitwise(x)
               
                if option3 == 4:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    bitwise.xor_bitwise(x,y)
                    
                if option3 == 5:
                    x = int(input("Enter the 1st number: "))                               
                    bitwise.rightshift_bitwise(x)
                
                if option3 == 6:
                    x = int(input("Enter the 1st number: ")) 
                    bitwise.leftshift_bitwise(x)
                    
                if option3 == 7:
                    break
        
        if option == 3:
            while True:
                option4 = int(input('''Select the following option from bellow
                              1> And
                              2> Or
                              3> Not
                              4> Go to upper menu      
                                : '''))                  
                
                if option4 == 1:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    logical.and_logical(x,y)
                    
                if option4 == 2:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    logical.or_logical(x,y)
                    
                if option4 == 3:
                    x = int(input("Enter the 1st number: "))                               
                    y = int(input("Enter the 2nd number: "))
                    logical.not_logical(x,y)
                    
                if option4 == 4:
                    break
        
        if option == 4:
            while True:
                option5 = int(input('''Select the following option from bellow
                             1> Equal
                             2> Not Equal                  
                             3> Greater than             
                             4> Less than                 
                             5> Graeter than and equal to  
                             6> Less than and equal to
                             7> go to upper menu                
                            : '''))  
                
                if option5 == 1:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: "))
                     comparitive.equal(x,y)
                     
                if option5 == 2:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: "))
                     comparitive.notequal(x,y)
                     
                if option5 == 3:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: "))
                     comparitive.greaterthan(x,y)
                     
                if option5 == 4:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: ")) 
                     comparitive.lessthan(x,y)
              
                if option5 == 5:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: ")) 
                     comparitive.greaterequal(x,y)
                     
                if option5 == 6:
                     x = int(input("Enter the 1st number: "))                               
                     y = int(input("Enter the 2nd number: ")) 
                     comparitive.lessereuqal(x,y)
                if option5 == 7:
                    break
                       
        if option == 5:
            exit()        
                                          
                                           
                          
                            
                    