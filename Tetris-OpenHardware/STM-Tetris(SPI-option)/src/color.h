#include <stdint.h>

struct RGB;
struct RGB {
    RGB() { 
        r = 0; 
        g = 0;
        b = 0; 
    }
    int r;
    int g;
    int b;
};
