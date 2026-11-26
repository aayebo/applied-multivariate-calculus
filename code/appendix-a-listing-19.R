objective <- function(p) {
  x <- p[1]; y <- p[2]
  (x - 1)^2 + 2*(y + 2)^2
}
gradient <- function(p) {
  c(2*(p[1] - 1), 4*(p[2] + 2))
}
fit <- optim(par = c(0, 0), fn = objective,
             gr = gradient, method = "BFGS")
fit$par
fit$value
fit$convergence            # zero typically indicates convergence
