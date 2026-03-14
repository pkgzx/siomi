#!/bin/bash

run(){
    if [ -z "$1" ]; then 
        uv run uvicorn src.app.main:app
    elif [ "$1" == "dev" ]; then
        uv run  uvicorn src.app.main:app --reload
    fi
}

run $1