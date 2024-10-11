using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text;
namespace NumericalMethods
    {
    class LinearRegression
        {
        static void Main()
            {
            int n, i;
            double sumOfx = 0, sumOfx2 = 0, sumOfy = 0, sumXY = 0, a, b;

            Console.BackgroundColor = ConsoleColor.Green;
            Console.Write("Number of the record : ");
            n = Convert.ToInt32(Console.ReadLine());

            double[] x = new double[n+2];
            double[] y = new double[n+2];

            Console.WriteLine("Enter the records");
            Console.WriteLine("---------------------");

            Console.BackgroundColor = ConsoleColor.Cyan;
            for (i = 1; i <= n; i++)
                {
                //cout << "x[" << i << "] = ";
                Console.Write("x[{0}] = ",i);
                x[i] = Convert.ToDouble(Console.ReadLine());

                Console.Write("y[{0}] = ",i);
                y[i] = Convert.ToDouble(Console.ReadLine());
                }
            
            for (i = 1; i <= n; i++)
                {
                sumOfx = sumOfx + x[i];
                sumOfx2 = sumOfx2 + x[i] * x[i];
                sumOfy = sumOfy + y[i];
                sumXY = sumXY + x[i] * y[i];
                }

            b = (n * sumXY - sumOfx * sumOfy) / (n * sumOfx2 - sumOfx * sumOfx);
            a = (sumOfy - b * sumOfx) / n;

            Console.BackgroundColor = ConsoleColor.Yellow;
            //Console.WriteLine("value of b0 = {0} and b1 = {1}",a,b);
            Console.WriteLine("Value of b0 = {0} and b1 = {1}",a.ToString("0.0000", CultureInfo.InvariantCulture), b.ToString("0.0000", CultureInfo.InvariantCulture));
            //Console.WriteLine("Equation for the linear regression : y = {0} + {1}x",a,b);
            Console.WriteLine("Equation for the linear regression : y = {0} + {1}x", a.ToString("0.0000", CultureInfo.InvariantCulture), b.ToString("0.0000", CultureInfo.InvariantCulture));
            Console.BackgroundColor = ConsoleColor.White;
            }
        }
    }
