# Chapter 5 expanded comparison benchmarks (base R)
midpoint <- function(n) {
  m <- ((1:n)-0.5)/n
  sum(outer(m,m,function(x,y) x^2+y^2))/n^2
}
for (n in c(4,8,16,32,64)) {
  err <- abs(midpoint(n)-2/3)
  stopifnot(abs(err-1/(6*n^2))<1e-12)
}
I <- integrate(function(y) y^2*exp(y^3),0,1)$value
stopifnot(abs(I-(exp(1)-1)/3)<1e-10)
I0 <- 8
IC <- I0-4*((7/6)^2+(1/2)^2)
stopifnot(abs(IC-14/9)<1e-12)
cat('Expanded Chapter 5 mathematical benchmarks passed.\n')
