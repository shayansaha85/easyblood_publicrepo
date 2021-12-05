# t = (('Shayan Saha', 'O+', '799001', '9774162637'), ('Pranjit Chowdhury', 'O+', '799001', '9862997186'))

def generating_html_table(fetched_data):
    html_data = []
    html_data.append("<table>")
    html_data.append("<thead>")
    
    columns = ["Firsntname", "District", "Phone"]
    for x in columns:
        html_data.append(f"<th>{x}</th>")
    html_data.append("</thead>")

    data = list(fetched_data)

    for x in data:  
        html_data.append("<tr>")
        for y in x:
            html_data.append(f"<td>{y}</td>")
        html_data.append("</tr>")
    html_data.append("</table>")

    s = ""
    for x in html_data:
        s = s + x + "\n"
    
    content = ""
    cols = "Firstname,District,Phone"
    content = content + cols + "\n"
    for x in fetched_data:
        content = content + str(x)[1:-1].replace("'","") + "\n"
    f = open("additional_data/table.csv", "w")
    f.write(content)
    f.close()
    return s
