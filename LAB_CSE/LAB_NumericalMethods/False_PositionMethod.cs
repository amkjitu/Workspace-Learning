using System;
using static System.Math;
using static System.Console;

namespace NumericalMethods
    {
    class False_PositionMethod
        {
        static double EPSILON;

        /// f(x) = x^3 - x - 4 
        static double f(double x)
            {
            return x * x * x - x - 4;
            //return x * x * x - 4*x - 9;
            }

        // Prints root of f(x) with error of EPSILON 
        static (double, double) InitialRootBetween()
            {
            int x1, x0;
            double xl, xu;
            ///Determining the initial approximate root
            //in this equn for x1 = 2, f(x)>1
            for (x1 = 1; ; x1++)
                {
                xu = f(x1);
                if (xu > 0)
                    break;
                }
            //in this equn for x0 = 1, f(x)<1
            for (x0 = x1 - 1; ; x0--)
                {
                xl = f(x0);
                if (xl < 0)
                    break;
                }
            return (xl, xu);
            }
        static void falsePosition(double a, double b)
            {
            /*
             ///initial root between er value jodi user nito
             if (f(a) * f(b) >= 0)
                 {
                 WriteLine("You have not assumed" + " right a and b");
                 return;
                 }
             */
            double c = (a+b)/2; int noOfIteration = 1; ///initial root xr = c
            WriteLine("Iteration\txl\t\t\txu\t\t\txr");
            WriteLine("------------------------------------------------------------------");
            while ((b - a) >= EPSILON)
                {
                WriteLine("{0}\t\t{1}\t\t\t{2}\t\t\t{3}", noOfIteration, Round(a, 5), Round(b, 5), c);
                // Find point where the staright line intersects in the x-axis 
                //c = (b*f(a)-a*f(b))/(f(a)-f(b)); //xr = xu*f(xl)-xl*f(xu)/f(xl)-f(xu)
                c = Round((b * f(a) - a * f(b)) * (1 / (f(a) - f(b))), 6); //xr = xu*f(xl)-xl*f(xu)/f(xl)-f(xu)

                // Check if intersecting
                // point is root 
                if (f(c) == 0.0)
                    break;

                // Decide the side  
                // to repeat the steps 
                else if (f(c) * f(a) < 0)
                    b = c;
                else
                    a = c;
                noOfIteration++;
                if (noOfIteration > 13) break;
                }

            //root upto 3 decimal places 
            WriteLine("The value of " + "root is : " + Round(c, 3));
            }

        // Driver Code 
        static public void Main()
            {
            WriteLine("False-Position Method");
            WriteLine("----------------------");
            BackgroundColor = ConsoleColor.Yellow;
            WriteLine("Given f(x) = x^3 - x - 4");
            Write("Enter the value of EPSILON: ");
            EPSILON = Convert.ToDouble(Console.ReadLine());

            // Determining initial roots
            var (xl, xu) = InitialRootBetween();
            BackgroundColor = ConsoleColor.Cyan;
            falsePosition(xl, xu);
            BackgroundColor = ConsoleColor.White;
            }
        }
    }
