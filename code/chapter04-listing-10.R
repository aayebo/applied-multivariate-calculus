q <- function(z) (z[1]-2)^2+4*(z[2]+1)^2
grad <- function(z) c(2*(z[1]-2),8*(z[2]+1))
z <- c(0,3); alpha <- 1/8
path <- matrix(z,nrow=1)
for (k in 1:100) {
  z <- pmax(0,z-alpha*grad(z))
  path <- rbind(path,z)
}
print(c(x=z[1],y=z[2],objective=q(z)))
stopifnot(max(abs(z-c(2,0)))<1e-10)
plot(path[,1],path[,2],type='o',pch=16,
     xlab='x',ylab='y',main='Projected gradient iterates')
