str=input()

frame=['.','.','#','.','.']

for i in range(len(str)):
    if (i+1)%3 !=0:
        frame[0]+='.#.'
        frame[1]+='#.#'
        frame[2]+=f'.{str[i]}.'
        frame[3]+='#.#'
        frame[4]+='.#.'
    
    else:
        frame[0]+='..*..'
        frame[1]+='.*.*.'
        frame[2]+=f'*.{str[i]}.*'
        frame[3]+='.*.*.'
        frame[4]+='..*..'

    if (i+1)%3 ==1:
        frame[0]+='.'
        frame[1]+='.'
        frame[2]+='#'
        frame[3]+='.'
        frame[4]+='.'
    
if (len(str))%3 ==2:
        frame[0]+='.'
        frame[1]+='.'
        frame[2]+='#'
        frame[3]+='.'
        frame[4]+='.'
for line in frame:
    print(line)
    