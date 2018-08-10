'''Catalan numbers are a sequence of natural numbers that occurs
in many interesting counting problems like following.
    1) Count the number of expressions containing n pairs of parentheses
       which are correctly matched.
       For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

    2) Count the number of possible Binary Search Trees with n keys (See this)

    3) Count the number of full binary trees
       (A rooted binary tree is full if every vertex has either two children
       or no children) with n+1 leaves.
'''


def nth_catalan_number(number):
    '''
    :param number: the nth number
    :return: demanding catalan number
    '''
    if number <= 1:
        return 1

    new_n = number - 1
    ret = 0
    for i in range(number):
        ret += nth_catalan_number(i) * nth_catalan_number(new_n - i)

    return ret

if __name__ == '__main__':
    for idx in range(10):
        print('{0}: {1}'.format(idx, nth_catalan_number(idx)))
