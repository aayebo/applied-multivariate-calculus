measurements <- data.frame(
  position = seq(0, 2, by = 0.5),
  temperature = c(20.1, 21.0, NA, 23.2, 24.1)
)
write.csv(measurements, "results/temperature.csv",
          row.names = FALSE)
reloaded <- read.csv("results/temperature.csv")
stopifnot(nrow(reloaded) == 5)
valid <- complete.cases(reloaded)
plot(reloaded$position[valid],
     reloaded$temperature[valid], type = "b",
     xlab = "Position (m)", ylab = "Temperature (degrees C)")
