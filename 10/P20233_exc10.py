

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
    binlist += x

#prints the binlist
print(binlist)

#the requests of the excersise req0 = number of the hexadecimal
req0 = 0
req1 = 0
req2 = 0
req3 = 0
req4 = 0

#turns the byte array to numbers as per the excersise request
for i in byte_array:
    x = str(bin(i))
    x = x[2:]
    #adds 0s because byte array only starts the binary at 1
    if(len(x) < 7):
        dist = 7 - len(x)
        x = ("0" * dist) + x
    #pics the first and last 2 digits
    x = x[:2] + x[-2:]
    #turns x into a interer
    x = int(x, 2)
    # turns x into hexadecimal and prints it
    x = hex(x)
    print(x)
    #turns it back to decimal to do the calculations required
    x = int(x,16)
    #finds the number of request fulfiled by the number
    req0 += 1
    if(( x % 2 ) == 0):
        req1 += 1
    if(( x % 3 ) == 0):
        req2 += 1
    if(( x % 5 ) == 0):
        req3 += 1
    if(( x % 7 ) == 0):
        req4 += 1

#finds the percentages
req1 = (req1 / req0) * 100
req2 = (req2 / req0) * 100
req3 = (req3 / req0) * 100
req4 = (req4 / req0) * 100
print("The percentage of numbers divided by 2 is", req1,"%")
print("The percentage of numbers divided by 3 is", req2,"%")
print("The percentage of numbers divided by 5 is", req3,"%")
print("The percentage of numbers divided by 7 is", req4,"%")
