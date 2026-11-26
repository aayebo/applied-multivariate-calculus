heat_ftcs <- function(N=41, alpha=0.1, T=0.2) {
  x <- seq(0,1,length.out=N); h <- x[2]-x[1]
  steps <- ceiling(T*alpha/(0.4*h^2)); dt <- T/steps
  r <- alpha*dt/h^2; u <- sin(pi*x)
  for (k in seq_len(steps)) {
    v <- u
    v[2:(N-1)] <- u[2:(N-1)] + r*(u[1:(N-2)]-2*u[2:(N-1)]+u[3:N])
    u <- v
  }
  exact <- exp(-alpha*pi^2*T)*sin(pi*x)
  c(h=h,error=max(abs(u-exact)),r=r)
}
values <- t(sapply(c(21,41,81,161),heat_ftcs))
print(values)
stopifnot(all(values[,"r"]>0 & values[,"r"]<=0.5))
stopifnot(all(diff(values[,"error"])<0))
order <- coef(lm(log(values[,"error"])~log(values[,"h"])))[2]
print(c(estimated_order=order))
stopifnot(order>1.8 && order<2.2)
