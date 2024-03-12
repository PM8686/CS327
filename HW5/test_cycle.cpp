#include <iostream>
#include "LinkedList.hpp"

int main()
{
    //  create two nodes and smart pointers to them
    //  as each object is created, the reference counter both increase to 1 for sp1 and sp2
    SmartPointer<Node<int>> sp1(new Node<int>(10));
    SmartPointer<Node<int>> sp2(new Node<int>(11));

    // Make sp1 point to sp2, creating a cycle
    // with a new pointer referencing the data, the reference counter increases to 2
    sp1->setNext(sp2); 
    sp2->setNext(sp1);

    // both return 2 because with sp1 having a pointer to sp2 and vice versa, along with sp1 and sp2 existing, 
    // this creates 2 references for each object managed by sp1 and sp2, and thus creates a cycle of objects that mutually refer to each other. 
    std::cout<<sp1.useCount() << "\n";
    std::cout<<sp2.useCount() << "\n";

    // the smart pointers sp1 and sp2 should both be destoryed, this means that the reference count will decrease by one for the object sp1 references 
    // and the object that sp2 references. However, when we destroy the data (the node) that each pointer is referencing, the destructor does not take
    // into account that within the node, there was a pointer to the object, so while both objects should have 0 references, they both have 1 despite
    // nothing pointing to that data. 
    sp1.~SmartPointer();
    sp2.~SmartPointer();

    std::cout<<sp1.useCount() << "\n"; // returns 1 (incorrectly, should be 0)
    std::cout<<sp2.useCount() << "\n"; // returns 1 (incorrectly, should be 0)

    return 0;
// in fact, if we did not call the destructor, the function would have returned a valgrind error. This would be due to the reference counter only ever reaching
// 1 and not 0 (for the reasons discussed on lines 21-24), so the reference counter would not have been properly destroyed, leading to a memory leak, and thus 
// a valgrind error. after returning 0, both sp1 and sp2 leave the scope and are supposed to be deleted by the stack, which automatically calls the destructor. 
}