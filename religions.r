# R script for religions

library(tidyverse)

# Load data
data <- read_csv("profession_by_all.csv")

# Make table for most common professions for each religion and the counts and percentage
religion_professions <- data |>
  filter(Religion != 'Religion', Profession != 'Profession') |>
  group_by(Religion, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Religion) |>
  mutate(total_in_religion = sum(count)) |>
  slice_max(count, n = 1, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_religion) * 100) |>
  ungroup() |>
  select(Religion, Profession, count, percentage) |>
  mutate(Religion = fct_reorder(Religion, percentage, .desc = TRUE))

# Plot barplot
barplot <- religion_professions |>
  ggplot(aes(
    x = Religion,
    y = percentage,
    fill = Profession
  )) +
  geom_col() +
  labs(
    x = 'Religion',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their religion\'s most common profession'
  ) +
  ylim(0, 30) +
  geom_hline(
    yintercept = seq(5, 30, by = 5),
    color = "grey", 
    linetype = "dashed"
  )

# Save the barplot as .png
ggsave(
  filename = "religions_barplot.png",
  plot = barplot
)
