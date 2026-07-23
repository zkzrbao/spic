import uvicorn

if __name__ == '__main__':
    try: uvicorn.run('main:app',host='0.0.0.0', port=8190, reload=True)
    except Exception as e: raise e
