A <- matrix(c(2, 1, 1, 3), nrow = 2, byrow = TRUE)
b <- c(5, 7)
A
nrow(A); ncol(A)
t(A)                       # transpose
det(A)                     # determinant
solve(A, b)                # solve A x = b
A %*% solve(A, b)          # verify solution
