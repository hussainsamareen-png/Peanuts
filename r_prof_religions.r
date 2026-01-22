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
# Farmer = #a67b5c
# Attorneys in the United States = #777777
# Authors = #333333

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
    y = 'People with profession (%)',
    # title = 'Percentage of people in their religion\'s 3 most common profession'
  ) +
  ylim(0, 30) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#fccd01","#87e23d", "#188d7b", "#115fff", "#f69cc2", "#a95c26", "#00FFFF", "#555555"),
                    labels = c("Politician","Businessperson", "Teacher", "Economist", "Lawyer", "Art", "Farmer", "Attorneys in the United States", "Author")) +
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
  filename = "religions_barplot.png",
  plot = barplot,
  width=10,
)

  # Seperate plots for all subplots for easier comparison

# Make table for most common professions for each religion and the counts and percentage
sub_religion_professions <- data |>
  filter(Religion != 'Religion', Profession != 'Profession') |>
  group_by(Religion, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Religion) |>
  mutate(total_in_religion = sum(count)) |>
  filter(Profession=="Politician"|Profession=="Businessperson"|Profession=="Teacher"|Profession=="Economist"|Profession=="Lawyer"|Profession=="Art"|Profession=="Farmer"|Profession=="Attorneys in the United States"|Profession=="Author") |>
  mutate(percentage = (count / total_in_religion) * 100) |>
  ungroup() |>
  select(Religion, Profession, count, percentage) |>
  mutate(Religion = fct_reorder(Religion, percentage, .desc = TRUE))

# Legend reorder
sub_religion_professions$Professions <- factor(sub_religion_professions$Profession,
  levels = c("Politician", "Businessperson", "Teacher", "Economist", "Lawyer", "Physician", "Barrister", "Art", "Farmer", "Attorneys in the United States", "Author"))

# Poltiician = #fe0002
# Lawyer = #115fff
# Businessperson = #fccd01
# Teacher = #87e23d
# Economist = #188d7b
# Physician = #ff8e02
# Barrister = #791e9f
# Art = #f69cc2
# Farmer = #a67b5c
# Attorneys in the United States = #00FFFF
# Authors = #555555

# Plot barplot
sub_barplot <- sub_religion_professions |>
  ggplot(aes(
    x = Professions,
    y = percentage/100,
    fill = Professions
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
    x = 'Religion',
    y = 'People with profession (%)',
    # title = 'Percentage of people in their religion\'s 3 most common profession'
  ) + facet_wrap(~Religion) +
  ylim(0, 30) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#fccd01","#87e23d", "#188d7b", "#115fff", "#f69cc2", "#a95c26", "#00FFFF", "#555555"),
                    labels = c("Politician","Businessperson", "Teacher", "Economist", "Lawyer", "Art", "Farmer", "Attorneys in the United States", "Author")) +
  geom_hline(
    yintercept = seq(5/100, 30/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) 

# Save the barplot as .png
ggsave(
  filename = "sub_religions_barplot.png",
  plot = sub_barplot,
  width=10,
)