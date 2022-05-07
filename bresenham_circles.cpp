#include<iostream>

using namespace std;

void bresenhamCircles(int r);
void selectPixel(int x, int y, int d, int x2, int y2);

int main(){
    bresenhamCircles(14);
}

void selectPixel(int x, int y){
    cout << "Point (" << x << ", " << y << ")" << endl;
}

void bresenhamCircles(int r){
    int x = 0;
    int y = r;
    int D = 1 - r; // integer arithmetic for floating must be 5/4 - r
    int incSE = 2*(x-y) + 5;
    int incE = 2*x + 3;

    selectPixel(x, y);
    while (y > x){
        x++;

        if (D>=0){
            // choosing the southeastern pixel
            y--;
            D += incSE;
        }else{
            // choosing the eastern pixel
            D += incE;
        }
        selectPixel(x, y);
    }
}
