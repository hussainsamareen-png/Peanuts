# R code for zodiac signs
library(tidyverse)

# Load data
data <- read_csv("profession_by_all.csv")

# Order them, such that they are in chronological order
zodiac_order <- c(
  "capricorn", "aquarius", "pisces", "aries", "taurus", "gemini", 
  "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius")

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
  filename = "zodiac_barplot.png",
  plot = barplot,
  width=12
)
