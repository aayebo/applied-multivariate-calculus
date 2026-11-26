L <- 1; kappa <- 0.1
nx <- 51
x <- seq(0, L, length.out = nx)
dx <- x[2] - x[1]
lambda <- 0.4
dt <- lambda*dx^2/kappa
nt <- 100
u <- sin(pi*x)
u[1] <- 0; u[nx] <- 0
for (step in 1:nt) {
  old <- u
  u[2:(nx-1)] <- old[2:(nx-1)] + lambda*(
    old[1:(nx-2)] - 2*old[2:(nx-1)] + old[3:nx])
  u[1] <- 0; u[nx] <- 0
}
time <- nt*dt
exact <- exp(-kappa*pi^2*time)*sin(pi*x)
cat("Maximum absolute error:", max(abs(u-exact)), "\n")
plot(x, u, type = "l", xlab = "Position", ylab = "u(x,t)")
lines(x, exact, lty = 2)
