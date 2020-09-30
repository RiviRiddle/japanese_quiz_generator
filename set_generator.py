fl_num = input("Tango number: ")
num = fl_num.replace(".", "")
extra = input("Extra words: ")

word_list = eval(input("Formatted word list: "))

# [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("q" + num + " = Quiz(" + fl_num + ", [], " + extra + ")")

for i in range(len(word_list)):
	if len(word_list[i]) == 4:
		print("q" + num + ".wl[" + str(i) + "] = Word(\"" + word_list[i][0] + "\", \"" + word_list[i][1] + "\", \"" + word_list[i][2] + "\", \"" + word_list[i][3] + "\", "  + "[], [])")
	else:
		print("q" + num + ".wl[" + str(i) + "] = Word(\"" + word_list[i][0] + "\", \"" + word_list[i][1] + "\", \"" + word_list[i][2] + "\", "  + "None, [], [])")

print("tango_set_list.append(" + fl_num + ")")

'''word_list = [[], [], [], [], [], [], [], [], []]

word_list.append([] * int(extra))'''

'''for i in range(len(word_list)):
	for j in range(1):
		word_list[i].append(input("Word (english translation, comma, romaji translation, comma, kana): "))
		word_list[i] = word_list[i][0].split(', ')
		
print(word_list)'''