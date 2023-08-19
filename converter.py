import os
import tkinter as tk
from tkinter import filedialog, ttk
from moviepy.editor import VideoFileClip, AudioFileClip

class MediaConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Converter")

        self.source_label = tk.Label(root, text="Source File:")
        self.source_label.pack()
        self.source_entry = tk.Entry(root)
        self.source_entry.pack()
        self.source_button = tk.Button(root, text="Browse", command=self.browse_source)
        self.source_button.pack()

        self.destination_label = tk.Label(root, text="Destination File:")
        self.destination_label.pack()
        self.destination_entry = tk.Entry(root)
        self.destination_entry.pack()
        self.destination_button = tk.Button(root, text="Browse", command=self.browse_destination)
        self.destination_button.pack()

        self.format_label = tk.Label(root, text="Output Format:")
        self.format_label.pack()
        self.output_format = tk.StringVar()
        self.format_menu = ttk.Combobox(root, textvariable=self.output_format, values=["MP4", "MP3", "AVI", "MOV", "WAV", "MKV"])
        self.format_menu.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def browse_source(self):
        file_path = filedialog.askopenfilename()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, file_path)

    def browse_destination(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, file_path)

    def convert(self):
        source_file = self.source_entry.get()
        destination_file = self.destination_entry.get()
        output_format = self.output_format.get().lower()

        if not source_file or not destination_file or not output_format:
            return

        if not os.path.exists(source_file):
            print("Source file does not exist.")
            return

        try:
            if output_format in ["mp4", "avi", "mov", "mkv"]:
                video_clip = VideoFileClip(source_file)
                video_clip.write_videofile(destination_file, codec="libx264")
                video_clip.close()
                print("Video conversion successful.")
            elif output_format == "mp3":
                audio_clip = AudioFileClip(source_file)
                audio_clip.write_audiofile(destination_file, codec="mp3")
                audio_clip.close()
                print("Audio conversion successful.")
            elif output_format == "wav":
                audio_clip = AudioFileClip(source_file)
                audio_clip.write_audiofile(destination_file, codec="pcm_s16le")
                audio_clip.close()
                print("Audio conversion successful.")
        except Exception as e:
            print(f"Error during conversion: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaConverterApp(root)
    root.mainloop()
