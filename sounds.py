import stdaudio
import threading
import time
import subprocess
import sys
import os


class SoundManager:
    _current_sound_process = None
    _sound_lock = threading.Lock()

    @staticmethod
    def play_sound(file):
        with SoundManager._sound_lock:
            # Stop current sound
            SoundManager._terminate_current_sound()

            try:
                # Create Python process to play sound
                sound_script = f"import stdaudio; " f"stdaudio.playFile('{file}')"

                # Start process
                process = subprocess.Popen(
                    [sys.executable, "-c", sound_script],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

                # Store process
                SoundManager._current_sound_process = process

            except Exception as e:
                print(f"Error starting sound process for {file}: {e}")

    @staticmethod
    def _terminate_current_sound():
        if SoundManager._current_sound_process is not None:
            try:
                # Kill process
                SoundManager._current_sound_process.terminate()

                # Wait for shutdown
                try:
                    SoundManager._current_sound_process.wait(timeout=0.2)
                except subprocess.TimeoutExpired:
                    # Force kill if not responding
                    SoundManager._current_sound_process.kill()

                # Remove currently playing sound
                SoundManager._current_sound_process = None
            except Exception as e:
                print(f"Error terminating sound process: {e}")

    @staticmethod
    def stop_all_sounds():
        # Stop currently playing sounds
        with SoundManager._sound_lock:
            SoundManager._terminate_current_sound()
