///Given the equations
/*
2x1 − 6x2 − x3    = −38  ........(i)
− 3x1 − x2 + 7x3 = −34  ........(ii)
− 8x1 + x2 − 2x3 = −20  ........(iii)
*/

///Matrix representation of the given equations
/*
A[1][1]   +  A[1][2]   +   A[1][3]  =   A[1][4]
A[2][1]   +  A[2][2]   +   A[2][3]  =   A[2][4]
A[3][1]   +  A[3][2]   +   A[3][3]  =   A[3][4]
*/

using System;
namespace NumericalMethods
    {
     class GuassElimination
        {
        static void Main()
            {
            Console.WriteLine("Example: (3*3 Matrix)");
            Console.WriteLine("----------------------------------------------------");
            Console.WriteLine("  2x1 − 6x2 − x3 = −38........(i)");
            Console.WriteLine("− 3x1 − x2 + 7x3 = −34........(ii)");
            Console.WriteLine("− 8x1 + x2 − 2x3 = −20........(iii)");
            Console.WriteLine("A[1][1]   +  A[1][2]   +   A[1][3]  =   A[1][4]");
            Console.WriteLine("A[2][1]   +  A[2][2]   +   A[2][3]  =   A[2][4]");
            Console.WriteLine("A[3][1]   +  A[3][2]   +   A[3][3]  =   A[3][4]");
            Console.WriteLine("----------------------------------------------------");

            int i = 0, j = 0, k = 0, n = 0;
            //double A[20][20],c,x[10],sum = 0.0;

            double[] x = new double[4];
            double c = 0, sum = 0.0, m = 0;
          
            Console.WriteLine("Enter the order of matrix: ");
            n = Convert.ToInt32(Console.ReadLine());
            double[,] A = new double[20,20];
            
            Console.WriteLine("Enter the elements of augmented matrix row-wise: ");
            for (i = 1; i <= n; i++)
                {
                for (j = 1; j <= (n + 1); j++)
                    {
                    Console.Write("A[{0}][{1}] : ", i, j);
                    m = Convert.ToDouble(Console.ReadLine());
                    A[i,j] = m;
                    }
                }

            /// loop for the generation of upper triangular matrix
            for (j = 1; j <= n; j++)
                {
                for (i = 1; i <= n; i++)
                    {
                    if (i > j)
                        {
                        c = A[i,j] / A[j,j];  /// this is retio of coefficient
                        for (k = 1; k <= n + 1; k++)
                            {
                            A[i,k] = A[i,k] - c * A[j,k];  /// (R2-(a2/a1)*R1)
                            }
                        }
                    }
                }

            /// x2,x1 er value for 3 unknowns
            x[n] = A[n,n + 1] / A[n,n];

            /// this loop is for backward substitution
            for (i = n - 1; i >= 1; i--)
                {
                sum = 0;
                for (j = i + 1; j <= n; j++)
                    {
                    sum = sum + A[i,j] * x[j];
                    }
                x[i] = (A[i,n + 1] - sum) / A[i,i];
                }

            Console.WriteLine("The solution is: ");
            for (i = 1; i <= n; i++)
                {
                Console.WriteLine("x{0} = {1}", i, Math.Round(x[i]));
                }
            }

        ///Checking the result
        /*
        From the above code we get
        x1 = 4
        x2 = 8
        x3 = -2

        Putting the value of x1, x2 and x3 in the above equations,
        2x1 − 6x2 − x3    = −38  ........(i)
        = (2*4)-(6*8)-(-2)
        = -38

        − 3x1 − x2 + 7x3 = −34  ........(ii)
        = (-3*4)-8+(7*(-2))
        = -34

        − 8x1 + x2 − 2x3 = −20  ........(iii)
        = (-8*4)+8-(2*(-2))
        = -20
        */
        }
    }