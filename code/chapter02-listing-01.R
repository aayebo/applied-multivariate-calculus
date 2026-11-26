t <- seq(0, 6*pi, length.out=500)
x <- 2*cos(t); y <- 2*sin(t); z <- t/3
par(mfrow=c(1,2))
plot(x,y,type="l",asp=1,xlab="x",ylab="y",main="Top view")
plot(t,z,type="l",xlab="t",ylab="z",main="Height")
par(mfrow=c(1,1))
