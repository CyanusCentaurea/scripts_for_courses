"""
Calculation of disjoining (genotype and phenotype) in the first generation

Sample Input:
Aa Aa

Sample Output:
Parent 1 gametes:
A
a
Parent 1 gametes:
A
a

F1:
AA
Aa
Aa
aa

F1 disjoining (genotype):
AA 1
aa 1
Aa 2

F1 disjoining (phenotype):
A 3
a 1
"""

import itertools


p1 = {}
p2 = {}
p1_input, p2_input = input("Parent genotypes separated by a space:\n").split()

# for parent p1 genotype
q = 0
for i in range(int(len(p1_input) / 2)):
    p1[i] = p1_input[q], p1_input[q + 1]
    q += 2

# for parent p2 genotype
q = 0
for i in range(int(len(p2_input) / 2)):
    p2[i] = p2_input[q], p2_input[q + 1]
    q += 2
    
# work with gametes
character = (int(len(p1_input) / 2))
p1_gametes = [[0 for j in range(len(p1))] for i in range(2**len(p1))]  # blank for the matrix of gametes of the parent p1
p2_gametes = [[0 for j in range(len(p2))] for i in range(2**len(p2))]  # blank for the matrix of gametes of the parent p1
j_gamete_index = []  # list to further fill in the j-index matrix of each allele
j_gamete_index_matrix = [[0 for j in range(len(p1))] for i in range(2**len(p1))]  # blank for j-index matrix of each allele
i_gamete_index_matrix = [[0 for j in range(len(p1))] for i in range(2**len(p1))] # blank for i-index matrix of each allele

# filling the i-index matrix of each allele
q = 0
for i in range(2**len(p1)):
    for j in range(len(p1)):
        i_gamete_index_matrix[i][j] += q
        q += 1
        if q > len(p1) - 1:
            q = 0

# preparing a list for further filling in the j-index matrix of each allele
for i in itertools.product(*[range(0, 2) for k in range(len(p1))]):
    j_gamete_index.append(i)

# translating this list into the j-index matrix of each allele
for i in range(2**len(p1)):
    for j in range(len(p1)):
        j_gamete_index_matrix[i][j] = j_gamete_index[i][j]

# filling the matrices of gametes of parents p1 and p2, respectively
for i in range(2**len(p1)):
    for j in range(len(p1)):
        p1_gametes[i][j] = p1[i_gamete_index_matrix[i][j]][j_gamete_index_matrix[i][j]]
for i in range(2**len(p2)):
    for j in range(len(p2)):
        p2_gametes[i][j] = p2[i_gamete_index_matrix[i][j]][j_gamete_index_matrix[i][j]]

# gametes output
print('Parent 1 gametes:')
for gamete in p1_gametes:
    print(*gamete, sep='')

print('Parent 1 gametes:')
for i in range(2 ** character):
    for j in range(character):
        print(p2_gametes[i][j], end='')
    print()
print() 

# work with offspring (F1)
f = [['' for j in range(character)] for i in range(2 ** character)]
f1 = []
f_output = []
genotype = ''
phenotype = ''
for q in range(2 ** character):
    for i in range(2 ** character):
        for j in range(character):
            if p2_gametes[q][j].isupper():
                f[i][j] = p2_gametes[q][j] + p1_gametes[i][j]
            else:
                f[i][j] = p1_gametes[i][j] + p2_gametes[q][j]
    for i in range(2 ** character):
        for j in range(character):
            genotype = genotype + f[i][j]
        f1.append(genotype)
        f.append(f1)
        f1 = []
        genotype = ''
f = f[2 ** character:]
for i in range(len(f)):
    f_output.append(f[i][0])
print('F1:', *f_output, sep='\n')
print()
types_of_genotype = set()
types_of_phenotype = set()
for i in range(len(f_output)):
    types_of_genotype.add(f_output[i])
print('F1 disjoining (genotype):')
for i in types_of_genotype:
    print(i, f_output.count(i))
    for j in range(0, 2 * character, 2):
        phenotype = phenotype + i[j]
    types_of_phenotype.add(phenotype)
    phenotype = ''
print()
print('F1 disjoining (phenotype):')
all_phenotypes_in_genotype = ''
for i in f_output:
    for j in range(0, 2 * character, 2):
        all_phenotypes_in_genotype = all_phenotypes_in_genotype + i[j]
for i in types_of_phenotype:
    print(i, all_phenotypes_in_genotype.count(i))
