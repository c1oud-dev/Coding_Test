from collections import defaultdict

def solution(genres, plays):
    play_count = defaultdict(int)
    genre_songs = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_count[genre] += play
        genre_songs[genre].append((play, i))
        
    sorted_genres = sorted(play_count, key=lambda x: play_count[x], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        for play, i in sorted_songs[:2]:
            answer.append(i)

    return answer