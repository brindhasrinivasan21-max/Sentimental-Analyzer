from textblob import TextBlob
from tabulate import tabulate
import csv

print("🧠 SENTIMENT ANALYZER FOR LOCAL NEWS 📰")
print("=" * 60)

# --- Step 1: Predefined Local News Samples ---
news_samples = [
    "The government launched a new scheme to help small farmers overcome drought conditions.",
    "Heavy rainfall caused severe flooding in several districts, displacing hundreds of families.",
    "Local schools have improved their performance in the recent board exams.",
    "A tragic accident on the highway claimed the lives of three people yesterday.",
    "Residents celebrated the town’s annual festival with great enthusiasm and joy.",
    "Power cuts across the region caused frustration among citizens.",
    "A new hospital was inaugurated today, promising better healthcare for all."
]

# --- Step 2: User can add custom news ---
while True:
    user_input = input("\nDo you want to add your own news? (yes/no): ").strip().lower()
    if user_input == "yes":
        custom_news = input("Enter your news story: ")
        news_samples.append(custom_news)
    elif user_input == "no":
        break
    else:
        print("Please enter only 'yes' or 'no'.")

# --- Step 3: Analyze each news story ---
results = []
pos_count = neg_count = neu_count = 0

for i, news in enumerate(news_samples, 1):
    blob = TextBlob(news)
    sentiment_score = blob.sentiment.polarity  # Range: -1 to +1

    if sentiment_score > 0.1:
        sentiment = "Positive 😊"
        pos_count += 1
    elif sentiment_score < -0.1:
        sentiment = "Negative 😔"
        neg_count += 1
    else:
        sentiment = "Neutral 😐"
        neu_count += 1

    results.append([i, news, round(sentiment_score, 2), sentiment])

# --- Step 4: Display results in table format ---
print("\n🧾 SENTIMENT ANALYSIS RESULTS:")
print(tabulate(results, headers=["No", "News Headline", "Score", "Sentiment"], tablefmt="grid"))

# --- Step 5: Summary Report ---
print("\n📊 SUMMARY REPORT:")
print(f"Total News Articles Analyzed: {len(news_samples)}")
print(f"Positive: {pos_count} | Negative: {neg_count} | Neutral: {neu_count}")

# --- Step 6: Save to CSV file ---
csv_filename = "sentiment_report.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "News Headline", "Score", "Sentiment"])
    writer.writerows(results)

print(f"\n✅ Results saved successfully to '{csv_filename}'")

print("\n🌟 Thank you for using the Sentiment Analyzer for Local News!")
