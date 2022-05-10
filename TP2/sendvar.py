import os,sys

var = 12.5
var_b = var.hex().encode()
length = len(var_b)
lb = length.to_bytes(4,byteorder="little",signed=True)
os.write(pipew,lb)
os.write(pipew,var_b)

lb==os.read(piper,4)
length = int.from_bytes(lb,byteorder='little',signed=True)
var_b= os.read(piper,length)
var=float.from_hex(var_b.decode())