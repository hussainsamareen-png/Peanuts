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
  filename = "A_continents_barplot.png",
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
  filename = "A_sub_continents_barplot.png",
  plot = sub_barplot,
  width=10,
)

# R script for religions

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
  filename = "B_religions_barplot.png",
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

print(sub_religion_professions, n =100)

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
  filename = "B_sub_religions_barplot.png",
  plot = sub_barplot,
  width=10,
)

# R code for zodiac signs


# Order them, such that they are in chronological order
zodiac_order <- c(
  "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", 
  "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius")

# Make table for most common professions for each zodiac sign and the counts and percentage
zodiac_professions <- data |>
  filter(Zodiac != 'Zodiac', Profession != 'Profession') |>
  group_by(Zodiac, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Zodiac) |>
  mutate(total_in_zodiac = sum(count)) |>
  slice_max(count, n = 3, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_zodiac) * 100) |>
  select(Zodiac, Profession, count, percentage) |>
  arrange(match(Zodiac, zodiac_order))

# Legend reorder
zodiac_professions$Professions <- factor(zodiac_professions$Profession,
  levels = c("Politician", "Lawyer", "Businessperson", "Teacher", "Economist", "Physician", "Barrister", "Art", "Farmer", "Attorneys in the United States", "Authors"))

print(zodiac_professions, n=100)

# Plot barplot
barplot <- zodiac_professions |>
  ggplot(aes(
    x = factor(Zodiac, levels = zodiac_order),
    y = percentage/100,
    fill = Professions
  )) +
  geom_density(alpha = 0.5) +
  geom_col(position="dodge",colour="white") +
  labs(
    x = 'Zodiac Signs (Chronological Order)',
    y = 'People with profession (%)',
    # title = 'Percentage of people each zodiac\'s 3 most common professions'
  ) +
  ylim(0, 25) +
  scale_y_continuous(labels=scales::label_percent()) +
  scale_fill_manual(values = c("#fe0002","#115fff","#fccd01","#87e23d"),
    labels = c("Politician","Lawyer", "Businessperson", "Teacher")) +
  geom_hline(
    yintercept = seq(5/100, 25/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) +
theme(
  axis.text.x = element_text(angle = 45, hjust = 1, vjust = 0.8, size = 12),
  axis.text.y = element_text(size = 10),
  axis.title.y = element_text(size = 14),
  axis.title.x = element_text(margin = margin(t = 15), size = 14),
  legend.title = element_text(size = 12)
)

# Save the barplot as .png
ggsave(
  filename = "C_zodiac_barplot.png",
  plot = barplot,
  width=12
)


 # Seperate barplot for subplots <- For activity
# Make table for most common professions for each zodiac sign and the counts and percentage
sub_zodiac_professions <- data |>
  filter(Zodiac != 'Zodiac', Profession != 'Profession') |>
  group_by(Zodiac, Profession) |>
  summarise(count = n(), .groups = "drop") |>
  group_by(Zodiac) |>
  mutate(total_in_zodiac = sum(count)) |>
  filter(Profession=="Politician"|Profession=="Lawyer"|Profession=="Businessperson"|Profession=="Teacher") |>
  mutate(percentage = (count / total_in_zodiac) * 100) |>
  select(Zodiac, Profession, count, percentage) |>
  arrange(match(Zodiac, zodiac_order))

# Legend reorder
sub_zodiac_professions$Professions <- factor(sub_zodiac_professions$Profession,
  levels = c("Politician", "Lawyer", "Businessperson", "Teacher", "Economist", "Physician", "Barrister", "Farmer", "Attorneys in the United States", "Authors", "Art"))

# Plot barplot
sub_barplot <- sub_zodiac_professions |>
  ggplot(aes(
    x = Professions,
    y = percentage/100,
    fill = Professions
  )) +
  theme(
  axis.text.x = element_blank(),
  axis.text.y = element_text(size = 10),
  axis.title.y = element_text(size = 14),
  axis.title.x = element_text(margin = margin(t = 15), size = 14),
  legend.title = element_text(size = 12)
) +
  geom_density(alpha = 0.5) +
  geom_col(position="dodge",colour="white") +
  labs(
    x = 'Zodiac Signs (Chronological Order)',
    y = 'People with profession (%)',
    # title = 'Percentage of people each zodiac\'s 3 most common professions'
  ) + facet_wrap(~Zodiac) +
  ylim(0, 25) +
  scale_y_continuous(labels=scales::label_percent()) +    scale_fill_manual(values = c("#fe0002","#115fff","#fccd01","#87e23d"),
    labels = c("Politician","Lawyer", "Businessperson", "Teacher")) +
  geom_hline(
    yintercept = seq(5/100, 25/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) 

# Save the barplot as .png
ggsave(
  filename = "C_sub_zodiac_barplot.png",
  plot = sub_barplot,
  width=15, height=10,
)

