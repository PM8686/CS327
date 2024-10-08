#pragma once

#include <iostream>
#include "SmartPointer.hpp"

template <class T>
class Node
{
    T data;
    SmartPointer<Node<T>> next;

public:
    Node(T d) : data(d), next(nullptr) {}

    const T &get() const
    {
        return data;
    }

    SmartPointer<Node<T>> getNext() const
    {
        return next;
    }

    void setNext(SmartPointer<Node<T>> n)
    {
        next = n;
    }
};

template <class T>
std::ostream &operator<<(std::ostream &os, Node<T> n)
{
    os << n.get();
    return os;
}

template <class T>
class LinkedListIterator
{
    SmartPointer<Node<T>> current;

public:
    LinkedListIterator(SmartPointer<Node<T>> n) : current(n) {}

    bool isDone() const
    {
        return current == nullptr;
    }
    T next()
    {
        T ret = current->get();
        current = current->getNext();
        return ret;
    }
};

template <class T>
class LinkedList
{
    SmartPointer<Node<T>> head;

public:
    LinkedList() : head(nullptr) {}

    LinkedListIterator<T> getIter()
    {
        return LinkedListIterator<T>(head);
    }

    void push(T data)
    {
        SmartPointer<Node<T>> newNode(new Node<T>(data));
        newNode->setNext(head);
        head = newNode;
    }

    T pop()
    {
        T ret = head->get();
        head = head->getNext();
        return ret;
    }

    T peek()
    {
        return head->get();
    }
};