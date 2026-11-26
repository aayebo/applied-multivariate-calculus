rho <- function(x,y) 1+x
inner_y <- function(x, integrand) {
  vapply(x, function(xx) {
    integrate(function(y) integrand(xx,y), 0, 1)$value
  }, numeric(1))
}
double_int <- function(integrand) {
  integrate(function(x) inner_y(x,integrand), 0, 2)$value
}
M <- double_int(rho)
Mx <- double_int(function(x,y) x*rho(x,y))
My <- double_int(function(x,y) y*rho(x,y))
centroid <- c(xbar = Mx/M, ybar = My/M)
print(centroid)
stopifnot(abs(M-4)<1e-7)
stopifnot(max(abs(centroid-c(7/6,1/2)))<1e-7)
