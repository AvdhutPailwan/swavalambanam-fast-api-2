def quiz_entity(item) -> dict:
    if item is not None:
        return {
            "Question": item["Question"],
            "optionOne": item["optionOne"],
            "optionTwo": item["optionTwo"],
            "optionThree": item["optionThree"],
            "optionFour": item["optionFour"],
            "correctAns": item["correctAns"]
        }
    else:
        return {}


def quiz_entities(items):
    return [quiz_entity(item) for item in items]
