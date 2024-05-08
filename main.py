# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# tree_data = {
#     "name": "CEO",
#     "children": [
#         {
#             "name": "Manager",
#             "children": [
#                 {"name": "Foreman", "children": [{"name": "Worker", "children": [{"name": "Pickachu"}, {"name": "Raichu"}]}]},
#                 {"name": "Forewoman", "children": [{"name": "Wrestler"}]}
#             ]
#         },
#         {
#             "name": "Developer",
#             "children": [
#                 {"name": "MERN stack", "children": [{"name": "React", "children": [{"name": "Bilal"}, {"name": "Model"}]}]},
#                 {"name": "Android", "children": [{"name": "Kotlin Developer"}]}
#             ]
#         }
#     ]
# }

# @app.get("/tree_data")
# async def get_tree_data():
#     return JSONResponse(content=tree_data)

# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse

# app = FastAPI()

# # Initial tree data
# initial_tree_data = {
#     "id": 1,
#     "name": "CEO",
#     "children": []
# }

# # Children tree data
# children_tree_data = {
#     1: {
#         "name": "CEO",
#         "children": [
#             {
#                 "id": 2,
#                 "name": "Manager",
#                 "children": []
#             },
#             {
#                 "id": 3,
#                 "name": "Developer",
#                 "children": []
#             }
#         ]
#     },
#     2: {
#         "name": "Manager",
#         "children": [
#             {
#                 "id": 4,
#                 "name": "Foreman",
#                 "children": []
#             },
#             {
#                 "id": 5,
#                 "name": "Forewoman",
#                 "children": []
#             }
#         ]
#     },
#     3: {
#         "name": "Developer",
#         "children": [
#             {
#                 "id": 6,
#                 "name": "MERN stack",
#                 "children": []
#             },
#             {
#                 "id": 7,
#                 "name": "Android",
#                 "children": []
#             }
#         ]
#     },
# }

# @app.get("/initial_tree_data")
# async def get_initial_tree_data():
#     return JSONResponse(content=initial_tree_data)

# @app.get("/children_tree_data/{node_id}")
# async def get_children_tree_data(node_id: int):
#     if node_id not in children_tree_data:
#         raise HTTPException(status_code=404, detail="Node not found")
#     return JSONResponse(content=children_tree_data[node_id])

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Initial tree data
initial_tree_data = {
    "id": 1,
    "name": "CEO",
    "children": []
}

# Children tree data
children_tree_data = {
    1: {
        "name": "CEO",
        "children": [
            {
                "id": 2,
                "name": "Manager",
                "children": []
            },
            {
                "id": 3,
                "name": "Developer",
                "children": []
            }
        ]
    },
    2: {
        "name": "Manager",
        "children": [
            {
                "id": 4,
                "name": "Foreman",
                "children": []
            },
            {
                "id": 5,
                "name": "Forewoman",
                "children": []
            }
        ]
    },
    3: {
        "name": "Developer",
        "children": [
            {
                "id": 6,
                "name": "MERN stack",
                "children": []
            },
            {
                "id": 7,
                "name": "Android",
                "children": []
            }
        ]
    },
    4: {
        "name": "Manager",
        "children": [
            {
                "id": 5,
                "name": "Foreman",
                "children": []
            },
            {
                "id": 6,
                "name": "Forewoman",
                "children": []
            }
        ]
    },
    7: {
        "name": "Developer",
        "children": [
            {
                "id": 9,
                "name": "MERN stack",
                "children": []
            },
            {
                "id": 8,
                "name": "Android",
                "children": []
            }
        ]
    },
    5: {
        "name": "Foreman",
        "children": [
            {
                "id": 10,
                "name": "Worker",
                "children": []
            }
        ]
    },
    6: {
        "name": "Forewoman",
        "children": [
            {
                "id": 11,
                "name": "Wrestler",
                "children": []
            }
        ]
    },
    9: {
        "name": "MERN stack",
        "children": [
            {
                "id": 12,
                "name": "React",
                "children": []
            }
        ]
    },
    12: {
        "name": "React",
        "children": [
            {
                "id": 13,
                "name": "Bilal",
                "children": []
            },
            {
                "id": 14,
                "name": "Model",
                "children": []
            }
        ]
    },
    8: {
        "name": "Android",
        "children": [
            {
                "id": 15,
                "name": "Kotlin Developer",
                "children": []
            }
        ]
    },
    10: {
        "name": "Worker",
        "children": [
            {
                "id": 16,
                "name": "Pickachu",
                "children": []
            },
            {
                "id": 17,
                "name": "Raichu",
                "children": []
            }
        ]
    },
    11: {
        "name": "Wrestler",
        "children": []
    },
    13: {
        "name": "Bilal",
        "children": []
    },
    14: {
        "name": "Model",
        "children": []
    },
    15: {
        "name": "Kotlin Developer",
        "children": []
    },
    16: {
        "name": "Pickachu",
        "children": []
    },
    17: {
        "name": "Raichu",
        "children": []
    }
}


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/initial_tree_data")
async def get_initial_tree_data():
    return JSONResponse(content=initial_tree_data)

@app.get("/children_tree_data/{node_id}")
async def get_children_tree_data(node_id: int):
    if node_id not in children_tree_data:
        raise HTTPException(status_code=404, detail="Node not found")
    return JSONResponse(content=children_tree_data[node_id])

