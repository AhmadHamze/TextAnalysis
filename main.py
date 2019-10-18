import time
sentence = "Once upon a time, there was a quite long sentence which served for testing reasons!"

alphabet = [chr(i) for i in range(65,91)]
start = time.perf_counter()

#alphabet_counter = [sentence.upper().count(chr(65+i)) for i in range(26)] #THIS MIGHT BE FASTER!

alphabet_counter = [0 for i in range(26)]
for char in sentence.upper():
    if char in alphabet:
        alphabet_counter[alphabet.index(char)] += 1
end = time.perf_counter()
print(alphabet_counter,-start+end)
