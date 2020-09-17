from pypresence import Presence
import time

client_id = '702852927450120282'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop


anime = input("Anime vvedi svoloch: ")
seriya = int(input("Na kakoi serii: "))
vsego = int(input("Vsego Skok: "))
while True:
	print(RPC.update(state=anime, details="Смотрит Аниме", party_size=[seriya, vsego])) # Can only update rich presence every 15 seconds
	time.sleep(1)