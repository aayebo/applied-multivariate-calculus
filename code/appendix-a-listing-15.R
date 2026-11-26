f <- function(x, y) x^2*y + sin(x*y)
h <- 1e-5
fx <- (f(1+h, 2) - f(1-h, 2))/(2*h)
fy <- (f(1, 2+h) - f(1, 2-h))/(2*h)
cat("Approximate gradient:", fx, fy, "\n")
