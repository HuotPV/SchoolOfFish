# SchoolOfFish

This program aims at reproducing the coordinated motion of fishes (or birds, as you prefer) and their response to predators.
Different types of fishes populate and evolves in a virtual pond.
At every time step, each fish makes a series of modifications to its orientation in response to its environnement (number and types of fishs present around it) and update its position in order to a) get closer to distant friendly fishes, b) imitate nearby friendly fishes, c) avoid collision with other fishes, and d) flee predatory fishes.


Requirements:
Docker

How to run:
With docker:
Build docker image:
docker build -t fish-python .

Run docker image:
docker run --name my-fish -v ${PWD}:/app/outputs fish-python

Manually:
install the python packages listed in requirements.txt
run main.py



Fish class:
Each specific fish class (BlueFish, RedFish, ...) inherits from the Fish class. The latter defines a set of attributes (velocity, position, colour, type ...) and methods used by most fishes.

Actions includes:
- random motion: add a random velocity vector to the fish velocity.
- list fish (several variations): return a list of fishes present in the neighbourhood of a fish.
- aimFish: adds a velocity vector aiming towards another fish to a fish velocity.
- avoidFish: adds a velocity vector directed away from a fish to a fish velocity.
- imitateFish: adds a close neighbouring fish velocity to a fish velocity.
- fleeFish: same as avoidFish, but with a bigger radius.

Specialized fish classes:
Each fish subclass has its own attrbiutes value, some specific methods and a dedicated list of actions.
BlueFish are the basic fish, identical to the default Fish.
RedFish are similar to BlueFish, but have slighlty different attributes values (stronger random motion, weaker group behaviour, faster motion ...)
BlueFish and RedFish do not interact with one another, appart from avoiding collisions.
CarnivorousFish have no group behaviour. When they are hungry, they hunt for fish until they manage to reach one and eat it.
