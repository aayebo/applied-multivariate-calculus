centered <- function(h) (sin(1+h)-sin(1-h))/(2*h)
h <- 10^seq(-1, -7, by = -1)
approximation <- vapply(h, centered, numeric(1))
error <- abs(approximation-cos(1))
results <- data.frame(h = h, estimate = approximation,
                      absolute_error = error)
print(results, digits = 8)
plot(h, error, log = "xy", type = "b",
     xlab = "Step size h", ylab = "Absolute error")
