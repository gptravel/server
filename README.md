# travel.gpt - 여행 코스 추천 서비스

20180863 윤태호<br>
AI융합캡스톤디자인과창업 - 하정욱 교수님

## Preview
### 정보 입력 페이지
![gptravel](https://user-images.githubusercontent.com/105200642/235815698-e832a1b5-f768-4ae1-882e-fce0db2509a4.png)
날짜, 기간, 여행지, 총예산, 여행 키워드와 목적, 동행인의 정보를 입력받아 추천해줍니다!

***
### 추천 페이지
![gptrecommend](https://user-images.githubusercontent.com/105200642/235815878-9d851325-f20d-4f26-80e5-fe93e5da40e1.png)
일자 별 시간을 나누어 추천해줍니다!

***


## Overview
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/105200642/235817563-95628f8c-02cb-4d88-81ee-83fbc2c8571f.png">

* openai api를 사용하여 백엔드와 GPT 소통
* 프론트엔드에서 유저의 입력값을 받아오면 백엔드 서버에서 gpt 서버로 전달, 답변 받아옴
* API : chat completion
* Model : gpt-3.5-turbo
* max_tokens, temperature, stream 등의 하이퍼 파라미터 사용

[여행지 추천 받기](https://client-seven-gray.vercel.app/)
