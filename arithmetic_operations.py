num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, division): ")
def perform_operation(add, subtract, multiply, division):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Unsupported operation!"                                                                                 
                                                    
                                                                                            
                                                             
                               
                                
                                       
                                
                                      
                               
                                    
                             
                                                   
                   
                                    
                   
                                                       
