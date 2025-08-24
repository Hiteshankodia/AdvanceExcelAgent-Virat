from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
import asyncio
from pandas_agent import execute_query

app = FastAPI()


# Input schema
class QueryInput(BaseModel):
    text: str


@app.post("/execute")
async def markdownify(input_data: QueryInput):
    """
    Accept text input, run execute_query in a thread, and return markdown string.
    """
    # Run your sync function in a thread to keep things async-friendly
    markdown_output = await asyncio.to_thread(execute_query, input_data.text)
    print(markdown_output)
    return markdown_output


