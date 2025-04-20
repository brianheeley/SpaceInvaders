import stdaudio
import threading
import time


class SoundManager:

    _active_sounds = {}
    _lock = threading.Lock()

    @staticmethod
    def play_sound(file):

        def _play_sound_thread():
            try:
                sound_id = f"{file}_{time.time()}"

                with SoundManager._lock:
                    SoundManager._active_sounds[sound_id] = True

                stdaudio.playFile(file)

                with SoundManager._lock:
                    if sound_id in SoundManager._active_sounds:
                        del SoundManager._active_sounds[sound_id]

            except Exception as e:
                print(f"Error playing {file}: {e}")

        sound_thread = threading.Thread(target=_play_sound_thread)
        sound_thread.daemon = True
        sound_thread.start()

        return sound_thread
