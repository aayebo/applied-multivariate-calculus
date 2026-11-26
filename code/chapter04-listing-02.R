q <- function(p) (p[1]-2)^2+4*(p[2]+1)^2+3
grad <- function(p) c(2*(p[1]-2),8*(p[2]+1))
fit <- optim(c(0,0),q,gr=grad,method="BFGS")
print(c(fit$par,minimum=fit$value))
stopifnot(max(abs(fit$par-c(2,-1)))<1e-5)
