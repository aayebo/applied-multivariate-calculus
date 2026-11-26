wire_mass <- integrate(function(t) 2*(1+2*sin(t)),0,pi)$value
flux <- integrate(function(r) 2*pi*(4-r^2)*r,0,1)$value
print(c(wire_mass=wire_mass,exact_mass=2*pi+8,
        surface_flux=flux,exact_flux=7*pi/2))
