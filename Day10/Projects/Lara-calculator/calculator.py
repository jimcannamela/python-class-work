import user_input
import calculation

def run_calculator_prgm():
    print("\n************************ Welcome to the Calculator! ************************\n")
    
    while True:
        operand1 = user_input.get_float_input()
        operand2 = user_input.get_float_input()
        operation = user_input.get_operator_input()

        ans = str(calculation.perform_calculation(operation, operand1, operand2))
        print('\033[36mThe answer is', ans, "\n\033[0m")
            
        while True:
            try_again_input = input('Would you like to perform another calculation (y/n)? ')
            if try_again_input == 'y' or try_again_input == 'n':
                break
            print('Please enter y or n')
        
        if try_again_input == 'n':
            break
    
    print('\n************************ Goodbye! ************************\n')
            
