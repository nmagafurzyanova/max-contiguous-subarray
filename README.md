# max-contiguous-subarray

## Compito:
Write a function that finds the contiguous subarray (containing at least one number) which has the largest sum within an array read in input to the function. 

The function should return the sub-array and the corresponding sum.  

Write a unit test for the function.

## Note: 

- Lo script principale è **compitino_python.py**, lanciandolo, ogni volta genera una lista con 5 numeri random nel range da -20 a 20. Stamperà la lista, la somma e la sottolista. 

- Lo script di unit test è **test_compitino.py**. Questo script controlla 4 casi:
 1. Una lista di numeri sia positivi, che negativi 
 2. Una lista che consiste solo di 0 
 3. Una lista che consiste solo di elementi negativi 
 4. Il controllo di Exception se dovesse arrivare una lista vuota (in quanto nella condizione è precisato che deve restituire al meno 1 elemento, e in questo caso la condizione non può essere soddisfatta). 

- Per curiosità personale, ho fatto uno script ausiliare **computational_difficulty.py** che calcola la complessità temporale per essere sicura che l'implementazione scelta non l'ha portato ad una difficoltà maggiore che lineare. 

## Esecuzione dei Test

Per eseguire i test, esegui il seguente comando dal terminale:

```bash
python test_compitino.py  ```

- Eventualmente per fare un test più approfondito, si può eseguire il seguente commando: 

	pytest --doctest-modules --junitxml=test-results.xml --cov=. --cov-report=html

che produrrà 2 output: test-results.xml dove verrà salvato il risultato dei test, e la cartella "htmlcov" che all'interno a sua volta conterrà dei report con coverage dei test effetuati. 

