using System;
using System.Collections.Generic;
using System.Text;

namespace NumericalMethods
    {
    class TrapezoidalRule
        {
        static double y(double x)
            {
            ///Declaring the function, f(x) = x2 + 2x
            double f_of_x;
            f_of_x = (x * x + (2 * x));
            return f_of_x;
            }

        /// Method: Trapezoidal Rule
        static double RuleTrapezoidal(double a,double b, int n)
            {
            ///Sub interval, h = (b-a)/n
            double h = (b - a) / n;

            ///sum of first and last terms: y0 + yn 
            double s = y(a) + y(b);

            ///sum of middle terms: y1 + y2 + y3 + ... + yn-1
            for (int i = 1; i < n; i++)
                s += 2 * y(a + i * h);

            ///T = h/2[y0 + yn + 2(y1 + y2 + y3 + ... + yn-1)]
            double T = (h / 2) * (s); 

            return T;
            }

        public static void Main()
            {
            Console.BackgroundColor = ConsoleColor.Cyan;
            
            //Our given funciton
            Console.WriteLine("f(x) = x2 + 2x");
            
            Console.BackgroundColor = ConsoleColor.Red;
            
            // Upper limit b, Lower limit a
            Console.Write("Enter the Lower Limit: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter the Upper Limit: ");
            double b = Convert.ToDouble(Console.ReadLine());

            //Interval n, the more interval the more accuracy
            Console.Write("Enter the Interval: ");
            int n = Convert.ToInt32(Console.ReadLine());

            Console.BackgroundColor = ConsoleColor.Yellow;

            //Result integration
            double integral = Math.Round(RuleTrapezoidal(a, b, n));
            Console.WriteLine("Integration of the above equation in the range of [{0} , {1}] = {2}",a,b,integral);

            Console.BackgroundColor = ConsoleColor.White;
            }
        }
    }
