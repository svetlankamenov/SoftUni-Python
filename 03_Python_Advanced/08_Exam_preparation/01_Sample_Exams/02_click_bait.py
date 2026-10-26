from collections import deque

final_feed = []

engagement_scores = deque(int(x) for x in input().split())
popularity_scores = [int(x) for x in input().split()]
target_value = int(input())

while engagement_scores and popularity_scores:
    s_link = engagement_scores.popleft()
    f_article = popularity_scores.pop()

    if s_link > f_article:
        reminder = s_link % f_article
        final_feed.append(-abs(reminder))
        if not reminder == 0:
            reminder *= 2
            engagement_scores.append(reminder)
    elif s_link < f_article:
        reminder = f_article % s_link
        final_feed.append(abs(reminder))
        if not reminder == 0:
            reminder *= 2
            popularity_scores.append(reminder)
    else:
        final_feed.append(0)

print("Final Feed: ", end="")
print(", ".join(map(str, final_feed)))

total_engagement_value = sum(final_feed)

if total_engagement_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    short_fall = target_value - total_engagement_value
    print(f"Goal not achieved! Short by: {short_fall}")
