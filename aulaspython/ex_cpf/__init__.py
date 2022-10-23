# /usr/bin/python3
import random
import re


def get_cpf(cpf: str = "602.958.833-80") -> str:
    """Format CPF to remove any format

    Args:
        cpf (str): The cpf to be formated as simple numeric string 
            (default empty)

    Returns:
        str: a string for cpf without any . or -
    """
    
    # Create pattern of REGEX (regular expression)
    pattern = r'-|\.'
    prog = re.compile(pattern)

    # Return what is find and replaced from REGEX over string CPF
    cleaned_cpf = prog.sub(repl='', string=cpf)

    if not validate_cpf(cleaned_cpf):
        raise Exception("CPF is not valid")

    return  f'CPF {cleaned_cpf} is Valid'

def calculate_digit(incomplete_cpf:str, first:bool = True) -> int:
    """Calculate first and second Digits from a CPF
    
    Args:
        incomplete_cpf (str): The cpf to be formated as simple numeric string without verification digits
        first (bool): true to the first digit and false if generating the second one

    Returns:
        str: Msg with verification digit
    """
    valid_digit, calculate_digit = 0, 0

    for idx, digit in enumerate(incomplete_cpf):
        if (first and 10 - idx < 2) or (not first and 11 - idx < 2):
            break
        calculate_digit += int(digit) * (10 - idx)

        print(f'{"First:" if first else "Second:"} {int(digit)} * {10 - idx} = {calculate_digit}')
    
    valid_digit = calculate_digit % 11

    return 11 - valid_digit if valid_digit > 2 else 0

def validate_cpf(cpf:str) -> bool:
    """CPF Validation

    Args:
        cpf (str): The cpf to be formated as simple numeric string 

    Raises:
        Exception: If CPF is not valid

    Returns:
        str: Msg with CPF Validated
    """
    print("""
    VALIDATING
    
    """)
    validating_cpf = str(cpf[:-2])

    first_digit = calculate_digit(validating_cpf,True)
    
    cpf_with_digit = validating_cpf + str(first_digit)
    
    second_digit = calculate_digit(cpf_with_digit,False)

    return cpf == cpf[:-2] + str(first_digit) + str(second_digit)

def generate_cpf() -> str:
    """Generate a New CPF from random seed

    Returns:
        str: Return a valid CPF
    """
    print("""
    GENERATING

    """)
    POSSIBLE_CPF_STRING = ['0','1','2','3','4','5','6','7','8','9']
    incomplete_cpf = ''
    for idx in range(9):
        incomplete_cpf += random.choice(POSSIBLE_CPF_STRING)
        
    first_digit = calculate_digit(incomplete_cpf,True)
    
    cpf_with_digit = incomplete_cpf + str(first_digit)
    
    second_digit = calculate_digit(cpf_with_digit,False)

    return str(incomplete_cpf) + str(first_digit) + str(second_digit)



# Try the default CPF
print(get_cpf())
# Try the generate a new  CPF
print(generate_cpf())
# Try a new generated CPF and validate it
print(get_cpf(generate_cpf()))
