import pyaudio
import wave
import tkinter as tk
import threading

audio = None
stream = None
frames = []
recording_thread = None

def toggle_label():
    global recording_thread
    if recording_thread and recording_thread.is_alive():
        stop_recording()
        generate_button.config(text="Start Recording")
    else:
        generate_button.config(text="Stop Recording")
        start_recording()

def start_recording():
    global audio, stream, frames, recording_thread
    chunk = 1024
    channels = 2
    sample_format = pyaudio.paInt16
    frames_per_second = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=sample_format,
                        channels=channels,
                        rate=frames_per_second,
                        frames_per_buffer=chunk,
                        input=True)

    print("Recording audio...")

    frames = []
    is_recording = True

    def record_audio_thread():
        while is_recording:
            data = stream.read(chunk)
            frames.append(data)

    recording_thread = threading.Thread(target=record_audio_thread)
    recording_thread.start()

def stop_recording():
    global audio, stream, frames
    print("Finished recording.")
    is_recording = False

    stream.stop_stream()
    stream.close()
    audio.terminate()

    filename = length_entry.get() + ".wav"
    wf = wave.open(filename, "wb")
    wf.setnchannels(2)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b"".join(frames))
    wf.close()

    length_entry.delete(0, tk.END)

    # Don't add the recorded filename to the history if it's empty
    if filename.strip():
        recordings_history.append(filename)

    # Update the history label to show the recorded filenames
    history_label.config(text="Recording History@:\n" + "\n".join(recordings_history))

root = tk.Tk()
root.title("github.com/devmer2311")
root.geometry("700x370")

# Labels
length_label = tk.Label(root, text="Audio Recorder", font=("Times New Roman", 20, "bold"))
length_label.pack(pady=5)

# Entry
length_entry = tk.Entry(root, font=("Times New Roman", 20, "bold"))
length_entry.pack(pady=7)

# Button
generate_button = tk.Button(root, text="Start Recording", height=2, width=20, font=("Times New Roman", 20, "bold"), command=toggle_label)
generate_button.pack(pady=10)

# Label to display recording history
history_label = tk.Label(root, text="Recording History@:", font=("Times New Roman", 16))
history_label.pack(pady=10)

recordings_history = []  # List to store recording history

root.mainloop()
