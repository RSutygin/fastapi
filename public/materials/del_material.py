def delete_html(material_list):
    result = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1 " charset="utf-8">
    <title>Удаление материала</title>
</head>
<body>
    <div id="message"></div>
    <p>
        <h2>Удаление материала</h2>
    </p>
    <p>
        Выберите наименование материала: <br />
        <select name="material_name" id="material_name">
"""
    for i in material_list:
        result += """           <option value="""+i+""">"""+i+"""</option>\n"""
    result += """       </select>
    </p>
    <button onclick="send()">Удалить материал</button>
<script>
    async function send(){

        // получаем введенное в поле имя и возраст
        const material_name = document.getElementById("material_name").value;

        // отправляем запрос
        const response = await fetch("/del_result", {
                method: "POST",
                headers: { "Accept": "application/json", "Content-Type": "application/json" },
                body: JSON.stringify({
                    name: material_name,
                })
            });
            if (response.ok) {
                const data = await response.json();
                document.getElementById("message").textContent = data.message;
            }
            else
                console.log(response);
    }
</script>
</body>
</html>"""
    return result
