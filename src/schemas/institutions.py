def institution_entity(item) -> dict:
    if item is not None:
        return {
            "id": str(item["_id"]),
            "AddressUniqueNeeds": item["AddressUniqueNeeds"],
            "BehaviourOfStaff": item["BehaviourOfStaff"],
            "CollegeName": item["CollegeName"],
            "Opportunities": item["Opportunities"],
            "StaffTraining": item["StaffTraining"],
            "SupportService": item["SupportService"]
        }
    else:
        return {}


def institutions_entity(items) -> list:
    return [institution_entity(item) for item in items]
