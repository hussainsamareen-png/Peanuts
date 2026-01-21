# R code for creating data tables and graphs

library(tidyverse)

# Note: make this into a loop for all of the files needed, so it can do all at once
# for .csv file in folder

# Load data
data <- read_csv("profession_by_zodiac.csv")

# Make table with zodiac and one profession per row
data_table_zodiac <- data |>
  select(Zodiac, Profession)

# Make a list of the tables (each entry in the list is a table) that count:
counts <- list(
  by_profession = data_table_zodiac |> count(Profession, name = "Count"), # amount of people in each profession
  by_zodiac = data_table_zodiac |> count(Zodiac, name = "Count") # amount of people with each zodiac sign
)

# Find the three most common professions
professions_rank <- counts$by_profession |>
  arrange(desc(Count)) |>
  slice_head(n = 3)

# Add a list in which the tables for the visualisation will be saved
tables <- list()

# Loop for three most common professions 
for (i in 1:3){

  # Extract profession and make zodiac table for each
  profession_i <- professions_rank$Profession[i]

  # Count how many times that profession appears 
  table_i <- data_table_zodiac |>
    filter(Profession == profession_i) |>
    group_by(Zodiac) |>
    summarise(Count = n(), .groups = "drop") |>
    mutate(Percentage = Count / counts$by_zodiac$Count[match(Zodiac, counts$by_zodiac$Zodiac)] * 100) |>
    arrange(desc(Percentage)) |> 
    mutate(Zodiac = factor(Zodiac, levels = Zodiac))

  # Create barplot
  barplot_i <- table_i |>
    ggplot(
      aes(
        x = Zodiac, 
        y = Percentage, 
        fill = Zodiac)
      ) +
    geom_col(fill = 'darkgrey') +
      labs(
        x = 'Zodiac sign', 
        y = paste0('Number of ', profession_i, 's'), 
        title = paste0('Percentage of ', profession_i, 's per zodiac sign %')
    ) +
    # Formatting to make the barplots prettier
    ylim(0, 30) +  # same y-axis for all barplots
    geom_hline( # formatting and aesthetics
      yintercept = seq(5, 30, by = 5),
      color = "grey", 
      linetype = "dashed"
    )

  # Save the barplot as .png
  ggsave(
    filename = paste0("zodiac_barplot", i, ".png"),
    plot = barplot_i
  )
}
