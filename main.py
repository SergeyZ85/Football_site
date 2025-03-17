from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def main():
    return 'Cristiano Ronaldo best player in the world'