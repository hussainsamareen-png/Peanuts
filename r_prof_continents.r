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
  # slice_max(count, n = 3, with_ties = FALSE) |>
  # slice_min(count, n=1, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_continent) * 100) |>
  ungroup() |>
  select(Continent, Profession, count, percentage) |>
  mutate(Continent = fct_reorder(Continent, percentage, .desc = TRUE))

# Legend reorder
continent_professions$group2 <- factor(continent_professions$Profession,
  levels = c("Politician", "Lawyer", "Businessperson", "Teacher", "Economist", "Physician", "Barrister", "Art", "Farmer", "Attorneys in the United States", "Authors"))

# Poltiician = #fe0002
# Lawyer = #115fff
# Businessperson = #fccd01
# Teacher = #87e23d
# Economist = #188d7b
# Physician = #ff8e02
# Barrister = #791e9f
# Art = #f69cc2
# Farmer = #999999
# Attorneys in the United States = #555555
# Authors = #111111


# Plot barplot
barplot <- continent_professions |>
  ggplot(aes(
    x = group2,
    y = percentage/100,
    fill = group2,
  )) +
  geom_col(position="dodge", colour="white") +
  labs(
    x = 'Continent',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their continents\'s most common profession'
  ) +
  ylim(0, 40) +
  scale_y_continuous(labels=scales::label_percent()) +
  # scale_fill_manual(values = c("#fe0002","#115fff","#fccd01","#188d7b","#ff8e02","#791e9f" ),
  #   labels = c("Politician","Lawyer", "Businessperson", "Economist", "Physician", "Barrister")) +
  geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) + facet_wrap(~Continent)

# Save the barplot as .png
ggsave(
  filename = "continents_barplot.png",
  plot = barplot,
  width=10,
)

