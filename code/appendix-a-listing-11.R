x <- seq(-2, 2, length.out = 401)
y <- x^3 - 3*x
plot(x, y, type = "l", lwd = 2,
     xlab = "x", ylab = "f(x)",
     main = "A cubic function")
abline(h = 0, v = 0, lty = 3)
points(c(-1, 1), c(2, -2), pch = 19)
