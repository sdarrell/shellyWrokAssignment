import json


def read_json_file():
    # Opening JSON file
    f = open('./workers.json', 'r')

    # returns JSON object as a dictionary
    data = json.load(f)
    f.close()
    return data


def gen_html_table(data):
    tbl = "<table>"
    if len(data["workers"]) > 0:
        tbl += "<tr>"
        for headers in data["workers"][0]:
            tbl += f"<th> {headers} </th>"
        for entry in data["workers"]:
            tbl += "<tr>"
            for _, value in entry.items():
                tbl += f"<td> {value} </td>"
            tbl += "</tr>"
    tbl += "</table>"
    return tbl


def create_html_page():
    tbl = gen_html_table(read_json_file())
    html_content = f"""<html>
                            <head>
                            <link rel=stylesheet href='./table_style.css'>
                                <title>Shelly's Assignment</title>
                                
                            </head>
                            <body><input id="SearchBar" type="text" onInput="updateTable()" />{tbl}</body>
                        </html>"""

    with open("./html_page.html", "w+") as f:
        f.write(html_content)


if __name__ == '__main__':
    create_html_page()
