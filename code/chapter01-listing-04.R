A <- c(0, 0, 0)
B <- c(1, 0, 2)
C <- c(0, 3, 1)
AB <- B - A; AC <- C - A
cross3 <- function(u, v) c(u[2]*v[3]-u[3]*v[2],
                            u[3]*v[1]-u[1]*v[3],
                            u[1]*v[2]-u[2]*v[1])
area <- sqrt(sum(cross3(AB, AC)^2))/2
stopifnot(isTRUE(all.equal(area, sqrt(46)/2)))
print(area)
