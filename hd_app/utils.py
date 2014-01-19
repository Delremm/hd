import requests
import json
from hd_app.models import Tag, Startup


def get_tags(begin=1, end=50):
    tags = []
    tags_json = []
    for i in range(begin, end):
        r = requests.get('https://api.angel.co/1/tags/%s/' % i)
        tags.append(json.loads(r.text))
        tags_json.append(r.text)
    return [tags, tags_json]


def get_startups(tag_id=1, last_page=None):
    startups = []
    startups_json = []
    first_r = requests.get('https://api.angel.co/1/tags/%s/startups/' % tag_id)
    first_r_dict = json.loads(first_r.text)
    last_page_row = first_r_dict['last_page']
    per_page = first_r_dict['per_page']
    total = first_r_dict['total']
    if last_page and (last_page < last_page_row):
        last_page_row=last_page
    for p in range(1, int(last_page_row)+1):
        params = {'page': p}
        r = requests.get('https://api.angel.co/1/tags/%s/startups/' % tag_id, params=params)
        startups.append(json.loads(r.text))
        startups_json.append(r.text)
    return [startups, startups_json]

def tags_to_db(begin=1, end=10):
    tags = get_tags()
    for t in tags[0]:
        if ('id' in t) and t['id']:
            tag = Tag.objects.get_or_create(row_id=t['id'])
            if ('name' in t) and t['name']:
                tag[0].name = t['name']
            if ('angellist_url' in t) and t['angellist_url']:
                tag[0].al_url = t['angellist_url']
            if ('display_name' in t) and t['display_name']:
                tag[0].title = t['display_name']
            tag[0].save()


def startups_to_db(tag_id, last_page=None):
    startups = get_startups(tag_id=tag_id, last_page=last_page)
    for page in startups[0]:
        for su in page['startups']:
            if (('id' in su) and su['id']) and (('hidden' in su) and (not su['hidden'])):
                startup = Startup.objects.get_or_create(row_id=su['id'], hidden=su['hidden'])[0]
                if ('name' in su) and su['name']:
                    startup.name = su['name']
                #TODO: location
                if ('angellist_url' in su) and su['angellist_url']:
                    startup.al_url = su['angellist_url']
                if ('hidden' in su) and su['hidden']:
                    startup.hidden = su['hidden']
                if ('follower_count' in su) and su['follower_count']:
                    startup.follower_count = su['follower_count']
                if ('created_at' in su) and su['created_at']:
                    startup.created_at = su['created_at']
                if ('fundraising' in su) and su['fundraising']:
                    startup.fundraising = json.dumps(su['fundraising'])
                tag = Tag.objects.filter(row_id=tag_id)
                if tag:
                    try:
                        startup.tags.add(tag[0])
                    except:
                        pass
                startup.save()

    print('startups_to_db')
    # row_id = models.IntegerField(null=True, blank=True)
    # name = models.CharField(max_length=1000, blank=True, null=True)
    # location = models.CharField(max_length=1000, blank=True, null=True)
    # al_url = models.CharField(max_length=1000, null=True, blank=True)
    # hidden = models.BooleanField(default=False)
    # follower_count = models.IntegerField(null=True, blank=True)
    # product_desc = models.TextField(null=True, blank=True)
    # quality = models.IntegerField(blank=True, null=True)
    # twitter_url = models.CharField(max_length=1000, null=True, blank=True)
    # company_url = models.CharField(max_length=1000, null=True, blank=True)
    # created_at = models.CharField(max_length=255, null=True, blank=True)
    # fundraising = models.TextField(null=True, blank=True)
    # tags = models.ManyToManyField(Tag, null=True, blank=True)




# if __name__=='__main__':
    # tags = get_tags()
    # with open('tags_50', 'w+') as f:
        # f.write(json.dumps(tags[0]))

    # startups = get_startups(tag_id=41, last_page=1)    
    # with open('startups_41', 'w+') as f:
    #     f.write(json.dumps(startups[0]))

