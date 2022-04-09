
<h3 align="center">Artificial Intelligence CSC 74011 Assignment 2.2 Solving Sudoku using Backtracking Search with MRV and Forward Checking</h3>

---

<p> In this assignment, we solve sudou puzzles by first reducing the domain with AC-3 then passing the remaining domains to a Backtracking search with minimum remaining value and forward checking heuristics. 

The search is tested using 400 puzzles from `sudokus_start.txt`, and solves all 400 of them sucessfully. 

<img src='img\BAR.png'>
    
| |Time (seconds)|
|-|-|
|Total time:|61.125|
|Average time:|0.1528125|
|Standard dev:|$\pm$ 0.111153|
|Min time:|0.046875|
|Max time:|1.015625|
</p>


##  Getting Started <a name = "getting_started"></a>

Given a sudoku board, the input is a txt file with the board represented as a single line of text, starting from the top-left corner of the board, listed left-to-right, top-to-bottom.


<img src='img\sampleboard.png'>
The following first board is represented by
`809501736207063000160000000000090407090307020706080000000000063000930502532604809`


The program is executed as follows
```
$ python driver_3.py <input_string>
```

The program prints the solution board as well as outputs a file callled `output.txt` which will contain the solution to your input.

### Prerequisites
 `queue` `timeit`

## Author
Nancy Sea

