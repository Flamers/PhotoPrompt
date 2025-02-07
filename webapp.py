from flask import Flask
import csv
import os
import sys
import random
import datetime
import time

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/web_page')
def prompt_out():
    current_time = int(time.time())
    os.chdir(sys.path[0])
    update_time =open("change_time.txt", "r")
    chosen_prompt = "None, you bastard"
    for line in update_time:
        if current_time > int(line):
            file_contents =open("change_time.txt", "r")
            for line in file_contents:  
                line= int(line)
                new_time = line + 2419200
                #print(new_time)
            with open("change_time.txt", "w") as file:
                file.write(str(new_time)) 
            prompt_list=[]
            previous_prompt=[]
            with open('prompts.csv','r') as file:
                reader = csv.reader(file)
                for row in reader:
                    prompt_list.append(row[0])
            with open('previous_prompt.csv','r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for val in row:
                        previous_prompt.append(val)
            #print(previous_prompt)
            #print(prompt_list)

            prompt_pick_list=[]
            for prompt in prompt_list:
                if prompt == previous_prompt[0]:
                    continue
                else:
                    prompt_pick_list.append(prompt)
            chosen_prompt=random.choice(prompt_pick_list)
            chosen_prompt_list=[]
            chosen_prompt_list.append(chosen_prompt)
            with open('previous_prompt.csv','w') as file:
                writer=csv.writer(file,  delimiter = ",")
                writer.writerow(chosen_prompt_list)
                file.close()
            chosen_prompt = 'Chosen prompt is '+chosen_prompt
            # print('Chosen prompt is '+chosen_prompt)
        else:
            with open('previous_prompt.csv','r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for val in row:
                        print('Chosen prompt is '+val)
                        chosen_prompt = 'Chosen prompt is '+val
        return chosen_prompt
def web_page():
    return prompt_out()

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449)