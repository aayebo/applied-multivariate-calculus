heat_ftcs <- function(N=41, alpha=0.1, T=0.2) {
  x <- seq(0, 1, length.out=N); h <- x[2]-x[1]
  steps <- ceiling(T*alpha/(0.4*h^2))
  dt <- T/steps; r <- alpha*dt/h^2
  u <- sin(pi*x)
  for (k in seq_len(steps)) {
    v <- u
    v[2:(N-1)] <- u[2:(N-1)] + r*(
      u[1:(N-2)]-2*u[2:(N-1)]+u[3:N])
    u <- v
  }
  exact <- exp(-alpha*pi^2*T)*sin(pi*x)
  list(h=h, error=max(abs(u-exact)), r=r)
}
print(heat_ftcs())
stopifnot(heat_ftcs()$r <= 0.5)
