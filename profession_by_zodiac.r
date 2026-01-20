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

count <- 0

# Loop for three most common professions 
for (i in 1:3){

  # Extract profession and make zodiac table for each
  profession_i <- professions_rank$Profession[i]

  # Count how many times that profession appears per zodiac and make a table for each
  table_i <- data_table |>
    filter(Profession == profession_i) |>
    group_by(Zodiac) |>
    summarise(Count = n(), .groups = "drop")

  # Save to specific table for each profession
  assign(paste0("zodiac_profession", i), table_i)
  assign(paste0("profession", i), profession_i)
}

#print(profession1)
#print(zodiac_profession1)

#print(profession2)
#print(zodiac_profession2)

#print(profession3)
#print(zodiac_profession3)
