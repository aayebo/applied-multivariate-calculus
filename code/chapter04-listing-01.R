f <- function(x,y) exp(x+2*y)
t1 <- function(x,y) 1+x+2*y
t2 <- function(x,y) 1+x+2*y+.5*(x+2*y)^2
print(c(exact=f(.1,.05),linear=t1(.1,.05),
        quadratic=t2(.1,.05)))
h <- 10^seq(-3,-1,length.out=25)
plot(h,abs(f(h,h)-t2(h,h)),log="xy",type="b",
     xlab="Step size",ylab="Quadratic error")
