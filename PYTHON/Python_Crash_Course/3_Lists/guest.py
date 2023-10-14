#!../bin/python3
import time

guests = ['Jesus', 'Holy Spirit', 'God the Father']

busy_guest = guests.pop(-1)
guests.append('Archangel Michael')
guests.insert(0, 'Archangel Gabriel')
guests.insert(3, 'Archangel Uriel')
guests.insert(-1, 'Archangel Ariel')
print('Great News Guys!!!, I found a bigger table for dinner tonight.')


for guest in guests:
    print('Dante Choppa your boy invites you to dinner, oh precious ' + guest)

print('Unfortunately ' + busy_guest + ' will not be joining us tonight.')
time.sleep(3)
print('OH NO!, I am really sorry Guys but the table will not be arriving anymore, \nnow i can only invite just two persons to dinner tonight')

cancelled_guests = [{guests.pop(0)}, {guests.pop(3)},{guests.pop(-2)},{guests.pop(-1)},]

for cancelled_guest in cancelled_guests:
    print(f"Hey" + cancelled_guest + "I am so sorry to inform you that I will not be able to invite you over for dinner tonight anymore.")

#print(type(cancelled_guests))