from matplotlib import pyplot as plt

alphabet = [chr(i) for i in range(65,91)]

with open("small_text.txt",'r',encoding="utf-8") as file:
    file_contents = file.read()
    alphabet_counter = [file_contents.upper().count(chr(65+i)) for i in range(26)]

plt.bar(alphabet,alphabet_counter,label="character repetition")
plt.legend()
plt.show()
