word = "cat"
word2 = "dog"
tlist1 = [1,2,3,4,5,6]
tlist2 = [1,2,3,4,5]
def mukki(word,word2):
	word3 = word + " " + word2
	return word3

final = mukki(word,word2)
print(final)

def mukki2(word2):
	return word

final2 = mukki2(word)
print(final2)	

def mukki3(list1,list2):
	if list1 > list2:
		print("mukul")
	else:
	    print("mukkki")

	return tlist2
yes = mukki3(tlist1,tlist2)
print(yes)