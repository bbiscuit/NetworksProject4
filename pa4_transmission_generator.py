
C1 = [1,1,-1,1]
C2 = [-1,1,-1,-1]

M1 = "HELLO"
M2 = "OYEAH"

ENCODING_MAP = {"A" : [1,1,1,1,1], \
                "B" : [1,1,1,1,-1], \
                "C" : [1,1,1,-1,1], \
                "D" : [1,1,1,-1,-1], \
                "E" : [1,1,-1,1,1], \
                "F" : [1,1,-1,1,-1], \
                "G" : [1,1,-1,-1,1], \
                "H" : [1,1,-1,-1,-1], \
                "I" : [1,-1,1,1,1], \
                "J" : [1,-1,1,1,-1], \
                "K" : [1,-1,1,-1,1], \
                "L" : [1,-1,1,-1,-1], \
                "M" : [1,-1,-1,1,1], \
                "N" : [1,-1,-1,1,-1], \
                "O" : [1,-1,-1,-1,1], \
                "P" : [1,-1,-1,-1,-1], \
                "Q" : [-1,1,1,1,1], \
                "R" : [-1,1,1,1,-1], \
                "S" : [-1,1,1,-1,1], \
                "T" : [-1,1,1,-1,-1], \
                "U" : [-1,1,-1,1,1], \
                "V" : [-1,1,-1,1,-1], \
                "W" : [-1,1,-1,-1,1], \
                "X" : [-1,1,-1,-1,-1], \
                "Y" : [-1,-1,1,1,1], \
                "Z" : [-1,-1,1,1,-1], \
                " " : [-1,-1,1,-1,1], \
                "," : [-1,-1,1,-1,-1], \
                "." : [-1,-1,-1,1,1], \
                "'" : [-1,-1,-1,1,-1], \
                "?" : [-1,-1,-1,-1,1], \
                "!" : [-1,-1,-1,-1,-1]}

def dotProduct(v1, v2) -> int:
	"""Finds the dot-product of the two given vectors."""

	if not len(v1) == len(v2):
		raise Exception(f'Vector lengths were not the same. len(v1) = {len(v1)}, len(v2) = {len(v2)}')

	outp = 0
	for i in range(0, len(v1)):
		outp += v1[i] * v2[i]

	return outp

def encodeStringToCDMA(stringInput, cdmaCode) :
    stringEncodedCDMA = [] # The result list.
    for letter in stringInput : # For each letter in the given string...
        letterEncoding = ENCODING_MAP[letter] # Encode to a list of values
        letterEncodedSignal = [] 
        for letterBit in letterEncoding : # For each value in the encoding, scale by every code in the chipping sequence
            letterEncodedCDMASignal = [] 
            for cdmaBit in cdmaCode : # For every bit in what I think is the chipping sequence
                letterEncodedCDMASignal.append(letterBit*cdmaBit) # Encode the encoding value by multiplying by the chipping sequence.
            letterEncodedSignal.append(letterEncodedCDMASignal)
        stringEncodedCDMA.append(letterEncodedSignal) # Append the finally encoded signal.
    return stringEncodedCDMA
    
def decodeTransmission(combinedTras, code):
    """Gets the transmission in the combined transmission with the given code. Assumes that the combined transmission has already been
    split into sections the same length as the code."""
    
    # ALGORITHM:
    # 1. Dot-product each section by the code.
    # 2. Interpret positive dot-products as 1s, and negative dot-products as 0s, and return the
    # transmission.
    
    result = []
    
    # 1. Dot-product each by the code.
    
    for x in combinedTrans:
        result.append(dotProduct(x, code))
    
    print(result)
    
    # 2. Interpret positive dot-products as 1s, and negative dot-products as 0s, and return the
    # transmission.

def addTransmissions(t1, t2) :
    # this simple method only works for same length strings
    if(len(t1)!=len(t2)) : return 0 # Guard clause
    sumOfTransmissions = [] # The output list: the two transmission values added together.
    for letter in range(len(t1)) : # for every index in transmission 1...
        letterEncodedSignal = [] 
        for letterBit in range(len(t1[letter])) : # For every bit in the asci-encoded character...
            letterEncodedCDMASignal = []
            for cdmaBit in range(len(t1[letter][letterBit])) :
                letterEncodedCDMASignal.append(t1[letter][letterBit][cdmaBit] + t2[letter][letterBit][cdmaBit])
            letterEncodedSignal.append(letterEncodedCDMASignal)
        sumOfTransmissions.append(letterEncodedSignal)
    return sumOfTransmissions

def outputRawTransmission(t, f) :
    output = ""
    for letter in range(len(t)) :
        for letterBit in range(len(t[letter])) :
            for cdmaBit in range(len(t[letter][letterBit])) :
                output += str(t[letter][letterBit][cdmaBit]) + ","
    # remove the trailing comma
    print(output[:-1])
    f.write(output[:-1])
     
trans1 = encodeStringToCDMA(M1,C1)
trans2 = encodeStringToCDMA(M2,C2)

combinedTrans = addTransmissions(trans1, trans2)

decodeTransmission(combinedTrans, C1)
      
outfile = open('transmission.txt', 'w')
outputRawTransmission(combinedTrans, outfile)
outfile.close()

