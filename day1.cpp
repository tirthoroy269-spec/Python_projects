// #include <iostream>
// using namespace std;

// int main() 
// {
//     cout << "Hello, World!";
//     return 0;
// }

// #include <iostream>
// using namespace std;

// int main() 
// {
//     cout << "Hello, World!"<<endl;
//     cout << "Tirtho!!";
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a,b,sum;
//     a=2;
//     b=3;
//     sum=a+b;
//     cout <<"Sum="<<sum;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a,b,sum;
//     a=2;
//     b=3;
//     sum=a+b;
//     cout<<"a="<<a<<"\n";
//     cout<<"b="<<b<<endl;
//     cout <<"Sum="<<sum;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a,b,sum;
//     a=2;
//     b=3;
//     sum=a+b;
//     cout<<"a="<<a<<"\n";
//     cout<<"b="<<b<<endl;
//     cout <<"Sum="<<sum<<"\n";
//     cout <<"Dif="<<a-b<<endl;
//     cout <<"Mul="<<a*b<<"\n";
//     cout <<"Div="<<(float)a/b<<endl;
//     cout <<"Mod="<<b%a<<"\n";
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a,b,sum;
//     cout<<"Enter two numbers"<<"\n";
//     cin>>a>>b;
//     //cin>>b;
//     sum=a+b;
//     cout<<"a="<<a<<"\n";
//     cout<<"b="<<b<<endl;
//     cout <<"Sum="<<sum<<"\n";
//     cout <<"Dif="<<a-b<<endl;
//     cout <<"Mul="<<a*b<<"\n";
//     cout <<"Div="<<(float)a/b<<endl;
//     cout <<"Mod="<<a%b<<"\n";
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int age=22;
//     int marks=85;
//     cout<<(age>=18 && age<=25)<<"\n";
//     cout<<(marks>=90 || marks>=80)<<endl;
//     cout<<!(age>18)<<endl;
//     return 0;
// }

#include <iostream>
using namespace std;
int main()
{
    int age;
    cout<<"Enter your age"<<endl;
    cin>>age;
    if(age>=18)
    {
        cout<<"You are eligible";
    }
    else
    {
        cout<<"You are not elgible";
    }
    return 0;
}