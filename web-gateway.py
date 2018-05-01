import os
import yaml
import web

from GreyMatter.SenseCells.tts import tts

render = web.template.render('templates/')
# render takes the location of the templates as an argument
urls = ('/', 'index',)

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# functioning variablea
name = profile_data['name']

# welcome message
tts('Welcome ' + name + ' systems are now ready to run. How can I help you?')

class index:
    def GET(self):
        return render.index()
    
    def POST(self):
        x = web.input(myfile={})
        filedir = os.getcwd() + '/uploads'
        if 'myfile' in x:
            filepath = x.myfile.replace('\\', '/')
            # replace the windows-style slashes with linux ones
            filename = filepath.split('/')[-1]
            # splits the command and chooses the last part (the filename with extension)
            
            fout = open(filedir + '/' + filename, 'w')
            # creates the directory where the updaloaded file should be stored
            
            fout.write(x.myfile.file.read())
            # writes the uploaded file to the newly created file
            fout.close()
            
            os.system('python main.py ' + filename)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    
    