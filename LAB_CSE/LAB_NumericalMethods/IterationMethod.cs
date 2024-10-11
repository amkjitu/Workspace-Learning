using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;
using static System.Math;

namespace NumericalMethods
    {
    class IterationMethod
        {
        const double ep = 0.0001;
        //int n;
        
        ///f(x) = x3 - 9x + 1
        static double f(double x)
            {
            double f_of_x = x * x * x - 9 * x + 1;
            return f_of_x;
            }

        ///g(x) = (9x - 1)^1/3
        static double g(double x)
            {
            double g_of_x = Pow((9 * x - 1), 0.3333333);
            return g_of_x;
            }

        ///The method for the iteration 
        static void Iteration()
            {
            int i = 0;
            double x1, x2, x0;
            double f1, f2, f0, error;

            ///Determining the initial approximate root
            //in this equn for x1 = 3, f(x)>1
            for (x1 = 1; ; x1++)
                {
                f1 = f(x1);
                if (f1 > 0)
                    break;
                }
            //in this equn for x0 = 2, f(x)<1
            for (x0 = x1 - 1; ; x0--)
                {
                f0 = f(x0);
                if (f0 < 0)
                    break;
                }

            ///root of f(x) = lies between 2 and 3 so taking 2.5
            x2 = (x0 + x1) / 2;
            Write("\n\n\t Iteration no.1 root is : {0}", x2);

            //for(;i<n-1;i++) //Jodi number of iteration dewa thake
            for (; ; i++)
                {
                f2 = g(x2);
                Write("\n\n\t Iteration no.{0} root is : {1}", (i+2), f2);
                x2 = g(x2);
                error = Abs(f2 - f1);
                if (error < ep)
                    break;
                f1 = f2;
                }
            f1 = Round(f1, 4);
            Write("\n\t ----------------------------------------------------");
            Write("\n\t Root  = {0} (Approximate to 4 Decimal places)\n", f1);
            
            /*
            ///Jodi number of iteration dewa thake
             if(error>EPS)
               Write("\n\n\t NOTE: The no. of iterations are not sufficient.");
               Write("\n\n\n\t\t -----------------------------------------------");
               Write("\n\t\t ROOT  = {0} (Approximate to 4 Decimal places)", Round(f1, 4));
               Write("\n\t\t -----------------------------------------------");
            */
            }

        static void Main()
            {
            BackgroundColor = ConsoleColor.Yellow;
            WriteLine(" THE ITERATION METHOD ");
            Write("\n Given equation is  x*x*x - 9*x + 1 = 0\n");
            /*
            ///Jodi number of iteration dewa thake
            Write("\n Enter the no. of iterations ");
            n = Convert.ToInt32(ReadLine());
            */
            BackgroundColor = ConsoleColor.Cyan;
            ///Iteration method er function
            Iteration();
            BackgroundColor = ConsoleColor.White;
            }
    }
 }
