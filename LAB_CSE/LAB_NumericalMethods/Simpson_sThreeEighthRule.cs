using System;
using System.Collections.Generic;
using System.Text;

namespace NumericalMethods
    {
    class Simpson_sThreeEighthRule
        {
        static double y(double x)
            {
            ///Declaring the function, f(x) = x2 + 2x
            double f_of_x;
            f_of_x = (x * x + (2 * x));
            return f_of_x;
            }

        /// Method: Simpsons3_8 Rule
        static double RuleSimpsons3_8(double a, double b, int n)
            {
            ///Sub interval, h = (b-a)/n
            double h = (b - a) / n;

            ///sum of first and last terms: y0 + yn 
            double s = y(a) + y(b);

            ///sum of middle terms: y1 + y2 + y4 + y5 + ...
            for (int i = 1; i < n; i++)
                {
                if (i % 3 == 0)
                    {
                    s += 2 * y(a + i * h);
                    }
                else
                    {
                    s += 3 * y(a + i * h);
                    }
                }
               
            ///S =3 h/8[y0 + yn + 3(y1 + y2 + y4 +y5 + ...) + 2(y3 + y6 + y9 + ...)]
            double T = ((3*h) / 8) * (s);

            return T;
            }

        public static void Main()
            {
            Console.WriteLine("Simpson's 3/8 Rule");
            Console.BackgroundColor = ConsoleColor.Cyan;

            //Our given funciton
            Console.WriteLine("f(x) = x2 + 2x");

            Console.BackgroundColor = ConsoleColor.Red;

            // Upper limit b, Lower limit a
            Console.Write("Enter the Lower Limit: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter the Upper Limit: ");
            double b = Convert.ToDouble(Console.ReadLine());
            int n = 0;
            void ValidInput()
                {
                //Interval n, the more interval the more accuracy
                Console.WriteLine("The Intervals must be the multiple of 3");
                Console.Write("Enter the Interval: ");
                n = Convert.ToInt32(Console.ReadLine());
                }

            ValidInput();
            int check = n % 3;
            while (check != 0)
                {
                check = n % 3;
                if (check == 0)
                    break;
                else
                    ValidInput();
                }

            Console.BackgroundColor = ConsoleColor.Yellow;

            //Result integration
            double integral = Math.Round(RuleSimpsons3_8(a, b, n));
            Console.WriteLine("Integration of the above equation in the range of [{0} , {1}] = {2}", a, b, integral);

            Console.BackgroundColor = ConsoleColor.White;
            }
        }
    }
