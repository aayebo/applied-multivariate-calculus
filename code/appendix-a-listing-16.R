f <- function(x, y) x^2 + x*y + 2*y^2
a <- 1; b <- -1
fx <- function(x, y) 2*x + y
fy <- function(x, y) x + 4*y
L <- function(x, y) {
  f(a, b) + fx(a, b)*(x-a) + fy(a, b)*(y-b)
}
c(exact = f(1.1, -0.9), linear = L(1.1, -0.9))
