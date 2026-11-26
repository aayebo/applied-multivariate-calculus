R <- 6371  # illustrative radius, kilometers
p <- c(1,0,0); q <- c(0,1,0)
angle <- acos(max(-1,min(1,sum(p*q))))
distance <- R*angle
print(distance)
stopifnot(abs(distance-R*pi/2)<1e-8)
