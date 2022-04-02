DEBUG_FLAGS = -g3 - O0
RELEASE_FLAGS = -DNDEBUG -O3

FLAGS = $(RELEASE_FLAGS)

preprocess:
	g++ $(FLAGS) -E Functions.cc > Temp.cc

assemble:
	g++ $(FLAGS) -S Functions.cc

compile:
	g++ $(FLAGS) -c Functions.cc -o Functions.o

build:
	g++ $(FLAGS) Functions.o -o Functions

print_exe:
	objdump -CS Functions
