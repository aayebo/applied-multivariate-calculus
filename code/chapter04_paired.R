f <- function(x,y) exp(x+2*y)
t1 <- function(x,y) 1+x+2*y
t2 <- function(x,y) 1+x+2*y+.5*(x+2*y)^2
print(c(exact=f(.1,.05),linear=t1(.1,.05),quadratic=t2(.1,.05)))
h <- 10^seq(-3,-1,length.out=25)
plot(h,abs(f(h,h)-t2(h,h)),log="xy",type="b",xlab="Step size",ylab="Quadratic error")
q <- function(p) (p[1]-2)^2+4*(p[2]+1)^2+3
grad <- function(p) c(2*(p[1]-2),8*(p[2]+1))
fit <- optim(c(0,0),q,gr=grad,method="BFGS")
print(c(fit$par,minimum=fit$value))
stopifnot(max(abs(fit$par-c(2,-1)))<1e-5)
nonconvex <- function(p) (p[1]^2-1)^2+p[2]^2
starts <- list(c(-2,1),c(2,1),c(-.7,-1),c(.7,-1))
print(do.call(rbind,lapply(starts,function(s) c(optim(s,nonconvex,method="BFGS")$par))))
angle <- optimize(function(t) -(cos(t)+2*sin(t)),c(0,2*pi))
print(c(disk_max=-angle$objective,exact=sqrt(5)))
fixed_sum <- optimize(function(x) -x*(10-x),c(0,10))
print(c(x=fixed_sum$minimum,y=10-fixed_sum$minimum,product=-fixed_sum$objective))
x <- c(0,1,2,3);y <- c(1,2,2,4);X <- cbind(1,x)
print(qr.solve(X,y));print(coef(lm(y~x)))
stopifnot(max(abs(qr.solve(X,y)-c(.9,.9)))<1e-10)
P <- function(p) 12*p[1]+10*p[2]-p[1]^2-2*p[2]^2-p[1]*p[2]
fit <- optim(c(1,1),function(p) -P(p),method="BFGS")
print(c(fit$par,benefit=P(fit$par)))
print(c(exact_x=38/7,exact_y=8/7))
