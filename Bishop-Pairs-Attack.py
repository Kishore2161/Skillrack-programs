"""
The program must accept a matrix of size N*N representing a chessboard. The chessboard contains a certain number of bishops(marked by 1) and the empty squares are marked by the
value 0. In the given chessboard, two bishops attack each other if they share the same diagonal. This includes the bishops that have another bishop located between them
(i.e., bishops can attack through pieces). The program must print the number of pairs of bishops that attack each other.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.

Output Format:
The first line contains the number of pairs of bishops that attack each other.

Example Input/Output 1:
Input:
5
1 0 0 0 0
0 0 1 0 0
0 0 1 0 0
0 0 0 0 0
1 0 0 0 0

Output:
2

Explanation:
The bishops at (1, 1) and (3, 3) attack each other.
Similarly, the bishops at (5, 1) and (3, 3) attack each other.
2 pairs of bishops that attack each other, so 2 is printed as the output.

Example Input/Output 2:
Input:
3
1 1 1
1 1 1
1 1 1

Output:
10
"""
