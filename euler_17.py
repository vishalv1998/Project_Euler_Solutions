dict_of_numbers={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "00":"zero",
    "01":"one",
    "02":"two",
    "03":"three",
    "04":"four",
    "05":"five",
    "06":"six",
    "07":"seven",
    "08":"eight",
    "09":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen",
    "20":"twenty",
    "30":"thirty",
    "40":"forty",
    "50":"fifty",
    "60":"sixty",
    "70":"seventy",
    "80":"eighty",
    "90":"ninety",
    "100":"one hundred",
    "200":"two hundred",
    "300":"three hundred",
    "400":"four hundred",
    "500":"five hundred",
    "600":"six hundred",
    "700":"seven hundred",
    "800":"eight hundred",
    "900":"nine hundred"
    }
#The above dictionary is used for formatting of output in accordance to the British English Vocabulary. Only Unique Numbers are used in the dictionary. other numbers
#can be derived from the above
print("FINDING LENGTH of Ouput excluding hyphens and whitespaces")
def get_number(n):
    if(len(n)==1):#checks if the input ranges from 1-10. if so prints the output corresponding to the dictionary key
        print(dict_of_numbers[n])
        print(len(dict_of_numbers[n]))
    else:
        if(len(n)==2):
            if(n in dict_of_numbers.keys()):
                print(dict_of_numbers[n])
                print(len(dict_of_numbers[n]))
                return
            n="0"+n#adds 0 to the input number in case number length is 2 ex:78 becomes 078
        number=[]
        number+=[n[0],n[1],n[2]]#List that obtains each character position
        #print(number)
        final_word=""#store the final word
        if(n in dict_of_numbers.keys()):
        	print(dict_of_numbers[n])
        	print(len(dict_of_numbers[n]))
        	return
        if(number[0]!="0"):#checks if 0 is not at hundred place
            final_word+=dict_of_numbers[n[0]]+" hundred"
        else:
            if(n[1:3] in dict_of_numbers.keys()):
                final_word+=dict_of_numbers[n[1:3]]#checks for case of 10,11,15,19,20 etc and prints the respective dict value of key
            else:
                number[1]=int(number[1])*10#multiply 10's position by 10. example for 352 the 5 becomes 50
                number[1]=str(number[1])#convert to string since dictionary keys are strings
                final_word+=dict_of_numbers[number[1]]+"-"+dict_of_numbers[n[2]]
            print(final_word)#display word
            final_word=final_word.replace(' ','')
            final_word=final_word.replace('-','')
            #removing hyphens and whitespaces to obtain actual length
            print(len(final_word))#print length
            return#return from current iteration to stop executing below code
        #print(n[1:3])
        #print(number)
        if(n[1:3] in dict_of_numbers.keys()):
            final_word+=" and "+dict_of_numbers[n[1:3]]#checks for case of 10,20,30,40 etc and prints the respective dict value of key
            print(final_word)
            print(len(final_word))
            return
        else:
	        if(n[1:3].endswith('0')):
	            final_word+=" and "+dict_of_numbers[n[1:3]]#format for output
	        else:
	            #same procedure as before
	            number[1]=int(number[1])*10
	            number[1]=str(number[1])
	            #print(number[1])

	            final_word+=" and "+dict_of_numbers[number[1]]+"-"+dict_of_numbers[n[2]]
	        print(final_word)
	        final_word=final_word.replace(' ','')
	        final_word=final_word.replace('-','')
	        #removing hyphens and whitespaces
	        print(len(final_word))
input1=input("ENTER A NUMBER (0-999)")
if(int(input1)>999 or int(input1)<0):
    print("Please enter a number within the specified range")
else:
    get_number(input1)

for i in range(1,1000):
	get_number(str(i))
