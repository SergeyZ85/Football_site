from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def main():
    return 'Dziuba best player in the world'