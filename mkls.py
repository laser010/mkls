import itertools
from array import array
import string
import sys

print("""

@@@@@@@@@@   @@@  @@@  @@@        @@@@@@
@@@@@@@@@@@  @@@  @@@  @@@       @@@@@@@
@@! @@! @@!  @@!  !@@  @@!       !@@
!@! !@! !@!  !@!  @!!  !@!       !@!
@!! !!@ @!@  @!@@!@!   @!!       !!@@!!
!@!   ! !@!  !!@!!!    !!!        !!@!!!
!!:     !!:  !!: :!!   !!:            !:!
:!:     :!:  :!:  !:!   :!:          !:!
:::     ::    ::  :::   :: ::::  :::: ::
 :      :     :   :::  : :: : :  :: : :

Programmed by https://www.instagram.com/laser01/  Version 1.0.0

""")

def main():
	try:
		chr_num_sym = input('\nEnter characters/numbers/symbols... : ')
		mattresses = input('Enter how many number of mattresses : ')

		def order():
			print("\n(1) Save outpot in wordlist.txt .\n(2) Show them on terminal .\n(99) exit")

			order = input('\nmkls > ')
			if order == "99" :
				exit()

			elif order == "1" :
				output = open("wordlist.txt", "w")
				sys.stdout = output
				for wl in itertools.product(chr_num_sym, repeat=int(mattresses)):
					try:
						op = ''.join(wl)
					except AttributeError:
						op = string.join(wl, '')
					print(op)
				output.close

			elif order == "2" :
				for wl in itertools.product(chr_num_sym, repeat=int(mattresses)):
					try:
						op = ''.join(wl)
					except AttributeError:
						op = string.join(wl, '')
					print(op)
			else:
				print("[ERROR] Not found!")
		order()

	except ValueError:
		print("\n\n[ERROR] You must enter just numbers !.")
	except KeyboardInterrupt:
		pass
if __name__ == "__main__" :
	main()

