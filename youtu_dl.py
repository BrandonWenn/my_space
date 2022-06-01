# importing the module 
from pytube import YouTube 
  
# where to save 
SAVE_PATH = "G:/" #to_do 
  
# link of the video to be downloaded 
link='https://www.youtube.com/watch?v=VIoFp0s9IYQ&list=PLteWyEGqaaeO3Dx48PCUNDyVs8BwGHb1g&index=2'
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 


try: 
    # downloading the video 
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
except: 
    print("Some Error!") 
print('Task Completed!')  