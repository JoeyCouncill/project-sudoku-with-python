% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
%each cell(X,Y) contains one number N 1..9
1 {sudoku(X, Y, N) : N = 1..9} 1 :- X = 1..9, Y = 1..9.

%check that the initial values line up
sudoku(X, Y, N) :- initial(X, Y, N).

%each number appears only once in each row
:- sudoku(X, Y1, N), sudoku(X, Y2, N), Y1 != Y2.

%each number appears only onc in each column
:- sudoku(X1, Y, N), sudoku(X2, Y, N), X1 != X2.

%cells are mapped to appropriate subgrid
subgrid(X, Y, G) :- X = 1..9, Y = 1..9, G = 1+(((X-1)/3)*3+(Y-1)/3).

%each number appears only once in each subgrid
:- sudoku(X1, Y1, N), sudoku(X2, Y2, N), subgrid(X1, Y1, G), subgrid(X2, Y2, G), X1 != X2, Y1 != Y2.

#show sudoku/3.