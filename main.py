import time

alphabet = [chr(i) for i in range(65,91)]
start = time.perf_counter()

with open("small_text.txt",'r',encoding="utf-8") as file:
    file_contents = file.read()
    alphabet_counter = [file_contents.upper().count(chr(65+i)) for i in range(26)]

end = time.perf_counter()
print(alphabet_counter,sum(alphabet_counter),-start+end)


""" OLD VERSION
with open("small_text.txt",'r',encoding="utf-8") as file:
    file_contents = file.read()
    for char in file_contents.upper():
        if char in alphabet:
            alphabet_counter[alphabet.index(char)] += 1
"""
