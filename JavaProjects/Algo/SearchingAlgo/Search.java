//What we will learn so far:
//1. linear search
//2. binary search
//3. interpolation search

public class Search {

    /*
    ///1. linear Search
    *Iterate through a collection one element at a time
    *runtime complexity: O(n)
    #Disadvantages :
    1. Slow for large data sets
    #Advantages :
    1. Fast for searches of small to medium data sets
    2. Does not need to sorted
    3. Useful for data structures that do not have random access (Linked List)
    */
    public static int LinearSearch(int array[], int targetValue) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == targetValue) {
                return i;
            }
        }
        return -1;
    }
    
    /*
    ///2. Binary Search
    1. Search algorithm that finds the position of a target value within a SORTED array. 
    2. Half of the array is eliminated during each "step"
    #runtime complexity: O(logn)
    */
    public static int BinarySearch(int array[], int targetValue) {
        int indexfound = -1;
        int indexlow = 0;
        int indexhigh = array.length - 1;

        while (indexlow <= indexhigh) {

            
            int indexmiddle = (indexlow + indexhigh) / 2;
            //int indexmiddle =indexlow + (indexhigh-indexlow)/2;
            System.out.print("Low index= " + indexlow + ", High index= " + indexhigh);
            System.out.print(", Middle index= " + indexmiddle);
            System.out.println(" Middle element= " + array[indexmiddle]);

            if (targetValue > array[indexmiddle])
                indexlow = indexmiddle + 1;
            else if (targetValue < array[indexmiddle])
                indexhigh = indexmiddle - 1;
            else//(targetValue == array[indexmiddle])
            {
                indexfound = indexmiddle;
                break; //when mid element matches
                
                //indexhigh = indexmiddle - 1; //find for the leftmost match
                //indexlow  = indexmiddle + 1;  //find for the rightmost match
            }
            
        }

        return indexfound;
    }

    /*
    ///3. Interpolation Search
    It is an improvement over binary search best used for SORTED and UNIFORMLY Distributed array.
    'guesses" where a value might be based on calculated probe results.
    if probe is incorrect, search area is narrowed, and a new probe is calculated
    #best base: O(1)
    #average case: O(log(log(n)))
    #worst case: O(n) [values increase exponentially]
    
    //Uniformly distrubuted data: [1,2,3,4,5], orthat holo shomantor dhara hote hobe
    //eikhetre best case
    
    //un-Uniformly distrubuted data: [1,3,7,8,13] diff of consicutive element [2,4,1,5]
    //un-Uniformly and exponentially increase data: [2,4,8,16], gunottor dhara 
    
    ///Interpolation Search VS Binary Search
    However, there are some key differences between interpolation search and binary search:
    
    1.Interpolation search estimates the position of the target element based on the values of the elements surrounding it, while binary search always starts by checking the middle element of the list. Binary->mid while Interpolation-> probe
    
    2. Interpolation search is more efficient than binary search when the elements in the list are uniformly distributed, while binary search is more efficient when the elements in the list are not uniformly distributed.
    
    3. Interpolation search can take longer to implement than binary search, as it requires the use of additional calculations to estimate the position of the target element.
    
    4.Interpolation search works in a way we search for a word in a dictionary. The interpolation search algorithm improves the binary search algorithm.  The formula for finding a value is: K = data-low/high-low. K is a constant which is used to narrow the search space. In the case of binary search, the value for this constant is: K=(low+high)/2.
    
    //The formula for pos can be derived as follows:
    There are many different interpolation methods and one such is known as linear interpolation. Linear interpolation takes two data points which we assume as (x1,y1) and (x2,y2) and the formula is :  at point(x,y).
    
    Let's assume that the elements of the array are linearly distributed. 
    General equation of line : y = m*x + c.
    
    y is the value in the array and x is its index.
    Now putting value of lo,hi and x in the equation
    
    arr[hi] = m*hi+c ----(1)
    arr[lo] = m*lo+c ----(2)
    x = m*pos + c    ----(3)
    
    m = (arr[hi] - arr[lo] )/ (hi - lo)
    
    subtracting eqxn (2) from (3)
    x - arr[lo] = m * (pos - lo)
    lo + (x - arr[lo])/m = pos
    pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])
    */

    public static int InterpolationSearch(int array[], int targetValue) {
        int indexfound = -1;
        int indexlow = 0;
        int indexhigh = array.length - 1;

        while (indexlow <= indexhigh && targetValue >= array[indexlow] && targetValue <= array[indexhigh]) {

            //Binary Search has sharp middle index 
            //In Interpolation Search has guess or probable index surrounding the targeted element
            int indexprobe = indexlow + (((targetValue - array[indexlow]) * (indexhigh - indexlow))
                    / (array[indexhigh] - array[indexlow]));
            System.out.print("Low index= " + indexlow + ", High index= " + indexhigh);
            System.out.print(", Probe index= " + indexprobe);
            System.out.println(" Probe element= " + array[indexprobe]);

            if (targetValue > array[indexprobe])
                indexlow = indexprobe + 1;
            else if (targetValue < array[indexprobe])
                indexhigh = indexprobe - 1;
            else//(targetValue == array[indexprobe])
            {
                indexfound = indexprobe;
                break; //when mid element matches

                //indexhigh = indexprobe - 1; //find for the leftmost match
                //indexlow  = indexprobe + 1;  //find for the rightmost match
            }

        }

        return indexfound;
    }


//==============================================Main============================================//

    public static void main(String[] args) {
        //------------------------------*Linear Search*------------------------------------//
        // int array[] = { 1, 5, 3, 4, 2 };
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(i+" ");    
        // } System.out.println();
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");    
        // }
        // int search = 2;
        //System.out.println("\nThe Element,"+search+" found at index: " + LinearSearch(array, search));
        //------------------------------*End Linear Search*------------------------------------//
        
        //------------------------------*Binary Search*------------------------------------//
        //int arraysorted[] = {1,1,2,2,4,8,12,12};
        //int arraysorted[] = { 2, 2, 2, 2, 2, 2, 2, 2, 2 };
        //int arraysorted[] = {1,2,3};

        //int arraysorted[]=new int[10];
        // for (int i = 0; i < arraysorted.length; i++) {
        //     arraysorted[i] = i*2+1;
        //     System.out.print(i+" ");    
        // } System.out.println();
        // for (int i = 0; i < arraysorted.length; i++) {
        //     System.out.print(arraysorted[i] + " ");
        // }System.out.println();

        // int search = 2;
        // System.out.println("The Element,"+search+" found at index: " + BinarySearch(arraysorted, search));
        //------------------------------*End Binary Search*------------------------------------//

        //---------------------------*Interpolation Search*--------------------------------//
        //int arrayuniformsorted[] = {1,2,3,4}; //best case example
        int arrayuniformsorted[] = {1,2,4,8,16,32}; //worst case example
        for (int i = 0; i < arrayuniformsorted.length; i++) {
            System.out.print(arrayuniformsorted[i] + " ");
        }System.out.println();

        int search = 32;
        System.out.println("The Element,"+search+" found at index: " + InterpolationSearch(arrayuniformsorted, search));

        //---------------------------*End Interpolation Search*--------------------------------//

    }
}
