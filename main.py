sentence = "Once upon a time, there was a quite long sentence which served for testing reasons!"

alphabet = [chr(i) for i in range(65,91)]
alphabet_counter = [sentence.upper().count(chr(65+i)) for i in range(26)]
print(alphabet_counter)
