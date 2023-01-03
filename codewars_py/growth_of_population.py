def nb_year(p0, percent, aug, p):
    """

    Args:
        p0 (int): population
        percent (float): percentage increase in population
        aug (int): newcomer
        p (int): top face

    Returns:
        int: year
    """
    year = 0
    while p0 < p:
        p0 +=  int(p0 * (percent / 100) + aug)
        year += 1
        
    return year

if __name__ == '__main__':
    
    # Original Kata: https://www.codewars.com/kata/563b662a59afc2b5120000c6

    print(nb_year(1500, 5, 100, 5000))
