observations <- data.frame(
  x = c(0, 1, 2, 3),
  temperature = c(20.0, 22.4, NA, 26.1)
)
str(observations)
mean(observations$temperature, na.rm = TRUE)
complete.cases(observations)
write.csv(observations, "results/observations.csv",
          row.names = FALSE)
