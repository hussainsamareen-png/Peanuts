# R script for continents

library(tidyverse)

# Load data
data <- read_csv("profession_by_all.csv")

# Make table for most common professions for each continent and the counts and percentage
continent_professions <- data |>
  filter(Continent != 'Continent', Profession != 'Profession') |>
  group_by(Continent, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Continent) |>
  mutate(total_in_continent = sum(count)) |>
  slice_max(count, n = 3, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_continent) * 100) |>
  ungroup() |>
  select(Continent, Profession, count, percentage) |>
  mutate(Continent = fct_reorder(Continent, percentage, .desc = TRUE))

# Plot barplot
barplot <- continent_professions |>
  ggplot(aes(
    x = Continent,
    y = percentage/100,
    fill = Profession
  )) +
  geom_col(position="dodge") +
  labs(
    x = 'Continent',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their continents\'s most common profession'
  ) +
  ylim(0, 40) +
  scale_y_continuous(labels=scales::label_percent()) +
  geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  )

# Save the barplot as .png
ggsave(
  filename = "continents_barplot.png",
  plot = barplot,
  width=10,
)

