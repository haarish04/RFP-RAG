from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from app.utils.load_file import load_csv_file, load_questions_file
from app.services.embedding import embed_texts
from app.api.models import QueryRequest
from app.utils.chroma import query_chroma_with_similarity, add_to_chroma, delete_collection
from app.services.llm import ask_llama
from app.utils.response_writer import write_response_to_excel
import uuid

router = APIRouter()

@router.post("/create_collection")
async def ingest(file: UploadFile= File(...), record_name: str= Form(...)):
    if not file.filename.endswith((".xlsx",".xls",".csv")):
        raise HTTPException(status_code=500, detail="Invalid file type")
    try:
        data = await load_csv_file(file)
        questions = [row["Question"] for row in data]
        embeddings = embed_texts(questions)
        ids=[str(uuid.uuid4()) for _ in data]
        response = add_to_chroma(ids, embeddings, data, record_name)
        return response
    
    except HTTPException as he:
        raise he

    except Exception as e:
        raise HTTPException(status_code=500, detail={e})

@router.delete("/delete_collection")
async def delete(collection_name: str= Form(...)):
    try:
        response = delete_collection(collection_name)
        return response
    
    except HTTPException as he:
        raise he
    
    except Exception as e:
        raise HTTPException(status_code=500, detail={e})



@router.post("/query")
async def query(file: UploadFile= File(...)):
    try:
        data = await load_questions_file(file)
        questions = [row["Question"] for row in data]

        results=[]
        for ques in questions:

            top_results, best_result = query_chroma_with_similarity(ques)

            context = best_result.get("metadata","")
            llm_answer= ask_llama(ques, context)

            results.append( {
                "question": ques,
                "matches": top_results,
                "LLM answer": llm_answer
            })

        output_excel = write_response_to_excel(results)
        filename = "query_results.xlsx"

        return StreamingResponse(
            output_excel,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")