set.seed(2026); n <- 100000
x <- runif(n); y <- runif(n)
vals <- ifelse(x+y<=1,x+2*y,0)
print(c(estimate=mean(vals),MC_SE=sd(vals)/sqrt(n),exact=.5))
