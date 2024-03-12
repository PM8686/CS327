#include "LinkedList.hpp"
#include <iostream>

int main() {

    LinkedList<int> list;
    list.push(1);
    list.push(2);
    list.push(3);
    LinkedListIterator<int> i = list.getIter();
    while (!i.isDone()) {
        std::cout << i.next() << std::endl;
    }
    list.push(4);
    list.push(5);

    std::cout << list.pop() << std::endl;
    std::cout << list.pop() << std::endl;
    std::cout << list.pop() << std::endl;

    return 0;
}
//  linked list where they both point to each other
// do that with reference to the reference counter
// #include "LinkedList.hpp"
// #include <iostream>

// int main(){
//     // Problem: Because the 2 SmartPointers point to each other, when we try to delete/free the SmartPointers's Nodes, 
//     // we do/can not free because each object still has a ReferenceCount > 0.
//     SmartPointer<Node<int>> sp1(new Node<int>(10));
//     SmartPointer<Node<int>> sp2(new Node<int>(11));
//     sp1->setNext(sp2); // we assign sp1's SmartPointer next to sp2 
//     sp2->setNext(sp1); // we assign sp2's SmartPointer next to sp1, creating a SmartPointer cycle.
//     // at the end, the program attempts to delete the Nodes, but because they point to each other, each object still has a ReferenceCount > 0
//     // thus, we get a memory leak (confirmed via Valgrind).

//     return 0;
// }