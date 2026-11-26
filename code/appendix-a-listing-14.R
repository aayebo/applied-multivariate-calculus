centered_derivative <- function(f, x, h = 1e-5) {
  (f(x + h) - f(x - h)) / (2*h)
}
centered_derivative(sin, pi/3)
cos(pi/3)                 # analytical comparison
