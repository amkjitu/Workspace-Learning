///aida cholesky na LU decomposition
using System;
namespace NumericalMethods
    {
    class CholeskyMethods
        {
        static void Main()
            {
            int n, i, k, j, p;
            double[,] a = new double[10, 10];
            double[,] l = new double[10, 10];
            double[,] u = new double[10, 10];
            double[] b = new double[10];
            double[] z = new double[10];
            double[] x = new double[10];
            double sum = 0;
            Console.Write("Enter the order of matrix : ");
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter all coefficients of matrix : ");
            for (i = 1; i <= n; i++)
                {
                //Console.Write("\nRow {0} ",i);
                for (j = 1; j <= n; j++)
                    {
                    Console.Write("a[{0}][{1}] = ", i,j);
                    a[i,j] = Convert.ToDouble(Console.ReadLine());
                    }       
                }

            Console.WriteLine("Enter elements of b matrix");
            for (i = 1; i <= n; i++)
                b[i] = Convert.ToDouble(Console.ReadLine());

            //********** LU decomposition *****//
            for (k = 1; k <= n; k++)
                {
                u[k,k] = 1;
                for (i = k; i <= n; i++)
                    {
                    sum = 0;
                    for (p = 1; p <= k - 1; p++)
                        sum += l[i,p] * u[p,k];
                    l[i,k] = a[i,k] - sum;
                    }

                for (j = k + 1; j <= n; j++)
                    {
                    sum = 0;
                    for (p = 1; p <= k - 1; p++)
                        sum += l[k,p] * u[p,j];
                    u[k,j] = (a[k,j] - sum) / l[k,k];
                    }
                }

            /*
            //Displaying LU matrix
            cout << endl << endl << "LU matrix is " << endl;
            for (i = 1; i <= n; i++)
                {
                for (j = 1; j <= n; j++)
                    cout << l[i][j] << "  ";
                cout << endl;
                }
            cout << endl;
            for (i = 1; i <= n; i++)
                {
                for (j = 1; j <= n; j++)
                    cout << u[i][j] << "  ";
                cout << endl;
                }
            */

            //***** FINDING Z; LZ=b*********//
            for (i = 1; i <= n; i++)
                { //forward subtitution method
                sum = 0;
                for (p = 1; p < i; p++)
                    sum += l[i,p] * z[p];
                z[i] = (b[i] - sum) / l[i,i];
                }

            //********** FINDING X; UX=Z***********//
            for (i = n; i > 0; i--)
                {
                sum = 0;
                for (p = n; p > i; p--)
                    sum += u[i,p] * x[p];
                x[i] = (z[i] - sum) / u[i,i];
                }

            /*********** DISPLAYING SOLUTION**************/
            Console.WriteLine("\nSet of solution is");
            for (i = 1; i <= n; i++)
                Console.Write("x{0} = {1}  ", i, x[i]);
                Console.WriteLine();
            }
        }
    }
