f <- function(x, y) x^2 + 2*y^2
linear <- function(h, k) 1.5 + 2*h + 2*k
h <- c(0.2, 0.1, 0.05, 0.025)
k <- h / 2
actual <- f(1+h, 0.5+k)
error <- abs(actual - linear(h, k))
bound <- 2*(h^2 + k^2)
print(data.frame(h, k, error, bound))
stopifnot(all(error <= bound + 1e-12))
