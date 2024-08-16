from walking import Llama, Donkey, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, BoaConstrictor, Python, GarterSnake
from swimming import Goldfish, Mallard, KoiFish, Frog, Turtle

# Creating instances of each critter with name and species
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )
lil_bro = Donkey("Mr. Little", "donkey", "morning", "Donkey Chow")
ronaldo = Goat("Ronaldo", "goat", "afternoon", "Goat chow")
wooly = Sheep("Wooly", "sheep", "midday")
porky = Pig("Porky", "pot-bellied pig", "morning")

copper = Copperhead("Copper", "Copperhead Snake")
rattles = RatSnake("Rattles", "Rat Snake")
squeezy = BoaConstrictor("Squeezy", "Boa Constrictor")
py = Python("Py", "Python")
slim = GarterSnake("Slim", "Garter Snake")

swimmy = Goldfish("Swimmy", "Goldfish")
mal = Mallard("Mal", "Mallard")
koiboy = KoiFish("KoiBoy", "Koi Fish")
hoppy = Frog("Hoppy", "Frog")
slowpoke = Turtle("Slowpoke", "Turtle")

#feeding walking animals
miss_fuzz.feed()
lil_bro.feed()


# Testing
print(f'{lil_bro.name} the {lil_bro.species} is available to pet during the {lil_bro.shift} shift.')
print(f'{ronaldo.name} the {ronaldo.species} is available to pet during the {ronaldo.shift} shift.')
print(f'{wooly.name} the {wooly.species} is available to pet during the {wooly.shift} shift.')
print(f'{porky.name} the {porky.species} is available to pet during the {porky.shift} shift.')

# Printing each critter's information
print(lil_bro)
print(miss_fuzz )
print(ronaldo)
print(wooly)
print(porky)
print(copper)
print(rattles)
print(squeezy)
print(py)
print(slim)
print(swimmy)
print(mal)
print(koiboy)
print(hoppy)
print(slowpoke)
