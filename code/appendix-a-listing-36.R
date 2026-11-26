f <- function(p) 0.5*(4*p[1]^2 + 2*p[2]^2)
grad <- function(p) c(4*p[1], 2*p[2])
eta <- 0.2
p <- c(3, -2)
history <- matrix(NA_real_, nrow = 31, ncol = 3)
colnames(history) <- c("x", "y", "objective")
for (k in 0:30) {
  history[k+1, ] <- c(p, f(p))
  if (k < 30) p <- p - eta*grad(p)
}
plot(0:30, history[, "objective"], type = "b",
     xlab = "Iteration", ylab = "Objective value")
stopifnot(tail(history[,"objective"],1) < 1e-8)
