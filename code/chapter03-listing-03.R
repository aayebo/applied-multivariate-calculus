h <- function(x,y) x*y/(x*x+y*y)
t <- 10^(-seq(1,6))
print(data.frame(t=t,axis=h(t,0),diagonal=h(t,t)))
