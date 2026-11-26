a <- 3; b <- 2
ellipse <- integrate(function(t) rep(a*b,length(t)),0,2*pi)$value
annulus <- pi*(2^2-1^2)
box <- function(a,b,c) a^2*b*c+a*b^2*c+a*b*c^2
print(c(ellipse=ellipse,expected=2*pi*a*b,
        annulus=annulus,box=box(2,3,4)))
stopifnot(abs(ellipse-2*pi*a*b)<1e-9)
stopifnot(abs(annulus-3*pi)<1e-9)
stopifnot(abs(box(2,3,4)-216)<1e-9)
