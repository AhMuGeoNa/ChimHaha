from django.shortcuts import render
from chim_channel.models import *
from datetime import datetime
# Create your views here.

def index(request):

    
    ## DB에서 가장 최신 영상 가져오는 코드
    video_db = Videos.objects.order_by('-published_date')[0]

    ## iso8061 시간대 형식을 변환해주는 코드 
    published_date = str(video_db.published_date)
    published_date = datetime.fromisoformat(published_date)

    ## UTC 시간대에서 한국 시간대로 맞춰주는 코드 
    published_date = published_date.timestamp() + 32400
    published_date = datetime.fromtimestamp(published_date).strftime('%Y/%m/%d - %H:%M:%S')
	
    context = {'videos' : video_db, 'published_date' : published_date}
    return render(request, 'index.html', context = context)