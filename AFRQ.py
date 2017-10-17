#Problem 65: Counting Disease Carriers
#Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k-th Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.
#Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected individual carries at least one copy of the recessive allele for the k-th factor.

with open('Example65.txt') as f:
    disease = map(float, f.readline().strip().split())

for i in disease:
    print (-i + 2 * i ** 0.5, end= " ")