from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    f = open("data/demofile2.txt", "a")
    f.write("Now the file has more content! \n")
    f.close()

    return 'OK'
