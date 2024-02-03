###### 기본 정보 설정 단계 ######
from fastapi import Request, FastAPI

###### 서버 생성 단계 #####

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TelegramChatbot"}

@app.post("/chat/")
async def chat(request: Request):
    telegramrequest = await request.json()
    print(telegramrequest)
    return 0