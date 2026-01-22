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
  # slice_min(count, n=1, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_continent) * 100) |>
  ungroup() |>
  select(Continent, Profession, count, percentage) |>
  mutate(Continent = fct_reorder(Continent, percentage, .desc = TRUE))

# Legend reorder
continent_professions$Professions <- factor(continent_professions$Profession,
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
# Attorneys in the United States = #00FFFF
# Authors = #555555


# Plot barplot
barplot <- continent_professions |>
  ggplot(aes(
    x = Continent,
    y = percentage/100,
    fill = Professions,
  )) +
  geom_col(position="dodge", colour="white") +
  labs(
    x = 'Continent',
    y = 'People with profession (%)',
    # title = 'Percentage of people in their religion\'s 3 most common profession'
  ) +
  ylim(0, 40) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#115fff","#fccd01","#188d7b","#ff8e02","#791e9f" ),
    labels = c("Politician","Lawyer", "Businessperson", "Economist", "Physician", "Barrister")) +
    geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) +
theme(
  axis.text.x = element_text(size = 12),
  axis.text.y = element_text(size = 10),
  axis.title.y = element_text(size = 14),
  axis.title.x = element_text(margin = margin(t = 15), size = 14),
  legend.title = element_text(size = 12)
)

# Save the barplot as .png
ggsave(
  filename = "continents_barplot.png",
  plot = barplot,
  width=10,
)


  # Seperate plot for all subplots for easier comparison
# Make table for most common professions for each continent and the counts and percentage
sub_continent_professions <- data |>
  filter(Continent != 'Continent', Profession != 'Profession') |>
  group_by(Continent, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Continent) |>
  mutate(total_in_continent = sum(count)) |>
  filter(Profession=="Politician"|Profession=="Lawyer"|Profession=="Businessperson"|Profession=="Economist"|Profession=="Physician"|Profession=="Barrister") |>
  mutate(percentage = (count / total_in_continent) * 100) |>
  ungroup() |>
  select(Continent, Profession, count, percentage) |>
  mutate(Continent = fct_reorder(Continent, percentage, .desc = TRUE))

# Legend reorder
sub_continent_professions$Professions <- factor(sub_continent_professions$Profession,
  levels = c("Politician", "Lawyer", "Businessperson", "Teacher", "Economist", "Physician", "Barrister", "Art", "Farmer", "Attorneys in the United States", "Authors"))

sub_barplot <- sub_continent_professions |>
  ggplot(aes(
    x = Professions,
    y = percentage/100,
    fill = Professions,
  )) +
  theme(
  axis.text.x = element_blank(),
  axis.text.y = element_text(size = 10),
  axis.title.y = element_text(size = 12),
  axis.title.x = element_text(margin = margin(t = 15), size = 12),
  legend.title = element_text(size = 12)
) +
  geom_col(position="dodge", colour="white") +
  labs(
    x = 'Professions',
    y = 'People with profession (%)',
    # title = 'Percentage of people in their religion\'s 3 most common profession'
  ) + facet_wrap(~Continent) +
  ylim(0, 40) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#115fff","#fccd01","#188d7b","#ff8e02","#791e9f" ),
    labels = c("Politician","Lawyer", "Businessperson", "Economist", "Physician", "Barrister")) +
  geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  )  

ggsave(
  filename = "sub_continents_barplot.png",
  plot = sub_barplot,
  width=10,
)