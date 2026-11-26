heat_ftcs <- function(N = 40, T = 0.2, alpha = 0.1) {
  x <- seq(0, 1, length.out = N + 1)
  h <- 1 / N
  steps <- ceiling(T * alpha / (0.4 * h^2))
  dt <- T / steps
  r <- alpha * dt / h^2
  u <- sin(pi * x)
  for (step in seq_len(steps)) {
    v <- u
    v[2:N] <- u[2:N] + r *
      (u[1:(N-1)] - 2*u[2:N] + u[3:(N+1)])
    u <- v
  }
  exact <- exp(-alpha*pi^2*T) * sin(pi*x)
  c(h=h, r=r, error=max(abs(u-exact)))
}
print(heat_ftcs())
