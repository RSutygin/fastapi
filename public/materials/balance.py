def balance_html(material_list):
    result = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1 " charset="utf-8">
    <title>Удаление материала</title>
</head>
<body>
    <div id="message"></div>
    <p>
        <h2>Расходы/приходы материала</h2>
    </p>
    <p>
        Выберите наименование материала: <br />
        <select name="material_name" id="material_name">
"""
    for i in material_list:
        result += """           <option value="""+i+""">"""+i+"""</option>\n"""
    result += """       </select>
    </p>
    <p>
        Выберите необходимое действие: <br>
        <select name="action" id="action">
            <option value="Расход">Расход</option>
            <option value="Приход">Приход</option>
        </select>
    </p>
    <p>
        Выберите даты: <br>
        c:
        <input type="date" id="date1" name="date1">
        по: 
        <input type="date" id="date2" name="date2">
    </p>
    <button onclick="send()">Рассчитать</button>
<script>
    async function send(){

        // получаем введенное в поле имя и возраст
        const material_name = document.getElementById("material_name").value;
        const date1 = document.getElementById("date1").value;
        const date2 = document.getElementById("date2").value;
        const action = document.getElementById("action").value;

        // отправляем запрос
        const response = await fetch("/balance_result", {
                method: "POST",
                headers: { "Accept": "application/json", "Content-Type": "application/json" },
                body: JSON.stringify({
                    name: material_name,
                    date1: date1,
                    date2: date2,
                    action: action
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
