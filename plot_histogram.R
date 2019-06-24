require(ggplot2)
require(skimr)
require(bbplot)

df  <- read.csv("sentences_sentiment.csv")
skim(df)

ggplot(df, aes(score)) +
  geom_histogram(bins = 20) +
  ggtitle("Histogram of sentiment values", 
          subtitle = "Calculated from a sample of tweets containing the hashtag #BringBackNationalDex") +
  bbc_style() +
  xlab("score") +
  ylab("count") +
  theme(axis.title = element_text(size = 18), 
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)))


