def likes(names):
    
    end_line = 'likes this'
    amount_of_elements = len(names)
    
    if amount_of_elements < 2:
        if amount_of_elements == 0:
            return f'no one {end_line}'
        elif amount_of_elements == 1:
            return f'{names[0]} {end_line}'
        
    else:
        end_line = "like this"
        if amount_of_elements == 2:
            return f'{names[0]} and {names[1]} {end_line}'
        elif amount_of_elements == 3:
            return f'{", ".join(names[:2])} and {names[2]} {end_line}'
        else:
            return f'{", ".join(names[:2])} and {amount_of_elements-2} others {end_line}'
        

def likes(names):
    n = len(names)
    
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

if __name__ == '__main__':
    
    # Original Kata: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
    

    print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Lisa']))
