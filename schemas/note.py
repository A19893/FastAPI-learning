def noteEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
    }

def notesEntity(items) -> list:
  return [noteEntity(item) for item in items]