from rest_framework.viewsets import ModelViewSet
from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
import os
import openai


openai.api_key = os.environ["OPENAI_KEY"]

class RecommendViewSet(ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer


def generate_prompt(prompt):
    return str(
        "안녕 나는 여행 코스 추천 회사의 매니저야.\n"
        "너에게 여행 코스 추천을 도움 받으려고 해.\n"
        "내가 유저의 여행 관련 정보들을 제시해줄테니 여행 코스를 짜줘.\n"
        "고객은 대한민국 국민이고, 언급이 굳이 없으면 해외 여행지를 추천해줘도 좋아.\n"
        "경비는 인당 기준이고, 총 여행기간 동안 쓸 수 있는 경비야.\n"
        "비행기를 타야하는 거리라면 첫날과 마지막 날은 비행기 타는 시간도 고려해서 짜줘\n"
        "일자별로 물어볼게 답변은 장소에 대한 설명 없이 장소만 추천해줘\n\n"

        f"시기: {prompt['month']}\n"
        f"지역: {prompt['where']}\n"
        f"날짜: {prompt['duration']}\n"
        f"여행 경비: 인당 {prompt['budget']}\n"
        f"여행 키워드: {prompt['keyword']}\n"
        f"여행 목적: {prompt['purpose']}\n"
        f"여행 동반자: {prompt['accompany']}\n"
    )

def event_stream_generator(prompt):
    duration = int(prompt['duration'])
    messages = [
        {"role": "user", "content": f"{generate_prompt(prompt)}"}
    ]
    for i in range(duration):
        full_message = ''
        messages.append({"role": "user", "content": f"{i+1}일차 일정 추천해줘. 오전, 점심, 오후, 저녁으로 나누어 추천해줘. 장소와 비용, 간략한 설명을 첨부해서 부탁해"})
        yield f"<h3>{i+1}일차:</h3>"
        for chunk in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0,
            stream=True,
        ):
            if chunk["choices"][0]["delta"].get("content") is not None:
                content = chunk["choices"][0]["delta"].get("content")
                full_message = str(full_message) + str(content)
                yield content
            else:
                yield '\n\n'
        messages.append({"role": "assistant", "content": f"{full_message}"})


@api_view(["POST"])
def generate_answer(request):
    prompt = request.data.get("state", "")    
    response = StreamingHttpResponse(event_stream_generator(prompt), content_type='text/plain')
    response['Cache-Control'] = 'no-cache'

    return response
