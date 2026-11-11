# -*- coding: utf-8 -*-
"""
Filename: bifalg_c01_algwarmup.py
Date created: Sat Nov  7 11:45:07 2026
@author: LioHong710
Purpose:
Steps:
    1.
    2.
    3.

"""
v_cholerae_oric = 'atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'
# https://rosalind.info/problems/ba1a/
# BA1A: Compute the Number of Times a Pattern Appears in a Text: 3694
def count_pattern_occurrences(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

# count_pattern_occurrences('GCGCG','GCG')
# count_pattern_occurrences('ACGTACGTACGT', 'CG')
# count_pattern_occurrences('ATGCGCGCGCGTA', 'GCG')
# count_pattern_occurrences('AAAGAGTGTCTGA','AAA')
# count_pattern_occurrences('AGTTTGCCGAAATTT','TTT')
# count_pattern_occurrences('ACTGAGTACTCAGTACTGAGTACTGACTTACT','ACT')
# count_pattern_occurrences('ATCCGATCCCATGCCCATG','CC')


# BA1B: Find the Most Frequent Words in a String: 3798
def find_most_frequent_words(text, pattern_len):
    # Word = k-mer.
    k = pattern_len
    freq_patterns = []
    freq_array = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        freq_array.append(count_pattern_occurrences(text, pattern))
    
    # Find patterns with max frequency.
    freq_max = max(freq_array)
    for i in range(len(text)-k+1):
        if freq_array[i] == freq_max:
            freq_patterns.append(text[i:i+k])
    return set(freq_patterns)

# find_most_frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)
# find_most_frequent_words('TGGACGTTGGCCCAGCTGGTCCCACGTGGT',3)
# find_most_frequent_words('CGTTTTGAACATTTTCAACAAGTTTTGCAACATTTT',4)
# find_most_frequent_words('GTTGGGTTGGAACAACAACAACAACAAGTTGGGTTGG',5)
# find_most_frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)
# find_most_frequent_words('TTCCTCATGCAATTC',3)

# find_most_frequent_words(v_cholerae_oric,3)
# find_most_frequent_words(v_cholerae_oric,4)
# find_most_frequent_words(v_cholerae_oric,5)
# find_most_frequent_words(v_cholerae_oric,6)
# find_most_frequent_words(v_cholerae_oric,7)
# find_most_frequent_words(v_cholerae_oric,8)
# find_most_frequent_words(v_cholerae_oric,9)
# count_pattern_occurrences(v_cholerae_oric,'tga')
# count_pattern_occurrences(v_cholerae_oric,'atga')
# count_pattern_occurrences(v_cholerae_oric,'gatga')
# count_pattern_occurrences(v_cholerae_oric,'tgatc')
# count_pattern_occurrences(v_cholerae_oric,'tgatca')
# count_pattern_occurrences(v_cholerae_oric,'atgatca')
# count_pattern_occurrences(v_cholerae_oric,'atgatcaa')
# count_pattern_occurrences(v_cholerae_oric,'atgatcaag')
# count_pattern_occurrences(v_cholerae_oric,'ctcttgatc')
# count_pattern_occurrences(v_cholerae_oric,'cttgatcat')
# count_pattern_occurrences(v_cholerae_oric,'tcttgatca')


# BA1C: Find the Reverse Complement of a String: 3521
def find_reverse_complement(dna_pattern):
    complement_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([complement_dict[d] for d in dna_pattern[::-1]])


def check_reverse_complement(dna_pattern, rc):
    return rc == find_reverse_complement(dna_pattern)

# check_reverse_complement('AAAACCCGGT', 'ACCGGGTTTT')
# check_reverse_complement('ACACAC', 'GTGTGT')


# BA1D: Find All Occurrences of a Pattern in a String: 3378
def find_all_pattern_occurrences(pattern, genome):
    occurrences = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

# find_all_pattern_occurrences('ATAT','GATATATGCATATACTT')
# find_all_pattern_occurrences('GCAT','AAGCATAAGCATAA')
# find_all_pattern_occurrences('ACAC','TTTTACACTTTTTTGTGTAAAAA')
# find_all_pattern_occurrences('AAA','AAAGAGTAAATTAAATAAACTGA')
# find_all_pattern_occurrences('TTT','GCTTTGCCTTTGCTTTGCTTT')
# find_all_pattern_occurrences('ATA','ATATATA')


# BA1E: Find Patterns Forming Clumps in a String: 3031
def find_patterns_forming_clumps(genome, pattern_len, clump_len, threshold):
    k = pattern_len
    freq_patterns = []
    num_all_words = 4**k
    clumps = [0 for i in range(num_all_words)]
    
    # Initialise the frequency array with the first window.
    text = genome[:clump_len]
    freq_array = gen_freq_array(text, k)
    for i in range(num_all_words):
        if freq_array[i] >= threshold:
            clumps[i] = 1
    
    # Sliding window.
    for i in range(1,len(genome)-clump_len+1):
        pattern_first = genome[i-1:i-1+k]
        index_first = convert_pattern_to_num_recursive(pattern_first)
        freq_array[index_first] -= 1
        
        pattern_last = genome[i+clump_len-k:i+clump_len]
        index_last = convert_pattern_to_num_recursive(pattern_last)
        freq_array[index_last] += 1
        
        if freq_array[index_last] >= threshold:
            # Wrong index leads to undefined behaviour.
            clumps[index_last] = 1
    
    # Find frequent patterns.
    for i in range(num_all_words):
        if clumps[i] == 1:
            freq_patterns.append(convert_num_to_pattern_recursive(i, k))
    
    return freq_patterns


# BA1F: Find a Position in a Genome Minimizing the Skew: 2923
def find_pos_of_minskew(genome):
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    # https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
    indices = [i for i,s in enumerate(skew) if s == min(skew)]
    return indices
    
# find_pos_of_minskew('CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG')
# find_pos_of_minskew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
# find_pos_of_minskew('ACCG')
# find_pos_of_minskew('ACCC')
# find_pos_of_minskew('CCGGGT')
# find_pos_of_minskew('CCGGCCGG')


# BA1G: Compute the Hamming Distance Between Two Strings: 3074
def calc_hamming_distance(string1, string2):
    if len(string1) == len(string2):
        dist = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                dist += 1
        return dist
    else:
        return 'Input strings must be same length.'

# calc_hamming_distance('GGGCCGTTGGT','GGACCGTTGAC')
# calc_hamming_distance('AAAA','TTTT')
# calc_hamming_distance('ACGTACGT','TACGTACG')
# calc_hamming_distance('ACGTACGT','CCCCCCCC')
# calc_hamming_distance('ACGTACG','TGCATGC')


# BA1H: Find All Approximate Occurrences of a Pattern in a String: 2405
def find_all_aprox_pattern_occurrences(pattern, genome, num_mismatch):
    occurrences = []
    for i in range(len(genome)-len(pattern)+1):
        if calc_hamming_distance(genome[i:i+len(pattern)], pattern) <= num_mismatch:
            occurrences.append(i)
    return occurrences

# find_all_aprox_pattern_occurrences('ATTCTGGA','CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC',3)
# find_all_aprox_pattern_occurrences('ATA','CGATCGAGTACCATAAG',1)
# find_all_aprox_pattern_occurrences('AAA','TTTTTTAAATTTTAAATTTTTT',2)
# find_all_aprox_pattern_occurrences('GAGC','GAGCGCTACTTCCCGACGAGCGCTTGA',2)
# find_all_aprox_pattern_occurrences('AATC','CGATGCATTAAATCC',2)
# find_all_aprox_pattern_occurrences('CCC','ACCCGCCCTCCCGGC',1)
# find_all_aprox_pattern_occurrences('TTT','AAAAAA',3)
# find_all_aprox_pattern_occurrences('CCA','CCACCT',0)


# BA1I: Find the Most Frequent Words with Mismatches in a String: 1938
def find_most_frequent_words_with_mismatches(text, pattern_len, num_mismatch):
    k = pattern_len
    d = num_mismatch
    freq_patterns = []
    num_all_words = 4**k
    close = [0 for i in range(num_all_words)]
    freq_array = [0 for i in range(num_all_words)]
    
    # Populate neighbourhood.
    for i in range(len(text)-k+1):
        nhood = gen_dnhood_of_string_recursive(text[i:i+k], d)
        # The list of 1 element is returned as a string instead. Force it to be a list.
        if type(nhood) != list:
            nhood = [nhood]
        for n in nhood:
            index = convert_pattern_to_num_recursive(n)
            close[index] = 1
    
    # Find approximate occurrences of neighbours.
    # Isn't this double mismatch?
    for i in range(num_all_words):
        if close[i] == 1:
            pattern = convert_num_to_pattern_recursive(i, k)
            # # faapo() returns a list of indices where the pattern occurs.
            freq_array[i] = len(find_all_aprox_pattern_occurrences(pattern, text, d))
            # freq_array[i] = len(find_all_pattern_occurrences(pattern, text))
    
    # freq_array = fmfwwm(text, pattern_len, num_mismatch)
    # Find patterns with max frequency.
    freq_max = max(freq_array)
    # for i in range(num_all_words):
    #     if freq_array[i] == freq_max:
    #         pattern = convert_num_to_pattern_recursive(i, k)
    #         freq_patterns.append(pattern)
    # Get indices with list comprehension: https://stackoverflow.com/questions/14864922/in-python-list-comprehension-is-it-possible-to-access-the-item-index
    freq_patterns = [convert_num_to_pattern_recursive(i, k) for i, f in enumerate(freq_array) if f == freq_max]

    return freq_patterns


def fmfwwm(text, pattern_len, num_mismatch):
    k = pattern_len
    d = num_mismatch
    num_all_words = 4**k
    close = [0 for i in range(num_all_words)]
    freq_array = [0 for i in range(num_all_words)]
    
    # Populate neighbourhood.
    for i in range(len(text)-k+1):
        nhood = gen_dnhood_of_string_recursive(text[i:i+k], d)
        # The list of 1 element is returned as a string instead. Force it to be a list.
        if type(nhood) != list:
            nhood = [nhood]
        for n in nhood:
            index = convert_pattern_to_num_recursive(n)
            close[index] = 1
    
    # Find approximate occurrences of neighbours.
    # Isn't this double mismatch?
    for i in range(num_all_words):
        if close[i] == 1:
            pattern = convert_num_to_pattern_recursive(i, k)
            # faapo() returns a list of indices where the pattern occurs.
            freq_array[i] = len(find_all_aprox_pattern_occurrences(pattern, text, d))
            # freq_array[i] = len(find_all_pattern_occurrences(pattern, text))
    return freq_array

# # ATGC ATGT GATG
# find_most_frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1)
# # GG
# find_most_frequent_words_with_mismatches('AGGT',2,1)
# # CC
# find_most_frequent_words_with_mismatches('ACCCT',2,0)
# # AGG GGC GCG CGG
# find_most_frequent_words_with_mismatches('AGGCGG',3,0)


# BA1J: Find Frequent Words with Mismatches and Reverse Complements: 1778
def find_most_frequent_words_with_mismatches_and_revcomp(text, pattern_len, num_mismatch):
    k = pattern_len
    d = num_mismatch
    freq_patterns = []
    num_all_words = 4**k
    close = [0 for i in range(num_all_words)]
    freq_array = [0 for i in range(num_all_words)]
    
    # Populate neighbourhood.
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        nhood = gen_dnhood_of_string_recursive(pattern, d)
        nhood_rc = gen_dnhood_of_string_recursive(find_reverse_complement(pattern), d)
        
        # print(nhood)
        # print(nhood_rc)
        # The list of 1 element is returned as a string instead. Handle the cases.
        if type(nhood) != list and type(nhood_rc) != list:
            nhood = [nhood, nhood_rc]
        elif type(nhood) == list and type(nhood_rc) != list:
            nhood.append(nhood_rc)
        elif type(nhood) != list and type(nhood_rc) == list:
            nhood = [nhood] + nhood_rc
        # elif type(nhood) == list and type(nhood_rc) == list:
        else:
            nhood = nhood + nhood_rc
        nhood = list(set(nhood))

        # print(nhood)
        # print('=====')
        
        # if type(nhood_rc) != list:
        #     nhood_rc = [nhood_rc]
        # print(nhood_rc)
        # for n in nhood_rc:
        for n in nhood:
            index = convert_pattern_to_num_recursive(n)
            close[index] = 1
            # rc_index = convert_pattern_to_num_recursive(find_reverse_complement(n))
            # close[rc_index] = 1
    
    # Find approximate occurrences of neighbours.
    for i in range(num_all_words):
        if close[i] == 1:
            pattern = convert_num_to_pattern_recursive(i, k)
            # Account for RC of text also.
            rc_text = find_reverse_complement(text)
            freq_array[i] = len(find_all_aprox_pattern_occurrences(pattern, text, d)) + len(find_all_aprox_pattern_occurrences(pattern, rc_text, d))
            # freq_array[i] = len(find_all_pattern_occurrences(pattern, text)) + len(find_all_pattern_occurrences(pattern, rc_text))
    
    # Find patterns with max frequency.
    freq_max = max(freq_array)
    freq_patterns = [convert_num_to_pattern_recursive(i, k) for i, f in enumerate(freq_array) if f == freq_max]
    return freq_patterns

# # ['ATGC', 'ATGT', 'GATG']
# find_most_frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1)
# # ['AA', 'AC', 'AG', 'AT', 'CA', 'GA', 'TA']
# find_most_frequent_words_with_mismatches('AAAAAAAAAA',2,1)
# # ['AAGC', 'AATT', 'ACAC', 'ACTG', 'AGAG', 'AGCA', 'AGGT', 'ATCC', 'ATTA', 'CATC', 'CGGC', 'CGTT', 'GGCC', 'GGTA', 'GTTC', 'TCTC', 'TGAC', 'TGTG']
# find_most_frequent_words_with_mismatches('AGTCAGTC',4,2)
# # GGTA
# find_most_frequent_words_with_mismatches('AATTAATTGGTAGGTAGGTA',4,0)
# # ['AAA', 'ACA', 'AGA', 'ATA', 'ATC', 'ATG', 'ATT', 'CTA', 'GTA', 'TTA']
# find_most_frequent_words_with_mismatches('ATA',3,1)
# # AAT
# find_most_frequent_words_with_mismatches('AAT',3,0)
# # GG TG
# find_most_frequent_words_with_mismatches('TAGCG',2,1)

# # Including RC of text and find_all_aprox_pattern_occurrences().
# # 1. ACAT ATGT
# find_most_frequent_words_with_mismatches_and_revcomp('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1)
# # 2. AT TA
# # AAAAAAAAAA & TTTTTTTTTT
# find_most_frequent_words_with_mismatches_and_revcomp('AAAAAAAAAA',2,1)
# # 3. AATT GGCC
# find_most_frequent_words_with_mismatches_and_revcomp('AGTCAGTC',4,2)
# # 4. AATT: Very valuable case that isolates only RC.
# # AATTAATTGGTAGGTAGGTA & TACCTACCTACCAATTAATT
# find_most_frequent_words_with_mismatches_and_revcomp('AATTAATTGGTAGGTAGGTA',4,0)
# # 5. 20 patterns: AAA AAT ACA AGA ATA ATC ATG ATT CAT CTA GAT GTA TAA TAC TAG TAT TCT TGT TTA TTT
# find_most_frequent_words_with_mismatches_and_revcomp('ATA',3,1)
# # 6. AAT ATT: Very valuable case that isolates only RC.
# find_most_frequent_words_with_mismatches_and_revcomp('AAT',3,0)
# # 7. CA CC GG TG
# # TAGCG & CGCTA
# find_most_frequent_words_with_mismatches_and_revcomp('TAGCG',2,1)

# Using reverse complement of pattern only.
# ['ATGC', 'ATGT', 'GATG']
# Correct: AT TA
# ['AATT', 'ACAC', 'ACTG', 'AGAG', 'ATTA', 'CGGC', 'GGCC', 'TCTC', 'TGAC', 'TGTG']
# Correct: AATT
# All 64 combo: AAA AAC AAG AAT ACA ACC ACG ACT AGA AGC AGG AGT ATA ATC ATG ATT CAA CAC CAG CAT CCA CCC CCG CCT CGA CGC CGG CGT CTA CTC CTG CTT GAA GAC GAG GAT GCA GCC GCG GCT GGA GGC GGG GGT GTA GTC GTG GTT TAA TAC TAG TAT TCA TCC TCG TCT TGA TGC TGG TGT TTA TTC TTG TTT
# All 64 combo: AAA AAC AAG AAT ACA ACC ACG ACT AGA AGC AGG AGT ATA ATC ATG ATT CAA CAC CAG CAT CCA CCC CCG CCT CGA CGC CGG CGT CTA CTC CTG CTT GAA GAC GAG GAT GCA GCC GCG GCT GGA GGC GGG GGT GTA GTC GTG GTT TAA TAC TAG TAT TCA TCC TCG TCT TGA TGC TGG TGT TTA TTC TTG TTT
# GG TG

# Including RC of text and find_all_pattern_occurrences().
# CATG
# AA TT
# AGTC GACT
# Correct: AATT
# ATA TAT
# Correct: AAT ATT
# CG GC TA


# BA1K: Generate the Frequency Array of a String: 1554
def gen_freq_array(text, pattern_len):
    k = pattern_len
    freq_array = [0 for i in range(4**k)]
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = convert_pattern_to_num_recursive(pattern)
        freq_array[j] += 1
    return freq_array


def find_most_frequent_words_faster(text, pattern_len):
    k = pattern_len
    freq_patterns = []
    freq_array = gen_freq_array(text, k)
    freq_max = max(freq_array)
    
    # Find patterns with max frequency.
    for i in range(len(freq_array)):
        if freq_array[i] == freq_max:
            pattern = convert_num_to_pattern_recursive(i, k)
            freq_patterns.append(pattern)
    return freq_patterns

# gen_freq_array('ACGCGGCTCTGAAA',2)
# gen_freq_array('GTTGGTGACGTC',1)
# gen_freq_array('ACGCGGCTCTGAAA',2)
# gen_freq_array('AAAAC',2)
# gen_freq_array('TTAAA',2)
# gen_freq_array('AAA',2)


# BA1L: Implement PatternToNumber: 1791
def convert_pattern_to_num_recursive(pattern):
    # '' returns False.
    if not pattern:
        return 0
    symbol_to_num = {'A':0, 'C':1, 'G':2, 'T':3}
    return 4*convert_pattern_to_num(pattern[:-1]) + symbol_to_num[pattern[-1]]


def convert_pattern_to_num(pattern):
    if not pattern:
        return 0
    val = 0
    symbol_to_num = {'A':0, 'C':1, 'G':2, 'T':3}
    rev_pattern = pattern[::-1]
    for i in range(len(pattern)):
        val += symbol_to_num[rev_pattern[i]] * 4**i
    return val

convert_pattern_to_num_recursive('AGT')


# BA1M: Implement NumberToPattern: 1724
def convert_num_to_pattern_recursive(index, pattern_len):
    num_to_symbol = 'ACGT'
    # This will fail if index > 4.
    if pattern_len == 1:
        return num_to_symbol[index]
    symbol = num_to_symbol[index%4]
    prefix_pattern = convert_num_to_pattern_recursive(index//4, pattern_len-1)
    return prefix_pattern + symbol


def convert_num_to_pattern(index, pattern_len):
    num_to_symbol = 'ACGT'
    # This will fail if index > 4.
    if pattern_len == 1:
        return num_to_symbol[index]
    pattern_list = []
    while index:
        pattern_list.append(num_to_symbol[index%4])
        index = index // 4
    # This final check is rather clumsy.
    if not index and len(pattern_list) < pattern_len:
        pattern_list.append('A')
    return ''.join(pattern_list[::-1])


# BA1N: Generate the d-Neighborhood of a String
def gen_immediate_dnhood_of_string(pattern):
    nucleotides = ['A','C','G','T']
    neighbours = [pattern]
    for nt in pattern:
        other_nt = nucleotides[:]
        other_nt.remove(nt)
        for ont in other_nt:
            nb = pattern.replace(nt,ont)
            neighbours.append(nb)
    return neighbours


def gen_dnhood_of_string_iterative(pattern, d):
    neighbours = [pattern]
    for j in range(d):
        for n in neighbours:
            sub_neighbours = gen_immediate_dnhood_of_string(n)
            neighbours = neighbours + sub_neighbours
            neighbours = list(set(neighbours))
    return neighbours


def gen_dnhood_of_string_recursive(pattern, d):
    # Gets all neighbours with Hamming distance <= d
    if d == 0:
        return pattern
    nucleotides = ['A','C','G','T']
    if len(pattern) == 1:
        return nucleotides
    neighbours = []
    suffix_neighbours = gen_dnhood_of_string_recursive(pattern[1:],d)
    for sn in suffix_neighbours:
        # Filter out suffix_neighbours which reach threshold.
        if calc_hamming_distance(pattern[1:], sn) < d:
            for nt in nucleotides:
                neighbours.append(nt + sn)
        else:
            neighbours.append(pattern[0] + sn)
    # # To get neighbours with Hamming distance = d, filter again.
    # neighbours = [n for n in neighbours if calc_hamming_distance(pattern, n) == d]
    return neighbours


def gen_dnhood_of_string_bruteforce(pattern, d):
    # I also used a spreadsheet to generate neighbours for counting.
    neighbours = [convert_num_to_pattern_recursive(i, len(pattern)) for i in range(4**len(pattern))]
    neighbours = [n for n in neighbours if calc_hamming_distance(pattern, n) <= d]
    return neighbours

# gen_dnhood_of_string_iterative('ACG',2) # 34
# gen_dnhood_of_string_recursive('ACG',2) # 37, which matches manual calc
# gen_dnhood_of_string_recursive('TACG',2)
# gen_dnhood_of_string_recursive('TACG',3)
