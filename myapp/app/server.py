from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes


app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

from together_chain import chain as together_chain
add_routes(app, together_chain, path="/together")

from openrouter_chain import chain as openrouter_chain
add_routes(app, openrouter_chain, path="/openrouter")

from llm_chain import chain as llm_chain
add_routes(app, llm_chain, path="/llm")

from gemini_chain import chain as gemini_chain
add_routes(app, gemini_chain, path="/gemini")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
