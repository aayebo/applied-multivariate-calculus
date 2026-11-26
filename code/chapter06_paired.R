a <- 2
circulation <- integrate(function(t) rep(a*a,length(t)),0,2*pi)$value
wire_mass <- integrate(function(t) 2*(1+2*sin(t)),0,pi)$value
flux <- integrate(function(r) 2*pi*(4-r*r)*r,0,1)$value
line <- integrate(function(t) rep(a*a/2,length(t)),0,2*pi)$value
cap <- integrate(function(r) 2*pi*r,0,a)$value
stopifnot(abs(circulation-2*pi*a*a)<1e-8,abs(wire_mass-(2*pi+8))<1e-8,abs(flux-7*pi/2)<1e-8,abs(line-4*pi)<1e-8,abs(cap-4*pi)<1e-8)
print(c(circulation=circulation,wire_mass=wire_mass,flux=flux,line=line,cap=cap))
