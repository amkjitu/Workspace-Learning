using System;
using System.Collections.Generic;
using System.Text;

namespace NumericalMethods
    {
    class Milne_sPredictorCorrectorMethod
        {
        // consider the differential equation 
        // for a given x and y, return v 
        static double f(double x, double y)
            {
            double v = 0.5*(x+y);
            return v;
            }

        // predicts the next value for a given (x, y) 
        static double predict(double x, double y, double h)
            {
            // value of next y(predicted) is returned 
            double y1p = y + h * f(x, y);
            return y1p;
            }
        static double correct(double x, double y,
                    double x1, double y1,
                    double h)
            {
            // (x, y) are of previous step 
            // and x1 is the increased x for next step 
            // and y1 is predicted y for next step 
            double e = 0.00001;
            double y1c = y1;

            do
                {
                y1 = y1c;
                y1c = y + 0.5 * h * (f(x, y) + f(x1, y1));
                }
            while (Math.Abs(y1c - y1) > e);

            // every iteration is correcting the value 
            // of y using average slope 
            return y1c;
            }

        static void printFinalValues(double x, double xn,
                            double y, double h)
            {

            while (x < xn)
                {
                double x1 = x + h;
                double y1p = predict(x, y, h);
                double y1c = correct(x, y, x1, y1p, h);
                x = x1;
                y = y1c;
                }

            // at every iteration first the value 
            // of for next step is first predicted 
            // and then corrected. 
            Console.WriteLine("The final value of y at x = " +
                                x + " is : " + Math.Round(y, 5));
            }

        // Driver code 
        static void Main()
            {
            // here x and y are the initial 
            // given condition, so x=0 and y=2 
            double x = 0, y = 2;

            // final value of x for which y is needed 
            double xn = 2;

            // step size 
            double h = 0.5;
            Console.WriteLine("Given Equation: y` = 1/2(x+y)");
            printFinalValues(x, xn, y, h);
            }
        }
    }
