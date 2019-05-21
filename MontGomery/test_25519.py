

from ecc_lib import *




p = 2**255  - 19

x1 = 0x0900000000000000000000000000000000000000000000000000000000000000
#scalar = 0x77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
#scalar = 0x6ebd9ed75882d52815a97585caf4790a7f6c6b3b7f821c5e259a24b02e502e11
#scalar = 0x0200000000000000000000000000000000000000000000000000000000000000
scalar = 0x05dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb

A24 = 0x01DB42


byte_scalar = scalar.to_bytes(32,byteorder='little')
byte_x1= x1.to_bytes(32,byteorder='little')

int_scalar = int.from_bytes(byte_scalar, byteorder='big')
int_x1= int.from_bytes(byte_x1, byteorder='big')
print("\n Prime                : ", hex(p))
print("\n Base Point           : ", hex(x1))
print("\n Base Point           : ", hex(int_x1))
print("\n scalar               : ", hex(scalar))
print("\n scalar after big_num : ",hex(int_scalar))


rx,rz = ecc_mul_x25519(int_x1,int_scalar,A24,p)
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
rz = (rz * inv_rz)%p


byte_rx  = rx.to_bytes(32,byteorder='big')
int_rx  = int.from_bytes(byte_rx,byteorder='little')

byte_rz  = rz.to_bytes(32,byteorder='big')
int_rz  = int.from_bytes(byte_rz,byteorder='little')
print("\n x25519 result       : ")
print(" rx = ", hex(rx))
print(" int_x = ", hex(int_rx))
print(" z = ", hex((int_rz)))
print()


