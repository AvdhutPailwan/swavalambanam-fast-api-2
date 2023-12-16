def theory_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "theory": item["theory"],
        "video_code": item["video_code"],
        "chapter_name": item["chapter_name"]
    }


def theories_entity(items) -> list:
    li = []
    for item in items:
        li.append(theory_entity(item))
    return li


# def example_entity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "answer": item["answer"]
#     }
