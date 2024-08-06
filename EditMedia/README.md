## 編輯影片
### 套件
* `pip install moviepy`
* `pip install opencv-python opencv-python-headless`

### 注意事項
若是在 windows 環境下須加入路徑方能使用  
```python
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
```

### 內容
* 影片插入圖片
```python
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
picture_path = "...\\XXXX.png"
input_video_path = "...\\XXXX.mp4"
output_video_path = "...\\YYYY.mp4"
fade_duration = 2
video = VideoFileClip(input_video_path, audio_fps=44100)
# 讀取要插入左邊中間的圖片，並調整大小以適應影片的高度的一部分
picture_image = ImageClip(picture_path).set_duration(video.duration)
picture_image = picture_image.resize(height=video.h / 1.5, width=video.w / 1.5)
# 將圖片放置在影片的左邊中間
picture_image = picture_image.set_position((100, (video.h - picture_image.h) // 2 - 50))
# 淡入淡出效果
picture_image = picture_image.crossfadein(fade_duration).crossfadeout(fade_duration)
# 創建一个新的影片剪輯，包含原始影片和圖片
new_video = CompositeVideoClip([video, picture_image])
new_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac', threads=4)
```
* 組合影片
```python
from moviepy.editor import VideoFileClip, concatenate_videoclips
# 獲取第一個剪輯的分辨率和幀率
video_lst = [VideoFileClip(v, audio_fps=44100) for v in video_path_lst]
target_size = video_lst[0].size
fps = video_lst[0].fps
# 調整所有剪輯的分辨率和幀率
top_page = top_page.set_fps(fps).resize(target_size)
clips = [top_page] + video_lst
combined_video = concatenate_videoclips(clips)
combined_video.write_videofile(new_video_path, codec='libx264', audio_codec='aac',
                               threads=os.cpu_count() * 2, preset="fast")

# 释放内存
for clip in clips:
    clip.close()
```

## 編輯圖片
### 套件
* `pip install pillow`

### 內容
* 圖片插入文字
