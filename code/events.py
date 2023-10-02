import csv # Forked

filename = 'players_updated.csv'

fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 

updated_events = fields
updated_rows = []

updated_events.remove('Event')
updated_events.append('Goal')
updated_events.append('SubIn')
updated_events.append('SubOut')
updated_events.append('RedCard')
updated_events.append('YellowCard')
updated_events.append('PenaltyScored')
updated_events.append('PenaltyMissed')
updated_events.append('OwnGoal')

print(updated_events)

temp_row = []
for row in rows:
    temp_row = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],'','','','','','','','']
    
    if row[8] == '':
        updated_rows.append(temp_row)
    else:
        if row[8][0:2] == 'OH':
            temp_row[10] = row[8][2:-1]
            #print(temp_row)
        if row[8][0] == 'G':
            temp_row[8] = row[8][1:-1]
            #print(temp_row)
            
        if row[8][0] == 'I':
            temp_row[9] = row[8][1:-1]
            #print(temp_row)
        if row[8][0:2] == 'IH':
            temp_row[9] = row[8][2:-1]
            print(temp_row)
            
        if row[8][0] == 'O':
            temp_row[10] = row[8][1:-1]
            #print(temp_row)
            
        if row[8][0] == 'R':
            temp_row[11] = row[8][1:-1]
            #print(temp_row)
        
        if row[8][0:3] == 'RSY':
            temp_row[11] = row[8][3:-1]
    
        if row[8][0] == 'Y':
            temp_row[12] = row[8][1:-1]
            #print(temp_row)
            
        if row[8][0] == 'P':
            temp_row[13] = row[8][1:-1]
            #print(temp_row)
            
        if row[8][0:2] == 'MP':
            temp_row[14] = row[8][2:-1]
            #print(temp_row)
            
        if row[8][0] == 'W':
            temp_row[15] = row[8][1:-1]
        updated_rows.append(temp_row)


with open('players_fixed.csv', 'w',newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(updated_events)
    write.writerows(updated_rows)



        

