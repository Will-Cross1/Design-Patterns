# Third-party libraries (pretend these are external and inconsistent)
class ThirdPartyMP3:
    """
    External MP3 audio library.
    Audio playback only. You must load the track first, then play_audio.
    """
    def load_track(self, path):
        print(f"MP3 Loading audio track: {path}")

    def play_audio(self):
        print("MP3 playing audio!")


class ThirdPartyMP4:
    """
    External MP4 video library.
    You must load the video first, then optionally attach subtitles, then start playback.
    This library's subtitle method include a file path and a time delay for syncing
    """
    def load_video(self, path):
        print(f"MP4 Loading video file: {path}")
    
    def attach_subtitles(self, srt_path, time_delay):
        print(f"MP4 Attaching subtitles: {srt_path} with delay: {time_delay}")

    def start_playback(self):
        print("MP4 playing video!")


class ThirdPartyAVI:
    """
    External AVI video library.
    You must open the container first, then optionally load subtitles from an API, then render frames.
    This library's subtitle method takes an API endpoint instead of a file path.
    (showing that it is different per external library)
    """
    def open_container(self, filename):
        print(f"AVI Opening AVI container: {filename}")
    
    def load_subtitle_file_from_api(self, API):
        print(f"AVI Loading subtitles from: {API}")

    def render_frames(self):
        print("AVI playing video!")


# Target interface (what the Player expects in terms of function and variables)
# Not necessarily needed, but included for documentation and to show the design pattern better.

class MediaDecoder:
    def play(self, file_path, subtitles=None, time_delay=0):
        """
        file_path: path to media file
        subtitles: optional subtitle source (e.g. .srt path or API for subtitle website)
        time_delay: optional delay for subtitles in seconds
        """
        raise NotImplementedError


# The adapters for the Adapter design pattern, one for each third party library

class MP3Adapter(MediaDecoder):
    def __init__(self):
        self.mp3 = ThirdPartyMP3()

    def play(self, file_path, subtitles=None, time_delay=0):
        # Translates the play() call to the MP3 library's specific calls.
        # subtitles and time_delay are ignored since MP3 doesn't support them, but they are included to match the MediaDecoder interface
        self.mp3.load_track(file_path)
        self.mp3.play_audio()


class MP4Adapter(MediaDecoder):
    def __init__(self):
        self.mp4 = ThirdPartyMP4()

    def play(self, file_path, subtitles=None, time_delay=0):
        # Translates the play() call to the MP4 library's specific calls.
        # This library uses each parameter, so they are used as needed.
        self.mp4.load_video(file_path)
        
        if subtitles is not None:
            self.mp4.attach_subtitles(subtitles, time_delay)

        self.mp4.start_playback()


class AVIAdapter(MediaDecoder):
    def __init__(self):
        self.avi = ThirdPartyAVI()

    def play(self, file_path, subtitles=None, time_delay=0):
        # subtitles are interpreted as an API endpoint for this library rather than a file.
        # time_delay is ignored as the library does not support it.
        # Translates the play() call to the AVI library's specific calls.
        self.avi.open_container(file_path)
        
        if subtitles is not None:
            self.avi.load_subtitle_file_from_api(subtitles)

        self.avi.render_frames()


class OGGAdapter(MediaDecoder):
    # Demonstration of how not implemented adapters can work.
    def __init__(self):
        # placeholder for future OGG third party library
        pass
    # play method not implemented, will raise a NotImplementedError exception when called


# What the user uses, new file types added as the library expands. 
# Depends on the MediaDecoder interface, not the third party libraries directly. 
# Selects appropriate adapter at runtime

class Player:
    def play(self, file_path, subtitles=None, time_delay=0):
        if file_path.endswith(".mp3"):
            decoder = MP3Adapter()
        elif file_path.endswith(".mp4"):
            decoder = MP4Adapter()
        elif file_path.endswith(".avi"):
            decoder = AVIAdapter()
        elif file_path.endswith(".ogg"):
            decoder = OGGAdapter()
        else:
            raise ValueError("Unsupported format")

        decoder.play(file_path, subtitles, time_delay)


# Example use prints
if __name__ == "__main__":
    player = Player()

    print(" mp3 test (plays, ignores subtitles and delay): ")
    player.play("song.mp3", "song.srt", 2)
    print("")
    
    print(" mp4 test (no subtitles): ")
    player.play("film.mp4")
    print("")
    
    print(" mp4 test (with subtitles, no delay): ")
    player.play("film.mp4", "film.srt")
    print("")

    print(" mp4 test (with subtitles and delay): ")
    player.play("film.mp4", "film.srt", 3)
    print("")

    print(" avi test (no subtitles): ")
    player.play("other_film.avi")
    print("")
    
    # please don't visit this link, I made it up (though it looks like it resolves...)
    print(" avi test (with subtitle API): ")
    player.play("other_film.avi", "http://subtitles.com/other_film")
    print("")

    print(" ogg test (should raise an exception): ")
    try:
        player.play("audio.ogg")
    except NotImplementedError:
        print(f"Caught expected error (NotImplementedError).")
    print("")
    
    print(" egg Non existent extension (should raise an exception): ")
    try:
        player.play("thing.egg")
    except ValueError:
        print(f"Caught expected error (ValueError).")
