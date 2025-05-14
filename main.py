from typing import Union
from fastapi import FastAPI
from API.SMS.sms import bomb

app = FastAPI()

@app.get("/number/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    number = str(item_id)
    return await bomb(number)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
