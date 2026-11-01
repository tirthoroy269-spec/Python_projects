// #include <iostream>
// using namespace std;
// int main()
// {
//     int a;
//     a=10;
//     int *p1=&a;
//     cout<<"Enter the number to be replaced ";
//     cin>>*p1;
//     cout<<"Replaced value "<<*p1;
// }

#include<iostream>
#include<string>
using namespace std;
class book{
    public:
    string name;
    float price;
    string ret;
};
int main(){
    book b1={"Harry Potter",450.75,"4th February"};
    cout<<b1.name<<endl;
    cout<<b1.price<<endl;
    cout<<b1.ret<<endl;
}