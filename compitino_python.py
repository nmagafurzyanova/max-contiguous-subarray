import random
from typing import List, Tuple

def max_contiguous_subarray(numbers: List[int]) -> Tuple[int, List[int]]:


    ''' 
        Funzione che dato una lista dei numeri in input, restituisce una sotto-lista dei numeri che insieme fanno la somma maggiore tra tutti i numeri della lista. La sotto-lista consiste da numeri consecutivi.
        
        Input: lista non vuota dei numeri 
        Output: somma della sotto-lista e la sotto-lista
    '''
    
    # Controllo che la lista non sia vuota:
    if len(numbers) == 0:
        raise TypeError("Please, ensure the list has at least one element")
        
    # Algoritmo: 
    # parto da -inf, così l'algoritmo è valido anche per le liste di tutti i numeri negativi. Poi creo una variabile temp, che è zero, che sarà aggiornata iterando sui numeri della lista, eventualmente sommandoli tra di loro. Le altre tre variabili sono i contatori per gli elementi della lista, che servono per restituire la sottolista (cioè, servono per delimitare l'inizio e la fine della sottolista).     
    to_start_with = float("-inf")
    temp_sum = 0
    start = 0
    end = 0
    el = 0

    for i, num in enumerate(numbers):

        temp_sum += numbers[i]

        # Aggiorniamo il valore massimo e gli indici se troviamo una somma maggiore.
        if to_start_with < temp_sum:
            to_start_with = temp_sum
            start = el
            end = i
        
        # Reset della somma temporanea se diventa negativa.
        if temp_sum < 0:
            temp_sum = 0
            el = i+1
    return (to_start_with, numbers[start:end+1])


if __name__ == '__main__':

    numbers = random.sample(range(-20, 20), 5)
    somma, subarray = max_contiguous_subarray(numbers)
    print("Lista in input: ", numbers)
    print("La somma: ",somma)
    print("La sottolista: ", subarray)

