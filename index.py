from lib.human import Human
from lib.network import Network
from lib import diffiehellman, mod
from lib.vars import variables

alice = Human("Alice")
bob = Human("Bob")
ethernet = Network()

alice.generate_keys(variables['g'], variables['prime'])
bob.generate_keys(variables['g'], variables['prime'])

ethernet.send(alice.public_key)
bob.calculate_secret_key(ethernet.receive(), variables['prime'])

ethernet.send(bob.public_key)
alice.calculate_secret_key(ethernet.receive(), variables['prime'])

print(alice.secret_key)
print(bob.secret_key)
