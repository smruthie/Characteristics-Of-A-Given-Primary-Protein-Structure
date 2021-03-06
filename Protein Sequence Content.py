# Calculates acidic, basic, hydrophobic, and hydrophilic residues
peptide_sequence = str(input("Enter a peptide sequence: ")) 
acidic_AA = 0
basic_AA = 0
hydrophobic_AA = 0
polar_AA = 0
nonpolar_AA = 0
sequence_list = list(peptide_sequence.upper())
if 'G' in sequence_list:
    G = sequence_list.count('G')
    hydrophobic_AA += G
if 'D' in sequence_list:
    D = sequence_list.count('D')
    acidic_AA += D
if 'E' in sequence_list:
    E = sequence_list.count('E')
    acidic_AA += E
if 'K' in sequence_list:
    K = sequence_list.count('K')
    basic_AA += K
if 'R' in sequence_list:
    R = sequence_list.count('R')
    basic_AA += R
if 'H' in sequence_list:
    H = sequence_list.count('H')
    basic_AA += H
if 'A' in sequence_list:
    A = sequence_list.count('A')
    hydrophobic_AA += A
if 'V' in sequence_list:
    V = sequence_list.count('V')
    hydrophobic_AA += V
if 'L' in sequence_list:
    L = sequence_list.count('L')
    hydrophobic_AA += L
if 'I' in sequence_list:
    I = sequence_list.count('I')
    hydrophobic_AA += I
if 'P' in sequence_list:
    P = sequence_list.count('P')
    hydrophobic_AA += P
if 'F' in sequence_list:
    F = sequence_list.count('F')
    hydrophobic_AA += F
if 'W' in sequence_list:
    W = sequence_list.count('W')
    hydrophobic_AA += W
if 'M' in sequence_list:
    M = sequence_list.count('M')
    hydrophobic_AA += M
hydrophobicity = hydrophobic_AA/len(sequence_list)*100
if 'B' in sequence_list or 'O' in sequence_list or 'J' in sequence_list or 'X' in sequence_list or 'Z' in sequence_list or 'U' in sequence_list:
    print("Imposter(s) Alert!") #prints this if one or more of the letters entered is not an amino acid
else:    
    print("\n", "N -", peptide_sequence.upper(), "- C")
    print("\n", "Length of peptide sequence: ", len(sequence_list), "amino acids")
    print(" Acidic residues: ", acidic_AA/len(sequence_list)*100, "%")
    print(" Basic residues: ", basic_AA/len(sequence_list)*100, "%")
    print(" Hydrophobic: ", hydrophobic_AA/len(sequence_list)*100, "%")
    print(" Hydrophilic: ", 100-hydrophobicity, "%")
    if hydrophobicity > 50:
        print(" This is a hydrophobic peptide!")
    elif hydrophobicity < 50:
        print(" This is a hydrophilic peptide!")
    else:
        print(" This peptide is equally hydrophobic and hydrophilic!")
