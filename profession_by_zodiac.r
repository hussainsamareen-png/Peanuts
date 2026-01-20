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

# Make a list of all the the tables
tables <- list(
  zodiac_profession1,
  zodiac_profession2,
  zodiac_profession3
)

# Loop for plotting the three barplots
for (i in 1:3) {

  # Track which profession each barplot is for
  profession_i <- professions_rank$Profession[i]
  table_i <- tables[[i]]

  # Create barplot
  barplot_i <- table_i |>
    ggplot(
      aes(
        x = Zodiac, 
        y = Count, 
        fill = Zodiac)
      ) +
    geom_col(fill = 'darkgrey') +
      labs(
        x = 'Zodiac sign', 
        y = paste0('Number of ', profession_i, 's'), 
        title = paste0('Distribution of ', profession_i, 's by zodiac sign')
    ) +
    # Formatting to make the barplots prettier
    ylim(0, 500) +  # same y-axis for all barplots
    geom_hline(yintercept = seq(100, 500, by = 100), color = "grey", linetype = "dashed", linewidth = 0.5)
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))

   # Save the barplot as .png
  ggsave(
    filename = paste0("zodiac_barplot", i, ".png"),
    plot = barplot_i
  )
}
