   # people = [
    #     {
    #         "given_name": "Alfonsa",
    #         "family_name": "Ruiz",
    #         "title": "Senior Software Engineer",
    #     },
    #     {
    #         "given_name": "Sayid",
    #         "family_name": "Khan",
    #         "title": "Project Manager",
    #     },
    # ]


def format_data_for_display(data):
    return [item.get('given_name') +" " + item.get('family_name') + ": " + item.get('title') for item in data]

def format_data_for_excel(data):
    ans = ""
    for key in data[0].keys():
        ans += key.split("_")[0]+','
    
    ans = ans[:-1]+"\n"
    for d in data:
        ans+=d.get('given_name')+","+d.get('family_name')+","+d.get('title')+'\n'
    # print(ans)
    return ans