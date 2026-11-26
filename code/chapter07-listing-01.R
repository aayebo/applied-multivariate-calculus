r <- 2; theta <- pi/6
J <- matrix(c(cos(theta),sin(theta),
              -r*sin(theta),r*cos(theta)),2,2)
g <- crossprod(J)
print(g)                  # diag(1,4)
stopifnot(max(abs(g-diag(c(1,4))))<1e-12)
