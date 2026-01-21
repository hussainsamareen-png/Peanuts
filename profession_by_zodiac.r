# R code for zodiac signs

library(tidyverse)

# Load data
data <- read_csv("profession_by_zodiac.csv")

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
  slice_max(count, n = 1, with_ties = FALSE) |>
  mutate(percentage = (count / total_in_zodiac) * 100) |>
  select(Zodiac, Profession, count, percentage) |>
  arrange(match(Zodiac, zodiac_order))

# Plot barplot
barplot <- ggplot(zodiac_professions, aes(
    x = factor(Zodiac, levels = zodiac_order),
    y = percentage,
    fill = Profession
  )) +
  geom_col() +
  labs(
    x = 'Zodiac sign in chronological order',
    y = 'Percentage of people with most common profession',
    title = 'Percentage of people in their zodiac\'s most common profession'
  ) +
  ylim(0, 30) +
  geom_hline(
    yintercept = seq(5, 30, by = 5),
    color = "grey", 
    linetype = "dashed"
  )

# Save the barplot as .png
ggsave(
  filename = "zodiac_barplot.png",
  plot = barplot
)
