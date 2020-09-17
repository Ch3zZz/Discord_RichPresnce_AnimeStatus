from pypresence import Presence
import time

client_id = ''  # put your real one client id
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop


anime = input("Какое аниме смотришь: ")
seriya = int(input("На какой серии: "))
vsego = int(input("Сколько всего: "))
while True:
	print(RPC.update(state=anime, details="Смотрит Аниме", party_size=[seriya, vsego])) # Can only update rich presence every 15 seconds
	time.sleep(1)
