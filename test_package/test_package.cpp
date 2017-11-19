#include <fakeit.hpp>

struct SomeInterface {
    virtual int foo(int) = 0;
    virtual int bar(double) = 0;
};

int main()
{
    // Instantiate a mock object.
    fakeit::Mock<SomeInterface> mock;

    return 0;
}
