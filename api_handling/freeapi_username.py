import requests

def fetch_youtube_video_details():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos"
    response = requests.get(url)
    data = response.json()
    
    if data["statusCode"] == 200 and "data" in data:
        video_data = data["data"]["data"][0]
        video_item = video_data["items"]
        
        title = video_item["snippet"]["title"]
        channel_id = video_item["snippet"]["channelId"]
        return title, channel_id
    else:
        raise Exception("Failed to fetch YouTube video data !!")

def fetch_random_username():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name, country
    else:
        raise Exception("Failed to fetch user data !!")

def main():
    try:
        username, country = fetch_random_username()
        print(f"Username: {username} \nCountry: {country}")
        title,ch_id=fetch_youtube_video_details()
        print(f"Title: {title} \n Channel Id: {channel_id}")

        
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()