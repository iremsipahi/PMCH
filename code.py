def read_fasta(filename):
    filename += ".fasta"
    fileobj = open(filename, 'r')  #fasta dosyasınun okunması
    sequences = ""  #fasta dosyasının içeriğinin tutulacağı değişken
    for line in fileobj:
        if line.startswith('>'):  #ilk satırın alınmaması için kontrol edilmesi
            continue
        else:
            sequences += line.rstrip()  #her satırın tek bir string olarak birleştirilmesi
    fileobj.close()
    return sequences


def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact


def calculate_possible_match(sequences):
    count_A = sequences.count("A")
    count_U = sequences.count("U")
    count_G = sequences.count("G")
    count_C = sequences.count("C")

    if (count_A == count_U) & (count_G == count_C):
        count_possible = factorial(count_A) * factorial(count_G)
        print("The total possible number of perfect matchings : " + str(count_possible))
    elif (count_A != count_U):
        print("Count of nucleotide A and count of nucleotide U are not equal")
    elif (count_G != count_C):
        print("Count of nucleotide G and count of nucleotide C are not equal")


sequences = read_fasta("Rosalind_23")
print("Sequences: " + sequences)
print("Count A: " + str(sequences.count("A")))
print("Count U: " + str(sequences.count("U")))
print("Count G: " + str(sequences.count("G")))
print("Count C: " + str(sequences.count("C")))

calculate_possible_match(sequences)
