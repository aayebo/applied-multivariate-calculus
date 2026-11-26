a <- 2
line <- integrate(function(t) rep(a^2/2,length(t)),0,2*pi)$value
flat <- pi*a^2
cap <- integrate(function(r) 2*pi*r,0,a)$value
print(c(line=line,flat=flat,cap=cap))
stopifnot(max(abs(c(line,flat,cap)-4*pi))<1e-8)
