import big_o
from compitino_python import max_contiguous_subarray

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(max_contiguous_subarray, positive_int_generator, n_measures=20)
print(best)