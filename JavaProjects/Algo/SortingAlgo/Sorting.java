/////What we will learn so far:
//https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/
//1.Bubble Sort
//2.Selection Sort
//3.Insertion Sort 
//4.Recursion
//5.Merge Sort
//6.Quick Sort

import javax.swing.plaf.basic.BasicBorders.FieldBorder;

public class Sorting {
   
    /* 
    ///1.Bubble Sort
    In bubble sort pairs of adjacent elements are compared and the elements swapped if they are not in order.
    *At first iteration Maximum element places at the last position
    *At Second iteration second Maximum element places at the second last position, and so on.
    *Quadratic time O(n^2)
    *small data set = okay-ish
    *large data set = bad 
    */

    public static void BubbleSort(int array[]) {

        //prothom loop er iteration determine kore koto guli element sort korte hobe
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - 1; j++) {

                //ascending order
                if (array[j] > array[j + 1]) {
                    //Swap
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }

                //descending order
                // if (array[j]<array[j+1]) {
                       //Swap
                //     int temp = array[j];
                //     array[j] = array[j + 1];
                //     array[j + 1] = temp;
                // }
            }

        }

    }
    
    /* 
    ///2.Selection Sort
    In selection sort, search through an array and keep track of the minimum value during each iteration(minimum value element er index ta khuje ber kore). At the end of each iteration, we swap variables(ith index value abong minimum value index moddhe swap hoy).
    *At first iteration Minimum element places at the first position
    *At Second iteration second Minimum element places at the second positoin, and so on.
    *Quadratic time O(n^2)
    *small data set = okay
    *large data set = BAD
    */

    public static void SelectionSort(int array[]) {

        //prothom loop er iteration determine kore koto guli element sort korte hobe
        for (int i = 0; i < array.length; i++) {
            int min = i;
            for (int j = i + 1; j < array.length; j++) {

                //ascending order
                if (array[min] > array[j]) {
                    min = j;
                }

                //descending order
                // if (array[min] < array[j]) {
                //    min = j;
                // }
            }

            //Swap
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;

        }

    }
    
        /* 
        ///3.Insertion Sort
        In insertion sort, after comparing elements to the left, shift elements to the right to make room to insert a value. It seems like a card sorting. We peck one value, compare it to the left elements and move the elements to right where one value was taken form and this it will have a room to put it to the position where that value is smaller than the element.
        *Run-time complexity O(n^2)
        *small data set = okay
        *large data set = BAD
        Less steps than Bubble Sort
        #Best case is O(n) compared to selection sort O(n^2)
        #Best Case Scenerio: 1 2 3 4 5 [already sorted]
        #Worst case is O(n^2)
        #Worst Case Scenerio: 5 4 3 2 1 [reversely sorted]
        */
    
        public static void InsertionSort(int array[]) {

            //prothom loop er iteration determine kore koto guli element sort korte hobe
            for (int i = 1; i < array.length; i++) {
                int current = array[i];
                int j = i - 1;
                while (j >= 0 && current < array[j]) {
                    array[j + 1] = array[j];
                    j--;
                }
                array[j + 1] = current;

            }

        }
       
    /*     
    ///4.Recursion
    // Recursion is, when a thing is defined in terms of itself.
    // Apply the result of a procedure, to a procedure.
    // A recursive method calls itself. Can be a substitute for iteration.
    // Divide a problem into sub-problems of the same type as the original.
    // Commonly used with advanced sorting algorithms and navigating trees
    // #Recursion has to case:
    // 1.Base case: stops the recursion
    // 2.Recursive case: continues the recursion
    // #Advantages
    // 1.easier to read/write
    // 2.easier to debug
    // #Disadvantages
    // 1.sometimes slower
    // 2.uses more memory
    // 3.may cause stack overflow
    */
    
    //4a.Factorial using recursion
    public static int factorial(int n) {
        if (n == 1)
            return 1; //base case
        return n * factorial(n - 1); //recursive case
    }
    
    //4b.Power using recursion
    public static int power(int x, int n) {

        if (n == 1)
            return 2; //base case
        return x * power(x, n - 1); //recursive case
    }

    //4c.Fibonacci series using recursion
    public static int Fibonacci(int n) {
        if (n == 1)
            return 0; //base case 1
        if (n == 2)
            return 1; //base case 2
        return Fibonacci(n - 1) + Fibonacci(n - 2); //resursive case
    }

    ///5. Merge Sort
    /*
    In merge sort, recursively divides array in 2 until having only one element of array, then sorts, re-combines.
    *Divide and Conquare technique
    *Run-time complexity = O(n Log n) for all cases
    *space complexity = O(n)
    */

    public static void MergeSort(int[] array) {
        
        int length = array.length;
        if (length <= 1)
            return;
        
        int middle = length / 2;
        int[] leftArray = new int[middle];
        int[] rightArray = new int[length - middle];
        
        int i = 0;
        int j = 0;

        while (i < length) {
            if (i < middle) {
                leftArray[i] = array[i];
            } else {
                rightArray[j] = array[i];
                j++;
            }

            i++;
        }
        
        MergeSort(leftArray);
        MergeSort(rightArray);
        merge(leftArray, rightArray, array);

    }
    
    public static void merge(int[] leftArray, int[] rightArray, int[] array) {
        int leftSize = array.length / 2;
        int rightSize = array.length - leftSize;
        int i = 0, l = 0, r = 0; //indices for array, left array, right array

        //check conditions for merging
        while (l < leftSize && r < rightSize) {
            if (leftArray[l] < rightArray[r]) {
                array[i] = leftArray[l];
                i++;
                l++;
            } else {
                array[i] = rightArray[r];
                i++;
                r++;
            }

        }

        while (l < leftSize) {
            array[i] = leftArray[l];
            i++;
            l++;
        }

        while (r < rightSize) {
            array[i] = rightArray[r];
            i++;
            r++;
        }

    }
    
    ///5. Quick Sort
    /*
    In quick sort, moves smaller elements to left of a pivot. recursively divide array in 2 partitions.
    *Divide and Conquare technique
    *Best case O(n log(n))
    *Average case O(n log(n))
    *Worst case O(n^2) if already sorted
    *Space complexity - O(log(n)) due to recursion
    */

    public static void QuickSort(int[] array, int start, int end) {
        if (end <= start)
            return; //base case
        
        int pivot = partition(array, start, end);
        QuickSort(array, start, pivot - 1); 
        QuickSort(array, pivot + 1, end);
         
    }
    
    public static int partition(int[] array,int start,int end) {
        int pivot = array[end];
        int i = start - 1;

        for (int j = start; j <= end - 1; j++) {
            if (array[j] < pivot) {
                i++;
                //swap
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        i++;
        //swap
        int temp = array[i];
        array[i] = array[end];
        array[end] = temp;
        
        return i;
    }




//================================================Main==========================================//
    public static void main(String[] args) {

        //------------------------------*Bubble Sort*------------------------------------//
    
        // int array[] = { 9, 2, 1, 8, 4, 7, 6, 3, 5 };

        // System.out.println("Original Array: ");
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();

        // System.out.println("Bubble Sorted Array: ");
        // BubbleSort(array);
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();
        //------------------------------*End Bubble Sort*------------------------------------//

        //------------------------------*Selection Sort*------------------------------------//
    
        // int array[] = { 9, 2, 1, 8, 4, 7, 6, 3, 5 };

        // System.out.println("Original Array: ");
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();

        // System.out.println("Selection Sorted Array: ");
        // SelectionSort(array);
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();
        //------------------------------*End Selection Sort*------------------------------------//

        //------------------------------*Insertion Sort*------------------------------------//
    
        // int array[] = { 9, 2, 1, 8, 4, 7, 6, 3, 5 };

        // System.out.println("Original Array: ");
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();

        // System.out.println("Insertion Sorted Array: ");
        // InsertionSort(array);
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();
        //------------------------------*End Insertion Sort*------------------------------------//

        //---------------------------------*Recursion*------------------------------------//
        
        //System.out.println(factorial(5));
        //System.out.println(power(2,8));
        //System.out.println(Fibonacci(7));
        //---------------------------------*End Recursion*------------------------------------//

        //------------------------------*Merge Sort*------------------------------------//
    
        // int array[] = { 9, 2, 1, 8, 4, 7, 6, 3, 5 };

        // System.out.println("Original Array: ");
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();

        // System.out.println("Merge Sorted Array: ");
        // MergeSort(array);
        // for (int i = 0; i < array.length; i++) {
        //     System.out.print(array[i]+" ");
        // }
        // System.out.println();
        //------------------------------*End Merge Sort*------------------------------------//

        //------------------------------*Quick Sort*------------------------------------//
    
        int array[] = { 9, 2, 1, 8, 4, 7, 6, 3, 5 };

        System.out.println("Original Array: ");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]+" ");
        }
        System.out.println();

        System.out.println("Quick Sorted Array: ");
        QuickSort(array,0,array.length-1);
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]+" ");
        }
        System.out.println();
        //------------------------------*End Quick Sort*------------------------------------//
    }
    

}
