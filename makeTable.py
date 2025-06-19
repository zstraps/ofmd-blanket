import json

# Open and read the JSON file
with open('sentences.json', 'r') as file:
    sentences = json.load(file)


with open('dimensions.json', 'r') as file:
    dimensions = json.load(file)

for block in dimensions:
    season = block['Season']
    episode = block['Episode']
    columns = block['columns']
    rows = block['rows']

    ep_sentences = [sentence for sentence in sentences if sentence['Season #'] == season and sentence['Episode #'] == episode]


    sumWords = 0
    for sentence in ep_sentences:
        mycnt = sentence['Count words']
        sumWords += mycnt

    sumStitches = rows * columns

    diff = sumWords - sumStitches
    absDiff = abs(diff)

    print("\n\n")
    print("s" + str(round(sentence['Season #'])) + "e" + str(round(sentence['Episode #'])))
    print(round(diff))


    if diff == 0:
        sentences_new = ep_sentences

    else:
        sentences_bylength_pre = sorted(ep_sentences, key=lambda x: x['Count words'], reverse=True)
        sentences_bylength = sorted(sentences_bylength_pre, key=lambda x: x['Locked'])
        
        modified_sentences = []

        i = 0
        while i < len(sentences_bylength):
            s = sentences_bylength[i]

            if i < absDiff:
                if diff < 0:
                    newcount = s['Count words'] + 1
                elif diff > 0:
                    newcount = s['Count words'] - 1
                s.update({'Count words': newcount})
                modified_sentences.append(s)
                print(s['Sentence'])
            else:
                modified_sentences.append(s)

            i += 1

        sentences_new = sorted(modified_sentences, key=lambda x: x['Sort order'])



    with open('characters.json', 'r') as file:
        characters = json.load(file)



    # to open/create a new html file in the write mode 
    f = open('patterns/OFMDblanketS'+ str(round(season)) + 'E' + str(round(episode)) + '.html', 'w') 
      


    table_cells = []

    for sentence in sentences_new:
        i = 0
        while i < sentence['Count words']:
            speaker = str(sentence.get('Speaker', 'Unknown'))
            speaker_upper = speaker.upper()
            color = characters.get(speaker_upper)
            cell = "<td class='" + speaker_upper.replace(" ","-").replace("/","-").replace("'","-").replace("???","unknown") + "' style='background:" + color + "88;'>" + speaker + "</td>"
            table_cells.append(cell)
            i += 1


    cell_sets = [] 

    for i in range(0, len(table_cells), columns):  # Slice list in steps of n
        cell_sets.append(table_cells[i:i + columns])

        
    border_row = "<tr>" + "<td style='background: #CDB69B88;'></td>"*(columns+2) + "</tr>"

    if rows % 2 == 0:
        table = "<tr style=\"display:none;\"></tr>"
    else:
        table=""


    table = table + border_row

    for set in cell_sets:
        table = table + "<tr><td style='background: #CDB69B88;'></td>" + ' '.join(set) + "<td style='background: #CDB69B88;'></td></tr>"

    table = table + border_row



    # the html code which will go in the file GFG.html 
    html_template = """<html> 
    <head> 
    <title>OFMD blanket</title>
    <link rel="stylesheet" href="pattern_style.css"/>
    </head> 
    <body> 
    <h2>Blanket pattern s""" + str(round(season)) + "e" + str(round(episode)) + """</h2>
    <div class="subhead">""" + str(columns + 2) + "x" + str(rows + 2) + """ (with borders)</div>
    <a class="home-button" href="../index.html">< All patterns</a>
      
    <table>""" + table + """</table>
      
    </body> 
    </html> 
    """
      
    # writing the code into the file 
    f.write(html_template) 
      
    # close the file 
    f.close() 
