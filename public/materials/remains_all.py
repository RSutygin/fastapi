def remains_all_html(remains_list):
    result = '''<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1 " charset="utf-8">
    <title>Остатки всех материалов</title>
</head>
<body>
    <h2>Остатки всех материалов</h2>
'''
    for remain in remains_list:
        result += f'''   <p>{str(remain[0])}: {str(remain[1])}</p>
'''
    result += '''</body>
</html>'''
    return result
