import uvicorn
#logs levels:
#TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="DEBUG",
        workers=4
    )