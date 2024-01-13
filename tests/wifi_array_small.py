line1 = "0000111111110000"
line2 = "0111110001111110"
line3 = "1110000000000111"
line4 = "0000000000000000"
line5 = "0000011111100000"
line6 = "0000111001110000"
line7 = "0011100000011100"
line8 = "0000000000000000"
line9 = "0000001111000000"
line10 = "0000011111100000"
line11 = "0000110000110000"
line12 = "0000000000000000"
line13 = "0000000000000000"
line14 = "0000000110000000"
line15 = "0000001111000000"
line16 = "0000000110000000"


data = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 + line12 + line13 + line14 + line15 + line16
bstrings = [data[8*i:8*(i+1)] for i in range(int(len(data)/8))]
rlist = []
for bstring in bstrings:
    rlist.append(int(bstring, 2))
barray = bytearray(rlist)
print(barray)


