import requests
import traceback
import base64
from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/{datas}")
def run_main(datas:str):
    try:
        datas=base64.b64decode(datas).decode()+"\n"
        datas=datas.split("\n")
        del datas[-1]
        for i in range(5-len(datas)):
            datas.append(None)
        post_type,url,data,headers,encoding=datas
        if post_type in ["get","post","head","options","put","delete","patch","trace","connect"]:
            req=eval(f"requests.{post_type}(\"{url}\",data={data},headers={headers})")
            req.encoding=encoding
            return {"apierror":"No error","status":req.status_code,"return":req.text}
        else:
            return {"apierror":"post_type most in get,post,head,options,put,delete,patch,trace,connect"}
    except:
        return {"apierror":traceback.format_exc()}
    