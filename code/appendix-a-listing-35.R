cross3 <- function(a, b) {
  c(a[2]*b[3]-a[3]*b[2],
    a[3]*b[1]-a[1]*b[3],
    a[1]*b[2]-a[2]*b[1])
}
a <- 2; b <- 0.5
rprime <- function(t) c(-a*sin(t), a*cos(t), b)
rsecond <- function(t) c(-a*cos(t), -a*sin(t), 0)
curvature <- function(t) {
  v <- rprime(t); acc <- rsecond(t)
  sqrt(sum(cross3(v,acc)^2))/(sum(v^2)^(3/2))
}
times <- seq(0, 2*pi, length.out = 100)
kvals <- vapply(times, curvature, numeric(1))
range(kvals)
stopifnot(max(abs(kvals - a/(a^2+b^2))) < 1e-10)
