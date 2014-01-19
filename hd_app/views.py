from django.shortcuts import render
from django.views.generic import TemplateView
import tempfile
from django.conf import settings
import uuid
import csv

from hd_app.models import Tag, Startup

class IndexView(TemplateView):
    template_name="index.html"

    def gen_csv_file_name(self):
        return '%s%s%s' % ('csv/', str(uuid.uuid4()), '.csv')
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'form_cvs' in request.GET:
            csv_file_name = self.gen_csv_file_name()
            with open('%s/%s' % (settings.MEDIA_ROOT, csv_file_name), 'w+') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow(['spam', 'love', 'peace'])
                context['css_file'] = '%s%s'  % (settings.MEDIA_URL, csv_file_name)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        tag_name=request.POST.get('tag_name')
        if tag_name:
            tag_list = Tag.objects.filter(name=tag_name)
            if tag_list:
                tag = tag_list[0]
                startups = Startup.objects.filter(tags__row_id=tag.row_id)
                csv_file_name = self.gen_csv_file_name()
                with open('%s/%s' % (settings.MEDIA_ROOT, csv_file_name), 'w+') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=',')
                    for su in startups:
                        try:
                            csv_writer.writerow([su.name, su.created_at, su.follower_count])
                        except:
                            pass
                    context['csv_file'] = '%s%s'  % (settings.MEDIA_URL, csv_file_name)
            else:
                context['message'] = 'now such tag at the moment'
            return self.render_to_response(context)
        else:
            context['message'] = 'wrong post data, "tag name is required"'

