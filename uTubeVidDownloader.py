from yt_dlp import YoutubeDL

def download_video(url):
    try:
        yt = {}
        
        with YoutubeDL(yt) as ydl:
    
            #keeping url in square brackets [] allows me to input many URLS
            #It creates a list with a single URL
            ydl.download([url])
        print("Download complete")
    except Exception as e:
        print(f"Error: {e}")
    
#Main execution
Video_url = input("Enter YouTube video URL: ")
download_video(Video_url)


#the --with-- block is used to create a context manager (in this case for YoutubeDL)
    #a context manager automatically handles the setup and teardown of resources.
        #It is a Python is a special object that sets something up before a block of code 
        #runs and then cleans it up afterward, even if there’s an error.
    #this ensures that resources are properly managed