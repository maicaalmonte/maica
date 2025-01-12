from moviepy import VideoFileClip

# Correctly specified file paths
input_video = r"C:\Users\jamai\OneDrive\Documents\Apowersoft\ApowerREC\20250112_103438.mp4"
output_gif = r"C:\Users\jamai\OneDrive\Documents\Apowersoft\ApowerREC\output_gif.gif"

# Load the video file
clip = VideoFileClip(input_video)

# Convert to GIF
clip.write_gif(output_gif, fps=10)

print(f"GIF saved as {output_gif}")
