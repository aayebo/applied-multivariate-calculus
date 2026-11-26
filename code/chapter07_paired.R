r <- 2; theta <- pi/6
J <- matrix(c(cos(theta),sin(theta),-r*sin(theta),r*cos(theta)),2,2)
g <- crossprod(J)
V <- c(2,3); V_lower <- as.vector(g %*% V)
stopifnot(max(abs(g-diag(c(1,4))))<1e-12)
stopifnot(abs(sum(V*V_lower)-40)<1e-12)
stopifnot(max(abs(as.vector(solve(g,V_lower))-V))<1e-12)
R <- 6371; p <- c(1,0,0); q <- c(0,1,0)
angle <- acos(max(-1,min(1,sum(p*q)))); distance <- R*angle
stopifnot(abs(distance-R*pi/2)<1e-8)
print(list(metric=g,lowered_vector=V_lower,great_circle_km=distance))
