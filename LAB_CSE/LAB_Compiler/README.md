# Top down parser with backtracking.
The aim of the project was to build a syntax anaylzer following production rules defined by the context free grammar. top-down parser with backtracking. It processed the input string and starts producting the parse tree from the top to the bottom. If one derviation of the tree fails it recursively comes back up and tries to use different rule. In case there are no more production rules - input string is not accepted. The input string may be processed several times to find the right derviation tree (production rules).  

## Build&run  
The program requires python3.   
Go to source directory and execute: 
```sh
python3 main.py
```

## Description
The program asks for CFG file. After valid CFG is provided, the program asks for input string.  
After validation is successful the input is parsed. At each parsing stage the current parsing tree is printed to the terminal.  
When parsing is finished there is printed information about input string being accepted by the provided CFG and final parsing tree.  

## Testing  
You can find more [here.](https://github.com/Kjablonska/Top-down-parser/blob/main/tests/Tests_with_results.pdf)


