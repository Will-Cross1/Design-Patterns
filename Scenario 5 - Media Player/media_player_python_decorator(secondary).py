# Decorator design pattern

# Base media player interface
class MediaPlayer:
    def play(self):
        raise NotImplementedError

# Main media player for MP4
class MP4Player(MediaPlayer):
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self):
        print(f"Playing video: {self.file_path}")
        
# Main media player for MP3
class MP3Player(MediaPlayer):
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self):
        print(f"Playing audio: {self.file_path}")


# Concrete decorator
class PlayerDecorator(MediaPlayer):
    def __init__(self, wrapped_player):
        self.wrapped_player = wrapped_player

    def play(self):
        self.wrapped_player.play()


# subtitle decorator feature
class SubtitleDecorator(PlayerDecorator):
    def __init__(self, wrapped_player, subtitle_file):
        super().__init__(wrapped_player)
        self.subtitle_file = subtitle_file

    def play(self):
        super().play()
        print(f"Displaying subtitles from: {self.subtitle_file}")

# Dub decorator feature
class DubDecorator(PlayerDecorator):
    def __init__(self, wrapped_player, dub_language):
        super().__init__(wrapped_player)
        self.dub_language = dub_language

    def play(self):
        super().play()
        print(f"Applying dubbing: {self.dub_language}")


# Example use
if __name__ == "__main__":
    # Basic video player
    video_player = MP4Player("film.mp4")
    video_player.play()
    print("")

    # Video player with subtitle decorator
    video_player_with_subtitles = SubtitleDecorator(
        MP4Player("film.mp4"),
        "film.srt"
    )
    video_player_with_subtitles.play()
    print("")

    # Video player with subtitle and dub decorators
    video_player_all = DubDecorator(SubtitleDecorator(
            MP4Player("film.mp4"),
            "film.srt"
        ),
        "English Dub"
    )
    video_player_all.play()
    print("")
    print("")
    
    
    # Basic music player
    music_player = MP3Player("song.mp3")
    music_player.play()
    print("")

    # Music player with dub decorator
    music_player_with_dub = DubDecorator(
        MP3Player("song.mp3"),
        "English Dub"
    )
    music_player_with_dub.play()
    print("")
