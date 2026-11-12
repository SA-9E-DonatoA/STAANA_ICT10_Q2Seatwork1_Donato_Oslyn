from pyscript import document

club_members = ["liam anderson", "emma thompson", "noah bennett", "mia collins",
                "lucas mitchell", "olivia parker", "ethan brooks", "ava morgan",
                "james cooper", "isabella reed", "mason bailey", "amelia foster",
                "logan hughes", "harper kelly", "elijah ward", "charlotte price",
                "benjamin ross", "evelyn james", "henry scott", "abigail turner"]


def candidate_checker(e):
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    candidate = f_name + " " + l_name

    member_checker = candidate.lower() in club_members

    messages = (
        f"Sorry {candidate.title()}, your name is not on the list.",
        f"Congratulations {candidate.title()}! You are now part of the ICT club.",
    )

    document.getElementById("result").innerHTML = messages[member_checker]

    