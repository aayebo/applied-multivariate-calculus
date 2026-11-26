inner <- function(x) {
  vapply(x, function(xx) {
    integrate(function(y) xx + y, 0, xx)$value
  }, numeric(1))
}
integrate(inner, 0, 1)$value
