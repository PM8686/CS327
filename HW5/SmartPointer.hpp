#pragma once

#include <cstddef>

class ReferenceCounter
{
    int count; // Reference count
public:
    ReferenceCounter() : count{0} {};
    void increment()
    {
        count++;
    }
    int decrement()
    {
        return --count;
    }

    template <typename T> friend class SmartPointer;
};

template <typename T>
class SmartPointer
{
    // private instance variables for dumb pointer and ReferenceCounter
    T *dumb_ptr;
    ReferenceCounter *counter;

public:
    SmartPointer(T* data) // should be stored on the stack
    {
        // initialize dumb pointer
        dumb_ptr = data;
        // set up and increment reference counter
        counter = new ReferenceCounter;
        counter->increment();
    }

    // Copy constructor
    SmartPointer(const SmartPointer<T> &other_sp)
    {
        // Copy the data and reference pointer
        dumb_ptr = other_sp.dumb_ptr;
        counter = other_sp.counter;
        
        // increment the reference count
        if (counter)
        {
            counter->increment();
        }
    }

    // Destructor
    ~SmartPointer()
    {
        // Decrement the reference count
        if (counter)
        {
            counter->decrement();
        }

        // if reference become zero delete the data
        if (counter->count == 0)
        {
            delete counter;
            delete dumb_ptr;
        }
    }

    T &operator*() const
    {
        // delegate
        return *dumb_ptr;
    }

    T *operator->() const
    {
        // delegate
        return dumb_ptr;
    }

    // Assignment operator
    SmartPointer<T> &operator=(const SmartPointer<T> &rhs)
    {
        // Lookout for use-after-free bug here! It may cause undefined behavior
        // refers to deleting the current data and reference counter but for some reason using it again.
        if (this == &rhs || dumb_ptr == rhs.dumb_ptr)
        {
            return *this;
        }

        // Deal with old SmartPointer that is being overwritten
        counter->decrement();
        if (counter->count == 0)
        {
            delete this->dumb_ptr;
            delete this->counter;
        }

        // Copy data and reference pointer from parameter into this (similar to copy constructor)
        dumb_ptr = rhs.dumb_ptr;
        counter = rhs.counter;

        // increment the reference count
        if (counter)
        {
            counter->increment();
        }

        // return this SmartPointer
        return *this;
    }

    // return the number of different SmartPointers managing the current object
    int useCount() const
    {
        if(counter)
        {
            return counter->count;
        }
        else
        {
            return 0;
        }
    }

    // Check equal to nullptr
    bool operator==(std::nullptr_t rhs) const
    {
        return dumb_ptr == rhs;
    }

    // Check not equal to nullptr
    bool operator!=(std::nullptr_t rhs) const
    {
        return dumb_ptr != rhs;
    }

    // Check not equal to nullptr
    operator bool() const
    {
        return this != nullptr;
    }
};
