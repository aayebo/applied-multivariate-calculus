heat_ftcs <- function(N=40, T=0.2, alpha=0.1) {
  x <- seq(0,1,length.out=N+1); h <- 1/N
  steps <- ceiling(T*alpha/(0.4*h^2)); dt <- T/steps
  r <- alpha*dt/h^2; u <- sin(pi*x)
  for (step in seq_len(steps)) {
    v <- u
    v[2:N] <- u[2:N] + r*(u[1:(N-1)]-2*u[2:N]+u[3:(N+1)])
    u <- v
  }
  exact <- exp(-alpha*pi^2*T)*sin(pi*x)
  c(h=h, r=r, error=max(abs(u-exact)))
}
results <- t(sapply(c(20,40,80,160),heat_ftcs))
print(results)
stopifnot(all(results[,"r"] <= 0.5))
orders <- log(results[-4,"error"]/results[-1,"error"])/log(2)
print(orders)
stopifnot(all(orders>1.8 & orders<2.2))
