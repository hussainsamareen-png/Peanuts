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


# Plot barplot
barplot <- zodiac_professions |>
  ggplot(aes(
    x = factor(Zodiac, levels = zodiac_order),
    y = percentage/100,
    fill = Profession
  )) +
  geom_col(position="dodge") +
  labs(
    x = 'Zodiac sign in chronological order',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their zodiac\'s most common profession'
  ) +
  ylim(0, 25) +
  scale_y_continuous(labels=scales::label_percent()) +
  geom_hline(
    yintercept = seq(5/100, 25/100, by = 5/100),
    color = "grey", 
    linetype = "dashed"
  ) +
theme(
  axis.text.x = element_text(angle = 45, hjust = 1, vjust = 0.5, size = 10),
  axis.title.x = element_text(margin = margin(t = 15))
)

# Save the barplot as .png
ggsave(
  filename = "zodiac_barplot.png",
  plot = barplot,
  width=10
)
