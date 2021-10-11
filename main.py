def citire_lista():
    '''

    :return: lista citita
    '''
    l = []
    n = int(input("Introduceti numar de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def toate_elementele_au_semne_alterante(l):
    '''

    :param l: lista in care se verifica conditia
    :return: daca toate elementele au semne alternante
    '''
    a = l[0]
    for i in range(1, len(l)):
        b = l[i]
        if b * a > 0:
            return False
        a = b
    return True


def get_longest_alternating_signs(l):
    '''

    :param l: lista in care se verifica conditia
    :return: secventa maxima de elemente cu semne alternante
    '''
    subsecventa_maxima = []
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if toate_elementele_au_semne_alterante(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_maxima):
                subsecventa_maxima = l[i:j + 1]
    return subsecventa_maxima


def test_get_longest_alternating_signs():
    '''

    :return: eficienta functiei get_longest_alternating_signs
    '''
    assert get_longest_alternating_signs([1, 1, -2]) == [1, -2]
    assert get_longest_alternating_signs([-1, 3, -2, 4]) == [-1, 3, -2, 4]
    assert get_longest_alternating_signs([]) == []


def numar_cu_cifre_prime(a):
    '''

    :param a: numarul dat
    :return: daca numarul este format doar din cifre prime
    '''
    aux = a
    while aux:
        if aux % 10 == 0 or aux % 10 == 1 or aux % 10 == 4 or aux % 10 == 6 or aux % 10 == 8 or aux % 10 == 9:
            return False
        aux = int(aux // 10)
    return True


def toate_elementele_au_toate_cifrele_prime(l):
    '''

    :param l: lista in care se verifica conditia
    :return: daca toate elementele au doar cifre prime
    '''
    for i in l:
        if numar_cu_cifre_prime(i) == False:
            return False
    return True


def get_longest_prime_digits(l):
    '''
    :param l: lista citita
    :return: cea mai lunga secventa de numere formate doar din cifre prime
    '''
    subsecventa_max = []
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if toate_elementele_au_toate_cifrele_prime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_prime_digits():
    '''
    :return: verifica eficienta functiei get_longest_prime_digits
    '''
    assert get_longest_prime_digits([3, 12]) == [3]
    assert get_longest_prime_digits([33, 23, 44, 7]) == [33, 23]
    assert get_longest_prime_digits([]) == []


def toate_numerele_sunt_pare(l):
    for i in l:
        if i % 2 == 1:
            return False
    return True


def get_longest_all_even(l):
    subsecv_maxima = []
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if toate_numerele_sunt_pare(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecv_maxima):
                subsecv_maxima = l[i:j + 1]
    return subsecv_maxima


def test_get_longest_all_even():
    assert get_longest_all_even([12, 14, 3, 7, 8]) == [12, 14]
    assert get_longest_all_even([3, 4, 6, 8]) == [4,6,8]
    assert get_longest_all_even([1,5]) == []


def main():
    test_get_longest_alternating_signs()
    test_get_longest_prime_digits()
    test_get_longest_all_even()
    l = []
    while True:
        print("1.Citire lista.")
        print("2.Determina cea mai lungă subsecvență cu proprietatea ca numerele au semne alternante.")
        print("3.Determina cea mai lungă subsecvență cu proprietatea ca toate numerele sunt formate din cifre prime.")
        print("4.Determina cea mai lungă subsecvență cu proprietatea ca toate numerele sunt pare.")
        print("-1.Inchide Programul.")
        optiune = input("Insereaza un numar: ")
        if optiune == "1":
            l = citire_lista()

        elif optiune == "2":
            print(get_longest_alternating_signs(l))

        elif optiune == "3":
            print(get_longest_prime_digits(l))

        elif optiune == "4":
            print(get_longest_all_even(l))

        elif optiune == "-1":
            print("Inchidere program!")
            break

        else:
            print("Insereaza alt numar: ")


main()
