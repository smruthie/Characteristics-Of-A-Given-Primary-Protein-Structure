peptide_sequence = str(input("Enter a peptide sequence: "))
acidic_AA = 0
basic_AA = 0
hydrophobic_AA = 0
sequence_list = list(peptide_sequence.upper())
if 'D' in sequence_list:
    acidic_AA += 1
if 'E' in sequence_list:
    acidic_AA += 1
if 'K' in sequence_list:
    basic_AA += 1
if 'R' in sequence_list:
    basic_AA += 1
if 'H' in sequence_list:
    basic_AA += 1
if 'A' in sequence_list:
    hydrophobic_AA += 1
if 'V' in sequence_list:
    hydrophobic_AA += 1
if 'L' in sequence_list:
    hydrophobic_AA += 1
if 'I' in sequence_list:
    hydrophobic_AA += 1
if 'P' in sequence_list:
    hydrophobic_AA += 1
if 'F' in sequence_list:
    hydrophobic_AA += 1
if 'W' in sequence_list:
    hydrophobic_AA += 1
if 'M' in sequence_list:
    hydrophobic_AA += 1
acidic_residues = acidic_AA/len(sequence_list)*100
basic_residues = basic_AA/len(sequence_list)*100
hydrophobicity = hydrophobic_AA/len(sequence_list)*100
if 'B' in sequence_list or 'O' in sequence_list or 'J' in sequence_list or 'X' in sequence_list or 'Z' in sequence_list or 'U' in sequence_list:
    print("There's an imposter in this sequence!") #prints this if one of the letters entered is not an amino acid
else:    
    print("\n", "N -", peptide_sequence.upper(), "- C")
    print("\n", "Length of peptide sequence: ", len(sequence_list), "amino acids")
    print(" Acidic residues: ", acidic_residues, "%")
    print(" Basic residues: ", basic_residues, "%")
    if hydrophobicity > 50:
        print(" Your peptide is mostly hydrophobic!")
    elif hydrophobicity < 50:
        print(" Your peptide is mostly hydrophilic!")
    else:
        print(" Your peptide is equally hydrophobic and hydrophilic!")
