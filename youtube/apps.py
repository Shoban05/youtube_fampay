from django.apps import AppConfig

from datetime import datetime
import django_rq
import os


class YoutubeConfig(AppConfig):
    name = "youtube"

    def ready(self):
        if os.environ.get("RUN_MAIN", None) != "true":
            from .tasks import fetch_youtube_data

            print("Scheduling")
            scheduler = django_rq.get_scheduler("default")

            # Delete any existing jobs in scheduler
            for job in scheduler.get_jobs():
                job.delete()

            # run every minute
            scheduler.schedule(
                datetime.utcnow(),
                func=fetch_youtube_data,
                args=[],
                kwargs={},
                interval=60,
                repeat=None,
                meta={"foo": "bar"},
            )
