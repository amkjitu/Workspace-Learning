using System;
namespace NumericalMethods
    {
    class Simpson_sOneThirdRule
        {
        static double y(double x)
            {
            ///Declaring the function, f(x) = x2 + 2x
            double f_of_x;
            f_of_x = (x * x + (2 * x));
            return f_of_x;
            }

        /// Method: Simpsons1_3 Rule
        static double RuleSimpsons1_3(double a, double b, int n)
            {
            ///Sub interval, h = (b-a)/n
            double h = (b - a) / n;

            ///sum of first and last terms: y0 + yn 
            double s = y(a) + y(b);

            ///sum of middle terms: y1 + y3 + y5 + ... + yn-1
            for (int i = 1; i < n; i=i+2)
                s += 4 * y(a + i * h);

            ///sum of middle terms: y2 + y4 + y6 + ... + yn-2
            for (int i = 2; i < n; i = i + 2)
                s += 2 * y(a + i * h);

            ///S = h/3[y0 + yn + 4(y1 + y3 + y5 + ... + yn-1) + 2(y2 + y4 + y6 + ... + yn-2)]
            double T = (h / 3) * (s);

            return T;
            }

        public static void Main()
            {
            Console.WriteLine("Simpson's 1/3 Rule");
            Console.BackgroundColor = ConsoleColor.Cyan;

            //Our given funciton
            Console.WriteLine("f(x) = x2 + 2x");

            Console.BackgroundColor = ConsoleColor.Red;

            // Upper limit b, Lower limit a
            Console.Write("Enter the Lower Limit: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter the Upper Limit: ");
            double b = Convert.ToDouble(Console.ReadLine());
            int n=0;
            void ValidInput()
                {
                //Interval n, the more interval the more accuracy
                Console.WriteLine("The Intervals must be even");
                Console.Write("Enter the Interval: ");
                n = Convert.ToInt32(Console.ReadLine());
                }

            ValidInput();
            int check = n % 2;
            while (check != 0)
                {
                check = n % 2;
                if (check == 0)
                    break;
                else
                ValidInput();
                }

            Console.BackgroundColor = ConsoleColor.Yellow;

            //Result integration
            double integral = Math.Round(RuleSimpsons1_3(a, b, n));
            Console.WriteLine("Integration of the above equation in the range of [{0} , {1}] = {2}", a, b, integral);

            Console.BackgroundColor = ConsoleColor.White;
            }
        }
    }
