

#opens the file
#and puts it into a
bint = open("binarysoontobe.txt", "r")
a = bint.read()




#turns the string into a byte array
byte_array = bytearray(a, "utf8")
byte_list = []
for i in byte_array:
    x = bin(i)
    byte_list.append(x)



#turns the byte array into a string removing the first two characters
binlist = ""

for i in byte_array:
    x = bin(i)
    x = x[2:]
    #adds 0s because byte array only starts the binary at 1
    if(len(x) < 7):
        dist = 7 - len(x)
        x = ("0" * dist) + x
    binlist += x



print(binlist)
#searches for the max length of 1s or 0s
searchfor = "1"
length = 0
mlength = 0
for i in binlist:
    #if searchfor is the same as 1 it adds plus 1 in the length
    if(searchfor == i ):
        length += 1
    else:
        #checks if length is the max
        if(length > mlength):
            mlength = length
        length = 0


print("the biggest length of 1s in the text is :",mlength)




#same as for 1s but with 0 in search for
searchfor = "0"
length = 0
mlength = 0
for i in binlist:
    if(searchfor == i ):
        length += 1
    else:
        if(length > mlength):
            mlength = length
        length = 0


print("the biggest length of 0s in the text is :",mlength)
