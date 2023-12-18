def remains_html(material_list):
    result = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1 " charset="utf-8">
    <title>Остатки материалов</title>
</head>
<body>
    <div id="message"></div>
    <p>
        <h2>Остатки материалов</h2>
    </p>
    <p>
        Выберите наименование материала: <br />
        <select name="material_name" id="material_name">
"""
    for i in material_list:
        result += """           <option value="""+i+""">"""+i+"""</option>\n"""
    result += """       </select>
    </p>
    <button onclick="send()">Остаток выбранного материала</button><br><br>
    <form action="remains_all_result" method="get">
        <input type="submit" value="Остатки всех материалов" />
    </form>
<script>
    async function send(){

        // получаем введенное в поле имя и возраст
        const material_name = document.getElementById("material_name").value;

        // отправляем запрос
        const response = await fetch("/remain_result", {
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
<script>
    async function send_all(){

        // получаем введенное в поле имя и возраст
        const material_name = document.getElementById("material_name").value;

        // отправляем запрос
        const response = await fetch("/remains_all_result", {
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
