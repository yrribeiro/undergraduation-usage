#include<iostream>

using namespace std;

void bresenham(int x, int y, int xf, int yf);
void selectPixel(int x, int y, int d, int x2, int y2);

int main(){
    bresenham(1, 1, 8, 5);
}

void selectPixel(int x, int y){
    cout << "Point (" << x << ", " << y << ")" << endl;
}

void bresenham(int x, int y, int xf, int yf){
    int dx = xf - x;
    int dy = yf - y;
    int D = 2*dy - dx;
    int incE = 2*dy;
    int incNE = 2*(dy-dx);

    selectPixel(x, y);
    while (x < xf){
        x++;

        if (D<=0){
            // choosing the eastern pixel
            D += incE;
        }else{
            // choosing the northeastern pixel
            y++;
            D += incNE;
        }
        selectPixel(x, y);
        // cout << "d-value = " << D << endl;
    }
}
