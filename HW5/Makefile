CXX = g++
CXXFLAGS = -std=c++11 -Wall

all: test

test: test.o 
	$(CXX) $(CXXFLAGS) $^ -o $@

test.o: test_cycle.cpp LinkedList.hpp SmartPointer.hpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# LinkedList.o: LinkedList.hpp
# 	$(CXX) $(CXXFLAGS) -c $< -o $@

# SmartPointer.o: SmartPointer.hpp
# 	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f *.o test