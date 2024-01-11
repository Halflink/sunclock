line1 = "01100000"
line2 = "10010000"
line3 = "10010000"
line4 = "01100000"
line5 = "00000000"
line6 = "00000000"
line7 = "00000000"
line8 = "00000000"



data = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8
bstrings = [data[8*i:8*(i+1)] for i in range(int(len(data)/8))]
rlist = []
for bstring in bstrings:
    rlist.append(int(bstring, 2))
barray = bytearray(rlist)
print(barray)


