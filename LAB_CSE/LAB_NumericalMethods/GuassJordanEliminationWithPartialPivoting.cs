using System;
namespace NumericalMethods
    {
    class GuassJordanEliminationWithPartialPivoting
        {
		public static int row_num, col_num;
		//function for partial pivoting 
		static void partially_pivot(double[,] arr, int pivot_row, int pivot_col){
		double temp;
		int i,large_pivot_row = pivot_row;
	
	for(i=pivot_row; i<row_num ; i++){
		//to find greatest among the pivot column column
		if(arr[i,pivot_col]>arr[large_pivot_row,pivot_col]){
			 large_pivot_row = i;
		}
	}
	
	if(pivot_row != large_pivot_row){
		//to interchange the rows
		for(i=0; i<col_num; i++){
			temp = arr[large_pivot_row,i];
			arr[large_pivot_row,i] = arr[pivot_row,i];
			arr[pivot_row,i] = temp;
		}
	}
}

		//function for printing the matrix
	static void printMatrix(double[,] arr){
	int i,j;
	   for(i=0; i<row_num; i++)
		{
		for(j=0; j<col_num; j++)
		{
                    Console.Write(arr[i,j]+ "\t");
		}
                Console.WriteLine();
	}
            Console.WriteLine();
}
        static void Main()
            {
			double [,]  arr=new double[10,10];
			double diagonal_element, flag;
			int i, j, k, l, step = 1;

            Console.WriteLine("Enter the Number of Rows");
			row_num = Convert.ToInt32(Console.ReadLine());

			Console.WriteLine("Enter the Number of Columns");
			col_num = Convert.ToInt32(Console.ReadLine());

			Console.WriteLine("Enter the Items in the Matrix :");
			for (i = 0; i < row_num; i++)
				{
				for (j = 0; j < col_num; j++)
					{
					Console.Write("row {0} column {1} : ",i,j);
					arr[i,j] = Convert.ToInt32(Console.ReadLine());
					Console.WriteLine();
					}
				}

			for (i = 0; i < row_num; i++)
				{
				for (j = 0; j < col_num; j++)
					{
					if (i == j)
						{
						partially_pivot(arr, i, j);

						diagonal_element = arr[i,j];
						k = i;
						l = j;

						for (l = 0; l < col_num; l++)
							{
							//for making the diagonal element 1
							arr[k,l] /= diagonal_element;
							}


						for (k = 0; k < row_num; k++)
							{
							//setting flag = the element on respective row which is exactly below the concerned diagonal element
							flag = arr[k,j];

							for (l = 0; l < col_num; l++)
								if (k != i)
									{
									//performing row operation to male all the elements = 0, except diagonal element 
									arr[k,l] = (arr[k,l]) - flag * (arr[i,l]);
									}
							}
						}
					}
                Console.WriteLine("Step:\t {0}",step);
				printMatrix(arr);
				step++;
				}
			//printing result
			for (i = 0; i < row_num; i++)
                Console.WriteLine("x{0} = {1}",i+1,arr[i,col_num - 1]);
		}
	}
  }
