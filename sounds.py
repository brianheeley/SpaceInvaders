import stdaudio
import threading
import time


class SoundManager:

    _current_sound_thread = None
    _sound_lock = threading.Lock()
    _stop_event = threading.Event()

    @staticmethod
    def play_sound(file):
        def _play_sound_thread(stop_event, sound_id):
            try:
                with SoundManager._sound_lock:
                    # Mark this as current sound
                    SoundManager._current_sound_id = sound_id

                if not stop_event.is_set():
                    stdaudio.playFile(file)

            except Exception as e:
                print(f"Error playing {file}: {e}")

        # Stop any currently playing sounds
        SoundManager.stop_all_sounds()

        # Reset stop event
        SoundManager._stop_event.clear()

        # Create unique sound ID
        sound_id = f"{file}_{time.time()}"

        # Start new sound thread
        sound_thread = threading.Thread(
            target=_play_sound_thread, args=(SoundManager._stop_event, sound_id)
        )
        sound_thread.daemon = True

        with SoundManager._sound_lock:
            SoundManager._current_sound_thread = sound_thread
            SoundManager._current_sound_id = sound_id

        sound_thread.start()
        return sound_thread

    @staticmethod
    def stop_all_sounds():

        # Stop any playing sounds
        SoundManager._stop_event.set()

        # Stop event for future sounds
        SoundManager._stop_event = threading.Event()

        with SoundManager._sound_lock:
            # Clear current sound thread
            SoundManager._current_sound_thread = None
