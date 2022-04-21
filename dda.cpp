#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <graphics.h>
#include <conio.h>

// Setting namespace
using namespace std;

// graph function

void InitVGA(void);
void traco(int x1, int x2, int y1, int y2, int color);

void InitVGA()
{
    int gdriver, gmode;
    char gerror;
    gdriver = DETECT;
    gmode = 2;
    initgraph(&gdriver, &gmode, (char *)"");

    gerror = graphresult();
    if (gerror != grOk)
    {
        printf("Graphic Error: %s\n", grapherrormsg(gerror));
        exit(1);
    }
}

void traco(int x1, int x2, int y1, int y2, int color)
{
    float x, y;
    int increment;

    // teste
    if ((x2 - x1) >= (y2 - y1))
    {
        increment = (y2 - y1) / (x2 - x1);
        y = y1;
        for (x = x1; x <= x2; x++)
        {
            putpixel(x, y, color);
            y += increment;
        }
    }
    else
    {
        increment = (x2 - x1) / (y2 - y1);
        x = x1;
        for (y = y1; y <= y2; y++)
        {
            putpixel(x, y, color);
            x += increment;
        }
    }
}

// main program
int main()
{
    int x1, x2, y1, y2, color;
    InitVGA();
    traco(500, 200, 400, 100, WHITE);
}
