text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')
numString = text[pos+1:]
num = float(numString)

print(num)
