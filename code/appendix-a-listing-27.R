sphere_metric <- function(theta) {
  matrix(c(1, 0, 0, sin(theta)^2),
         nrow = 2, byrow = TRUE)
}
sphere_metric(pi/3)
det(sphere_metric(pi/3))   # sin(theta)^2
