from moviepy import VideoFileClip

# Correctly specified file paths
input_video = r"C:\Users\jamai\OneDrive\Documents\Apowersoft\ApowerREC\20250113_115641.mp4"
output_gif = r"C:\Users\jamai\OneDrive\Documents\Apowersoft\ApowerREC\output_gif3.gif"

# Load the video file
clip = VideoFileClip(input_video)

# Resize the video to 720p (1280x720)
clip_resized = clip.resized(new_size=(1280, 720))

# Convert to GIF with specified FPS
clip_resized.write_gif(output_gif, fps=10)

print(f"GIF saved as {output_gif}")
