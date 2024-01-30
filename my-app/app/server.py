from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()


from company_name_chain import chain as company_name_chain
add_routes(app, company_name_chain, path="/company-name")

from llm_chain import chain as llm_chain
add_routes(app, llm_chain, path="/llm")

from z_value_params_chain import chain as z_value_params_chain
add_routes(app, z_value_params_chain, path="/z_value_params")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
