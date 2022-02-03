from django.shortcuts import render
from . import scrape

# def home(request):
#     return render(request,'scraper/requests.html')

def response(request):
    result = scrape.RONBsearch()
    print(result)
    # return render(request,'scraper/response.html',{'data' : result.items()})
    # result = { 
    #        'tweets': ['sunil','Doleshor','sunil','Doleshor','sunil','Doleshor','sunil','Doleshor'],
    #        'likes': [1000,10000,1000,10000,1000,10000,1000,10000],
    #        'retweets_count':[300,700,300,700,300,700,300,700]
    #        }
    return render(request,'scraper/response.html',{
        'tweets': result['tweets'],
        'likes' : result['likes'],
        'retweets_count': result['retweets_count']
    })