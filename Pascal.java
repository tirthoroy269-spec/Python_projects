import java.util.*;
public class Pascal
{
    int fact(int i)
    {
        int p=1;
        for(int j=1;j<=i;j++)
        {
            p=p*j;
        }
        return p;
    }

    void pattern(int n)
    {
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=n-i;j++)
            {
                System.out.print(" ");
            }

            for(int j=0;j<=i;j++)
            {
                System.out.print(fact(i)/(fact(j)*fact(i-j))+" ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of rows");
        int a=sc.nextInt();
        Pascal obj=new Pascal();
        obj.pattern(a);
    }
}