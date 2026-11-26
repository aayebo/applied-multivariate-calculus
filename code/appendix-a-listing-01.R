# scripts/first_steps.R
rm(list = ls())               # optional for a fresh teaching session
radius <- 3
height <- 8
volume <- pi * radius^2 * height
cat("Cylinder volume:", round(volume, 3), "cubic units\n")
