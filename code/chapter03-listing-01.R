Tfield <- function(x,y) 20+3*x^2+2*y^2
x <- seq(-2,2,length.out=120)
y <- seq(-2,2,length.out=120)
z <- outer(x,y,Tfield)
contour(x,y,z,levels=c(22,24,26,30,34),
        xlab="x (m)",ylab="y (m)")
stopifnot(Tfield(1,-2)==31)
