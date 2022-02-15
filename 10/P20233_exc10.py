

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


#reuse of binlist
binlist = ""
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
    #adds them to the list
    binlist += x



print(binlist)


#times needed to run the multiplication
while(len(binlist) % 16 != 0 ):
    #makes sure that len(binlist)/16 will be an int
    #the list is with increments of 4 characters so I only have ta add 4 0 every time
    binlist += "0000"
times = int(len(binlist) / 16) - 1

#the requests of the excersise req0 = number of the hexadecimal
req0 = 0
req1 = 0
req2 = 0
req3 = 0
req4 = 0
#checks if the numbers fill the requirements
for i in range(times):
    req0 += 1
    x = binlist[(16 * req0) :16 * (req0 + 1)]
    print(x)
    x = int(x, 2)
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
