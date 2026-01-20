# R code for creating data tables and graphs

library(tidyverse)

# Load data
data <- read_csv("profession_by_zodiac.csv")

# Make table with zodiac and one profession per row
data_table <- data |>
  select(Zodiac, Profession)

# Count the amount of times each profession appears
profession_counts <- data |>
  filter(Zodiac != "Zodiac", Profession != "Profession") |>
  group_by(Profession) |>
  summarise(Count = n(), .groups = "drop")

# Find the three most common professions
professions_rank <- profession_counts |>
  arrange(desc(Count)) |>
  slice_head(n = 3)

# Distribution of most common zodiac signs among zodiac signs

# Extract profession and make zodiac table for each
profession1 <- professions_rank$Profession[1]

# Count how many times that profession appears per zodiac
zodiac_profession1 <- data_table |>
  filter(Profession == profession1) |>
  group_by(Zodiac) |>
  summarise(Count = n(), .groups = "drop")

#print(zodiac_profession1)
