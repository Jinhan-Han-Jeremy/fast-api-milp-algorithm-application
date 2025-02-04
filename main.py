from fastapi import FastAPI
import asyncio
import uvicorn
from typing import Union
from fastapi.responses import JSONResponse

import sys
import os

# 현재 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from milp_algorithm_ex import ParallelTeamScheduler  # 클래스 import
from milp_algorithm_ex import run_milp_scheduler  # MILP 모듈 가져오기

# FastAPI 앱 생성
app = FastAPI()

@app.get("/async/say-hello")
async def async_read_root():
    """비동기 Hello World 엔드포인트"""
    return {"async Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """아이템 ID와 선택적 질의 문자열을 반환하는 엔드포인트"""
    return {"item_id": item_id, "q": q}

@app.get("/milp/execute", response_class=JSONResponse)
async def execute_milp():
    """MILP 알고리즘 실행 및 결과 반환 API"""
    result = await run_milp_scheduler()
    return result

async def main():
    """FastAPI 서버 실행을 위한 메인 함수"""
    # 모듈 이름이 올바른지 확인하세요
    config = uvicorn.Config("main:app", port=4321, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    # 메인 이벤트 루프에서 FastAPI 실행
    asyncio.run(main())