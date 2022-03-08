pKa_Nt = 8.0 # N-terminal pKa
pKa_Ct = 3.1 # C-terminal pKa


# pKa's of amino acids near N- and C- terminals and side chain pKa's - Source: https://www.chem.ucalgary.ca/courses/351/Carey5th/Ch27/ch27-1-4-2.html
Nt_AA = {'A':9.87, 'R':8.99, 'N':8.72, 'D':9.90, 'C':10.70, 'E':9.47, 'Q':9.13, 'G':9.78, 'H':9.33, 'I':9.76, 'L':9.74, 'K':9.06, 'M':9.28, 'F':9.31, 'P':10.64, 'S':9.21, 'T':9.10, 'W':9.41, 'Y':9.21, 'V':9.74} # N-terminal amino acid pKa's
Ct_AA = {'A':2.35, 'R':1.82, 'N':2.14, 'D':1.99, 'C':1.92, 'E':2.10, 'Q':2.17, 'G':2.35, 'H':1.80, 'I':2.32, 'L':2.33, 'K':2.16, 'M':2.13, 'F':2.20, 'P':1.95, 'S':2.19, 'T':2.09, 'W':2.46, 'Y':2.20, 'V':2.29} # C-terminal amino acid pKa's
R_AA = {'R':12.48, 'D':3.90, 'C':8.37, 'E':4.07, 'H':6.04, 'K':10.54, 'Y':10.46} # side chain amino acid pKa's


with open(input("Enter file name: "), "r") as file:
	for line in file:
		line = line.rstrip('\n')
		if line.startswith('>'):
			del line
		file = file.read()
	AA = [] # appending each amino acid into this list, including \n
	for i in file:
		AA.append(i)
	AA2 = [] # appending only amino acid, without \n
	for i in AA:
		if i != '\n':
			AA2.append(i)
	protein = ''.join(AA2)
	pKas_AA = []
	pKas_AA.append(pKa_Nt) # N-terminal pKa append
	pKas_AA.append(Nt_AA[file[0]]) # N-terminal amino acid pKa append
	for i in protein:
		if i in R_AA:
			pKas_AA.append(R_AA[i]) # side chain amino acid pka appends
	if protein[len(protein)-1] in R_AA:
		del pKas_AA[len(pKas_AA)-1] 
		pKas_AA.append(Ct_AA[protein[len(protein)-1]]) # replace last amino acid side chain pKa with C-terminal pKa
	else:
		pKas_AA.append(Ct_AA[protein[len(protein)-1]]) # C-terminal amino acid pKa append
	pKas_AA.append(pKa_Ct) # C-terminal pKa append
	positive_charges = [Nt_AA['K'], Ct_AA['K'], R_AA['K'], Nt_AA['R'], Ct_AA['R'], R_AA['R'], Nt_AA['H'], Ct_AA['H'], R_AA['H'], pKa_Nt]
	negative_charges = [Nt_AA['D'], Ct_AA['D'], R_AA['D'], Nt_AA['E'], Ct_AA['E'], R_AA['E'], pKa_Ct]
	pH = float(input("Enter pH: "))
	charge = []
	for i in pKas_AA:
		if pH > i and i == pKa_Nt:
			charge.append(-1)
		elif pH < i and i == pKa_Ct:
			charge.append(1)
		elif pH < i and i in positive_charges:
			charge.append(1)
		elif pH > i and i in negative_charges:
			charge.append(-1)
		else:
			charge.append(0)
	pKas_AA.append(pH)
	pKas_AA = sorted(pKas_AA)
	pKa1 = pKas_AA[pKas_AA.index(pH)-1]
	pKa2 = pKas_AA[pKas_AA.index(pH)+1]
	print("protein charge =",sum(charge), "\n")
	if sum(charge) == 0:
		print("isoelectric point =", 0.5*(pKa1+pKa2), "\n")
