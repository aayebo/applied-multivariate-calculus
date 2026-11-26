# F(r,theta) = (r*cos(theta), r*sin(theta))
polar_J <- function(r, theta) {
  matrix(c(cos(theta), -r*sin(theta),
           sin(theta),  r*cos(theta)),
         nrow = 2, byrow = TRUE)
}
det(polar_J(2, pi/4))     # equals r = 2
