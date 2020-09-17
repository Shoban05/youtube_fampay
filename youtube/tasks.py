from .models import VideoData
from django_rq import job

from youtube_datafetch.settings import (
    YOUTUBE_API_URL,
    YOUTUBE_API_KEY,
    YOUTUBE_SEARCH_LIST,
)

import requests


@job("default")
def fetch_youtube_data():
    # Creating the GET APIto query youtube
    url = YOUTUBE_API_URL
    params = {
        "part": "snippet",
        "maxResults": 50,
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "publishedAfter": "2015-01-01T00:00:00Z",
        "order": "date",
        "q": "|".join(YOUTUBE_SEARCH_LIST),
    }
    try:
        response = requests.get(url, params=params)
    except Exception as exc:
        print("Exception while accessing the search API")
        print("Exception: " + str(exc))
        return

    # If status is 200
    if response.status_code == 200:
        # Iterating this over a loop to get all data (as max 50 entries are sent in one request)
        while True:

            json_response = response.json()
            page_token = ""
            more_result = False

            # Flag to check if subsequent call is required
            if json_response.get("nextPageToken"):
                page_token = json_response["nextPageToken"]
                more_result = True

            # Iterating the QuerySet received
            for item in json_response.get("items"):
                video_id = item.get("id", {}).get("videoId")
                snippet_data = item.get("snippet")
                if snippet_data:
                    (obj, created) = VideoData.objects.get_or_create(
                        id=video_id,
                        title=snippet_data.get("title"),
                        description=snippet_data.get("description"),
                        publishing_datetime=snippet_data.get("publishedAt"),
                        defaults={
                            "thumbnails_urls": snippet_data.get("thumbnails", {})
                            .get("default", {})
                            .get("url")
                        },
                    )
                    if created:
                        print("Successfully Created: ", obj.title)

            # Check if next API Call is required
            if more_result:
                params["pageToken"] = page_token

                try:
                    response = requests.get(url, params=params)
                    continue
                except Exception as exc:
                    print("Exception while accessing the search API")
                    print("Exception: " + str(exc))
                    break

            break

    # If status is other than 200
    else:
        print("Issue in Youtube Search Calls, Response: ", response.status_code)
        print("URL: ", url, " Params: ", params)
        return

    print("Successful Completion")
    return


# fetch_youtube_data.delay()
