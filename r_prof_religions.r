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
  slice_max(count, n = 3, with_ties = FALSE) |>
  # slice_min(count, n=2, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_religion) * 100) |>
  ungroup() |>
  select(Religion, Profession, count, percentage) |>
  mutate(Religion = fct_reorder(Religion, percentage, .desc = TRUE))

# Legend reorder
religion_professions$Professions <- factor(religion_professions$Profession,
  levels = c("Politician", "Businessperson", "Teacher", "Economist", "Lawyer", "Physician", "Barrister", "Art", "Farmer", "Attorneys in the United States", "Author"))

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
barplot <- religion_professions |>
  ggplot(aes(
    x = Religion,
    y = percentage/100,
    fill = Professions
  )) +
  geom_col(position="dodge", colour="white") +
  labs(
    x = 'Religion',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their religion\'s most common profession'
  ) +
  ylim(0, 30) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#fccd01","#87e23d", "#188d7b", "#115fff", "#f69cc2", "#999999", "#555555", "#111111"),
                    labels = c("Politician","Businessperson", "Teacher", "Economist", "Lawyer", "Art", "Farmer", "Attorneys in the United States", "Author")) +
  geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  )

# Save the barplot as .png
ggsave(
  filename = "religions_barplot.png",
  plot = barplot,
  width=10,
)
