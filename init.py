import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

linkUrl = ""
statusMsg = ""

# File Location
def on_file():
    file_path = filedialog.askdirectory(title="Select a location")
    if file_path:
        file_field.insert(tk.END, file_path)

# Download Submission
def on_submit():
    global linkUrl
    linkUrl = entry.get()

    if linkUrl:
        try:
            yt = YouTube(linkUrl)

            video_stream = yt.streams.get_highest_resolution()

            filePath = file_field.get()

            if filePath:
                downloadVideo = video_stream.download(filePath)
            else:
                statusMsg = "Invalid File Path."
                status_msg.config(text=statusMsg, fg="white", bg="red")
                return False

            if downloadVideo:
                statusMsg = "Successful"
                status_msg.config(text=statusMsg, fg="white", bg="green")               
                file_field.delete(0, tk.END)
                entry.delete(0, tk.END)
                return True
            else:
                statusMsg = "Failed"
                status_msg.config(text=statusMsg, fg="white", bg="red")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    else:
        return False


# GUI of Youtube Video Downloader
def appInterface():
    global entry
    global file_field
    global status_msg

    root = tk.Tk()
    root.title("Youtube Video Downloader | It's Nathan")

    # Set window style
    root.geometry("400x300")
    root.configure(bg="#000")    

    # Create label
    link_label = tk.Label(root, text="Enter Youtube Video Link", bg="black", fg="white", font="roboto")
    link_label.pack(pady=5)

    # Link input field
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    # File Dialog for File Location
    file_label = tk.Label(root, text="Location", bg="black", fg="white", font="roboto")
    file_label.pack(pady=5)

    file_field = tk.Entry(root, width=30)
    file_field.pack(pady=5)

    file_select = tk.Button(root, text="Browse", command=on_file, bg="lightblue", fg="white")
    file_select.pack(pady=5)

    # Create download button
    download_button = tk.Button(root, text="Download", command=on_submit, bg="red", fg="white")
    download_button.pack(pady=5)

    # Status Messages
    status_msg = tk.Label(root, text="", bg="black")
    status_msg.pack(pady=5)

    # Run the tkinter main loop
    root.mainloop()

# Run the App
appInterface()