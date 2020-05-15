import re
from subprocess import Popen, PIPE

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from jyutping.jyutping import get_jyutping
from synthesizer.models import Transcript
from .forms import TranscriptForm
import json
from django.http import HttpResponse, Http404, StreamingHttpResponse

# import json
# from django.http import HttpResponse
 
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
 

# @csrf_exempt
# def my_api(request):
#     dic = {}
#     if request.method == 'GET':
#         dic['message'] = 0
#         return HttpResponse(json.dumps(dic))
#     else:
#         dic['message'] = '方法错误'
#         return HttpResponse(json.dumps(dic, ensure_ascii=False))


class SendDataToFrontEndProView(View):
    """专门从后端传递所需数据给前端

    method: Post
    access_url: http://ip:port/senddata
    """
    def get(self, request):
        """处理post请求

        Args:
            NA
        Returns:
            NA
        """
        status = "ok"
        data = [{"data0":"A"}, {"data1":"B"}, {"data2":"C"},]

        return HttpResponse(json.dumps({
            "status": status,
            "data":data,
        }))
    
    # def post(self, request):
    #     """处理post请求

    #     Args:
    #         NA
    #     Returns:
    #         NA
    #     """
    #     status = "ok"
    #     data = [{"data0":"A"}, {"data1":"B"}, {"data2":"C"},]

    #     return HttpResponse(json.dumps({
    #         "status": status,
    #         "data":data,
    #     }))    

# Create your views here.
class IndexView(TemplateView):
    # print("i am here 0")
    template_name = "index.html"


class TranscriptView(View):
    form = TranscriptForm
    # print("origin form:",form)
    template_name = "transcript.html"
    # print("i am TranscriptView")
    def get(self, request):
        form = self.form(request.POST)
        print("get form:",form)
        return render(self.request, self.template_name, {"form": form})

    def post(self, *args, **kwargs):
        pk = "/media/wav/cn.wav"
        if self.request.method == "POST" and self.request.is_ajax():
            form = self.form(self.request.POST)
            print("post form:",form)
            if form.is_valid():
                transcript = form.cleaned_data['transcript']
                transcript = re.sub("[，。, . ]+", "", transcript)
                jyutping = " ".join(get_jyutping(transcript))

                model = Transcript(transcript=transcript, jyutping=jyutping)
                model.save()
                pk = str(model.id)
                # subprocess.call(['./ossian.sh', str(pk), jyutping], shell=True)
                process = Popen(['sudo', './ossian.sh', pk, jyutping], stdin=PIPE, stdout=PIPE,
                                stderr=PIPE, shell=False)
                # output = process.communicate()[0]
                output = process.wait()
                pk = pk + ".wav"
            return JsonResponse({"success": True, "path": str("/media/wav/{}".format(pk))}, status=200)
        return JsonResponse({"success": False}, status=400)
