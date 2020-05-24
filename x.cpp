#include <stdio.h>
#include <math.h>

float distance(float v1, float r1, float v2, float r2, float dt) {
    // Calculate new positions and convert to radians                           
    float fi1 = v1*dt*3.14/180, fi2 = v2*dt*3.14/180;
    //print("%d",M_PI);
    // Polar distance formula                                                   
    return sqrt(pow(r1, 2) + pow(r2, 2) - 2*r1*r2*cos(fi1-fi2));
}

int main()
{
    float v1,v2,r1,r2,t;
    scanf("%f%f%f%f%f",&v1,&r1,&v2,&r2,&t);
    printf("%.2f\n", distance(v1,r1,v2,r2,t));
}
