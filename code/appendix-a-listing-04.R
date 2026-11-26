cross3 <- function(a, b) {
  stopifnot(length(a) == 3, length(b) == 3)
  c(a[2]*b[3] - a[3]*b[2],
    a[3]*b[1] - a[1]*b[3],
    a[1]*b[2] - a[2]*b[1])
}
a <- c(1, 2, 0)
b <- c(0, 1, 3)
cross3(a, b)
sum(cross3(a, b) * a)    # zero: orthogonality
