import json

def load_data():
    try:
        with open('youtube.txt','r')as file:
            return json.load(file)#automatically jaye ga file mein jo data hai usy read kry ga aur usy json mein bi convert kry ga
    except FileNotFoundError:
        return[]#return empty list instead of [1,2]

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)#kia likhna hai videos ko # kidr likhna file mein likhna hai  

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name= input("Enter video name :")
    time=   input("Enter video time :")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)  # Save the updated list after adding a video
    print("Video added successfully!")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
        print("Video updated successfully!")
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid video index selected")


#professional practice btanay ky liye main entry point program ka idr hai
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option:")
        print("1.List all youtube videos")
        print("2.Add a youtube video")
        print("3.Update a youtube video")
        print("4.Delete a youtube video")
        print("5.Exit")
        choice=input("Enter your choice:")
        # print(videos) # Removed this line as it's not needed for normal operation

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":    
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice, please try again.")

if __name__== "__main__":#agr function ka name kahain pr b main hai to main ko run krdo
 main()

#load mean data load krlo
#dump mean data save krdo sara ka sara