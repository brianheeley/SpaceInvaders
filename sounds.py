import stdaudio
import threading
import time


class SoundManager:

    _current_sound = None
    _sound_lock = threading.Lock()

    @staticmethod
    def play_sound(file):

        def _play_sound_thread(sound_id):
            try:
                with SoundManager._sound_lock:
                    # Mark this as current sound
                    SoundManager._current_sound = sound_id

                stdaudio.playFile(file)

                with SoundManager._sound_lock:
                    # Only clear if this is still the current sound
                    if SoundManager._current_sound == sound_id:
                        SoundManager._current_sound == None

            except Exception as e:
                print(f"Error playing {file}: {e}")

        # Generate a unique ID for this sound
        sound_id = f"{file}_{time.time()}"

        # Stop any currently playing sounds
        SoundManager.stop_all_sounds()

        # Start new sound thread
        sound_thread = threading.Thread(target=_play_sound_thread, args=(sound_id,))
        sound_thread.daemon = True
        sound_thread.start()

        return sound_thread

    @staticmethod
    def stop_all_sounds():
        with SoundManager._sound_lock:
            # Set current sound to None as no sound should be playing
            SoundManager._current_sound = None
