from collections import deque

suggested_links = [int(x) for x in input().split()]
suggested_links_deque = deque(suggested_links)
featured_articles = [int(x) for x in input().split()]
final_feed = []
target_engagement_value = int(input())

while suggested_links_deque and featured_articles:
    s = suggested_links_deque.popleft()
    f = featured_articles.pop()
    if s == f:
        final_feed.append(0)
    elif s > f:
        remaining = s % f
        final_feed.append(-remaining)
        if remaining != 0:
            suggested_links_deque.append(2 * remaining)
    else:
        remaining = f % s
        final_feed.append(remaining)
        if remaining != 0:
            featured_articles.append(2 * remaining)

total = sum(final_feed)
print(f"Final Feed: " + ", ".join(map(str, final_feed)))
if total >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total}")
