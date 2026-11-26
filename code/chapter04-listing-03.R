nonconvex <- function(p) (p[1]^2-1)^2+p[2]^2
starts <- list(c(-2,1),c(2,1),c(-.7,-1),c(.7,-1))
print(do.call(rbind,lapply(starts,function(s)
  c(optim(s,nonconvex,method="BFGS")$par))))
angle <- optimize(function(t) -(cos(t)+2*sin(t)),
                  c(0,2*pi))
print(c(disk_max=-angle$objective,exact=sqrt(5)))
fixed_sum <- optimize(function(x) -x*(10-x),c(0,10))
print(c(x=fixed_sum$minimum,y=10-fixed_sum$minimum,
        product=-fixed_sum$objective))
