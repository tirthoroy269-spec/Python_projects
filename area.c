# include <stdio.h>
int main()
{
    float r , area ;
    printf("Enter the radius of the circle ");
    scanf("%f",&r);
    area=r*r*22/7;
    printf("Area of the circle %.1f\n",area);
    return 0;
}